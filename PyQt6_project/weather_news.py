# 串口调试上位机 PyQt6 串口上位机 
# 一键打包	pyinstaller -F -w weather_news.py 生成无控制台 exe #打包压缩后大小大概35M
# pyinstaller -F -w weather_news.py --upx-dir D:\tools\upx-5.0.2-win6  #加了upx打包压缩后大小大概31M 
import sys,requests,base64
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from PyQt6.QtCore import QObject, pyqtSignal, QThread,QSize
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox,QListWidget, QListWidgetItem
)
from pypinyin import lazy_pinyin, Style
from urllib.parse import urlparse, parse_qs
from readability import Document
from bs4 import BeautifulSoup,NavigableString

# ========== 配置区（无 Key） ==========
GEO_API = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_API = 'https://api.open-meteo.com/v1/forecast'
# RSS新闻源
RSS_SOURCES = [
    'https://rss.aishort.top/?type=guokr',
    'https://rss.aishort.top/?type=36kr'
]

# =====================================
# 放在 NetWorker 类外面，全局可用
def get_city_by_ip() -> str:
    """通过 IP 获取城市，失败返回北京"""
    try:
        # 大陆用户建议用这个，返回中文城市名
        r = requests.get('https://api.vore.top/api/IPdata', timeout=3)
        r.raise_for_status()
        return r.json()['adcode']['c'] or '北京'
    except Exception:
        return '北京'

def wmo_code_desc(code: int) -> str:
    """返回中文天气描述"""
    table = {
        0: "晴朗", 1: "大部晴朗", 2: "部分多云", 3: "阴天",
        45: "雾", 48: "雾凇",
        51: "毛毛雨（轻）", 53: "毛毛雨（中）", 55: "毛毛雨（浓）",
        56: "冻毛毛雨（轻）", 57: "冻毛毛雨（浓）",
        61: "小雨", 63: "中雨", 65: "大雨",
        66: "冻雨（轻）", 67: "冻雨（重）",
        71: "小雪", 73: "中雪", 75: "大雪",
        77: "雪粒", 80: "小阵雨", 81: "中阵雨", 82: "大阵雨",
        85: "小阵雪", 86: "大阵雪",
        95: "轻微雷暴", 96: "雷暴伴小冰雹", 99: "雷暴伴大冰雹"
    }
    return table.get(code, f"未知({code})")

def wind_dir_desc(deg: int) -> str:
    """风向角度→中文"""
    dirs = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    idx = int((deg + 22.5) % 360 / 45)
    return dirs[idx]

def unwrap_sina_link(redirect: str) -> str:
    """把新浪 RSS 跳转链接解包成真实文章地址"""
    try:
        return parse_qs(urlparse(redirect).query)['url'][0]
    except (KeyError, IndexError):
        return redirect          # 解析失败就原样返回

class ImgBase64Converter(QObject):   # 继承 QObject 才能发信号
    # 新增：单张图片下载完成
    img_converted = pyqtSignal(str, str)   # 原始 src → data:uri

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pool = ThreadPoolExecutor(8)   # 8 线程同时下
        self._cache = {}                    # 防止重复下载

    def convert_async(self, html: str, img_ready: pyqtSignal):
        """
        只负责“调度”：扫描所有 <img>，没缓存就丢线程池；
        每张图下完 emit(img_ready, 原始src, data_uri)。
        """
        soup = BeautifulSoup(html, 'lxml')
        for img in soup.find_all('img'):
            src = img.get('src', '').strip()
            if not src or src.startswith('data:') or src in self._cache:
                continue
            self._cache[src] = None          # 占位，防止重复提交
            self.pool.submit(self._download_one, src, img_ready)
        return str(soup)                     # 先返回带原始 src 的 html

    def _download_one(self, src: str, img_ready: pyqtSignal):
        """真正下载并 emit"""
        try:
            host = urlparse(src).netloc
            headers = {
                'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/130.0.0.0 Safari/537.36'),
                'Referer': f'https://{host}/',
                'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'
            }
            resp = requests.get(src, timeout=6, headers=headers)
            resp.raise_for_status()
            mime = resp.headers.get('Content-Type', 'image/jpeg').split(';')[0]
            b64  = base64.b64encode(resp.content).decode()
            data_uri = f'data:{mime};base64,{b64}'
            self._cache[src] = data_uri
            img_ready.emit(src, data_uri)      # 通知主线程
        except Exception:
            self._cache[src] = ''              # 失败也缓存，避免反复下

# --------------- 网络线程池 ---------------
class NetWorker(QObject):
    weather_done = pyqtSignal(dict)   # dict 或 None
    news_done    = pyqtSignal(list)   # [(title, desc), ...]
    detail_done  = pyqtSignal(str)   # 返回纯文本正文

    def __init__(self):
        super().__init__()
        self.pool = ThreadPoolExecutor(max_workers=4)

    def get_weather(self, city: str):
        self.pool.submit(self._weather_thread, city)

    def get_news(self):
        self.pool.submit(self._news_thread)

    # ---------- 天气 ----------
    def _weather_thread(self, city: str):
        try:
            city_zh = city
            # 1. 中文→拼音（带声调去掉，空格分隔）
            city = ''.join(lazy_pinyin(city, style=Style.NORMAL))
            # 1. 地理编码：拿经纬度
            r = requests.get(GEO_API, params={'name': city, 'count': 1}, timeout=5)
            r.raise_for_status()
            j = r.json()
            results = j.get('results')
            if not results:
                self.weather_done.emit(None)
                return
            lat, lon = results[0]['latitude'], results[0]['longitude']
            real_city = city_zh

            # 2. 查当前天气
            params = {
                'latitude': lat,
                'longitude': lon,
                'current_weather': 'true',
                'timezone': 'Asia/Shanghai'
            }
            r = requests.get(WEATHER_API, params=params, timeout=5)
            r.raise_for_status()
            j = r.json()
            cw = j['current_weather']
            code = int(cw.get('weathercode', -1))
            data = {
                'city': real_city,
                'temp': cw['temperature'],
                'wind': f"{cw['windspeed']} km/h",
                'wind_dir': wind_dir_desc(cw.get('winddirection', 0)),
                'weather': wmo_code_desc(code)
            }
            self.weather_done.emit(data)
        except Exception:
            self.weather_done.emit(None)

    def _news_thread(self):
        all_items = []

        # 1. 中文 RSS 批量拉取
        for url in RSS_SOURCES:
            try:
                r = requests.get(url, timeout=6, headers={'User-Agent': 'Mozilla/5.0'})
                r.raise_for_status()
                r.encoding = 'utf-8'
                root = ET.fromstring(r.text)
                for item in root.iter('item'):
                    title = item.find('title').text or ''
                    desc  = item.find('description').text or ''
                    link  = unwrap_sina_link(item.find('link').text or '')
                    all_items.append((title.strip(), desc.strip(), link))
            except Exception:
                continue
        self.news_done.emit(all_items)

    def get_detail(self, url: str):
        self.pool.submit(self._detail_thread, url)

    def _detail_thread(self, url: str):
        try:
            r = requests.get(url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            })
            r.raise_for_status()
            r.encoding = 'utf-8'

            doc = Document(r.text)
            html = doc.summary()
            self.detail_done.emit(html)
        except Exception as e:
            self.detail_done.emit(f'<p>正文提取失败：{e}</p>')
    
# --------------- 主窗口 ---------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('天气+新闻 精简版')
        self.resize(500, 400)

        central = QWidget()
        self.setCentralWidget(central)
        lay = QVBoxLayout(central)
        # ---- 天气区 ----
        lay.addWidget(QLabel('<b>当日天气</b>'))
        self.city_edit = QLineEdit('北京')
        self.query_btn = QPushButton('查询天气')
        self.query_btn.clicked.connect(self.query_weather)
        h = QHBoxLayout()
        h.addWidget(self.city_edit)
        h.addWidget(self.query_btn)
        lay.addLayout(h)

        self.weather_label = QLabel('温度：--　风力：--')
        lay.addWidget(self.weather_label)
        # ---- 新闻区 ----
        self._current_title = ''
        self._current_link = ''
        lay.addWidget(QLabel('<b>新闻列表</b>'))
        h_btn = QHBoxLayout()
        self.refresh_btn = QPushButton('刷新全部')
        self.refresh_btn.clicked.connect(lambda: self.load_page(0))
        h_btn.addWidget(self.refresh_btn)
        h_btn.addStretch()
        lay.addLayout(h_btn)
        # 左右分栏
        hsplit = QHBoxLayout()
        self.news_list = QListWidget()
        self.news_list.setFixedWidth(220)
        self.news_list.itemClicked.connect(self.load_detail_of_item)
        hsplit.addWidget(self.news_list)

        self.news_detail = QTextEdit()
        self.news_detail.setReadOnly(True)
        # 允许加载远程图片
        self.news_detail.setHtml('<p>Loading...</p>')
        hsplit.addWidget(self.news_detail)
        lay.addLayout(hsplit)

        # 分页控件
        page_lay = QHBoxLayout()
        self.prev_btn = QPushButton('上一页')
        self.prev_btn.clicked.connect(lambda: self.load_page(self._page - 1))
        self.page_label = QLabel('第 1 页')
        self.next_btn = QPushButton('下一页')
        self.next_btn.clicked.connect(lambda: self.load_page(self._page + 1))
        page_lay.addWidget(self.prev_btn)
        page_lay.addWidget(self.page_label)
        page_lay.addWidget(self.next_btn)
        page_lay.addStretch()
        lay.addLayout(page_lay)

        # 分页数据
        self._all_items = []   # 全部新闻
        self._page = 0         # 当前页索引
        self._page_size = 5    # 每页条数

        # ---- 线程 ----
        self.thread = QThread()
        self.worker = NetWorker()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        self.worker.weather_done.connect(self.on_weather)
        self.worker.news_done.connect(self.on_news)
        self.worker.detail_done.connect(self.on_detail)

         # ---- 新增：默认定位 ----
        default_city = get_city_by_ip()
        self.city_edit.setText(default_city)
        # 启动即查一次
        self.query_weather()
        # 启动即加载第 1 页
        self.load_page(0)

    # ---------- 天气 ----------
    def query_weather(self):
        city = self.city_edit.text().strip()
        if not city:
            QMessageBox.warning(self, '提示', '请先输入城市')
            return
        self.query_btn.setEnabled(False)
        self.weather_label.setText('查询中…')
        self.worker.get_weather(city)

    def on_weather(self, data: dict):
        self.query_btn.setEnabled(True)
        if data:
            self.weather_label.setText(
                f"城市：{data['city']}　"
                f"温度：{data['temp']}℃　"
                f"天气：{data['weather']}　"
                f"风向：{data['wind_dir']}　"
                f"风速：{data['wind']}　"
            )
        else:
            QMessageBox.critical(self, '失败', '获取天气失败，请检查城市名或网络')

    # ---------- 新闻 ----------
    def on_list_click(self, item: QListWidgetItem):
        row = self.news_list.row(item)
        title, desc, link = self._news_items[row]
        self._current_link = link
        self.news_detail.setHtml(f'<h3>{title}</h3><p>{desc}</p>')

    def load_all_news(self):
        """拉取全部新闻并填充左侧列表"""
        self.refresh_btn.setEnabled(False)
        self.news_list.clear()
        self.news_detail.clear()
        self.worker.get_news()

    def on_news(self, items: list):
        self.refresh_btn.setEnabled(True)
        if not items:
            QMessageBox.critical(self, '失败', '获取新闻失败')
            self._all_items = []
            return
        self._all_items = items
        self.load_page(0)          # 加载第 1 页

    def load_page(self, page):
        """加载第 page 页（0 起始）"""
        if not self._all_items:          # 首次拉取
            self.refresh_btn.setEnabled(False)
            self.worker.get_news()
            return
        max_page = len(self._all_items) // self._page_size
        page = max(0, min(page, max_page))
        self._page = page

        start, end = page * self._page_size, (page + 1) * self._page_size
        self.news_list.clear()
        for idx in range(start, min(end, len(self._all_items))):
            title, _, _ = self._all_items[idx]
            seq = idx + 1
            item = QListWidgetItem(f'{seq}.  {title}')
            item.setSizeHint(QSize(200, 28))   # 行高 28
            self.news_list.addItem(item)

        self.page_label.setText(f'第 {page + 1} 页')
        self.prev_btn.setEnabled(page > 0)
        self.next_btn.setEnabled(end < len(self._all_items))
        # 自动选中第一条并加载详情
        if self.news_list.count():
            self.news_list.setCurrentRow(0)
            self.load_detail_of_item(self.news_list.currentItem())

    def load_detail_of_item(self, item: QListWidgetItem):
        row = self.news_list.row(item) + self._page * self._page_size
        title, desc, link = self._all_items[row]
        self._current_title = title
        self._current_link = link
        # 1. 右侧先清空，提示加载中
        self.news_detail.clear()
        self.news_detail.setHtml(f'<h3>{title}</h3><p>正在加载正文…</p>')
        # 2. 立即后台抓正文
        self.worker.get_detail(link)

    def on_detail(self, html: str):
        soup = BeautifulSoup(html, 'lxml')
        # 0. 段首空格：样式保留空格 + 两个实体
        for p in soup.find_all('p'):
            # 先清空段首可能的空白，避免重复
            text = p.get_text(strip=False)
            if text and not text.startswith('\u00A0'):
                # 样式：保留空白，首行缩进 2 全角
                p['style'] = 'white-space:pre; text-indent:2em; margin:0;'
                # 最前面插两个“非断行空格”实体
                p.insert(0, NavigableString('\u00A0\u00A0'))

        html = str(soup)
        # 1. 先显示文字（图片还是原始 src）
        self._raw_html = html                  # 保留一份，用于后续局部替换
        self.news_detail.clear()
        self.news_detail.setHtml(
            f'<h1 style="text-align:center;">{self._current_title}</h1>'
            f'{html}'
        )
        # 2. 启动异步转码
        self.img_converter = ImgBase64Converter(self)
        # 连自己的信号
        self.img_converter.img_converted.connect(self._replace_img_src)
        # 把 *自己的信号* 传进去当回调
        self.img_converter.convert_async(html, self.img_converter.img_converted)

    def _replace_img_src(self, old_src: str, data_uri: str):
        """单张图下载完，直接在 QTextDocument 里把 src 换掉"""
        if not data_uri:                       # 下载失败直接忽略
            return
        # 1. 把当前 HTML 重新解析
        soup = BeautifulSoup(self.news_detail.toHtml(), 'lxml')
        # 2. 找到这张图片
        img = soup.find('img', {'src': old_src})
        if not img:                            # 已经换过了/被删了
            return
        # 3. 改 src + 统一居中样式
        img['src'] = data_uri
        img['style'] = 'display:block; margin:8px auto; max-width:100%; height:auto;'
        # 4. 外包一层居中 <p>
        p = soup.new_tag('p', style='text-align:center; margin:8px 0;')
        img.wrap(p)
        # 5. 写回 QTextEdit（保留滚动条）
        bar = self.news_detail.verticalScrollBar()
        pos = bar.value()
        self.news_detail.setHtml(str(soup))
        bar.setValue(pos)

    # ---------- 退出 ----------
    def closeEvent(self, a0):
        self.thread.quit()
        self.thread.wait()
        if hasattr(self, 'img_converter'):
            self.img_converter.pool.shutdown(wait=False)
        super().closeEvent(a0)

# --------------- 入口 ---------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())