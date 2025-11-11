#!/usr/bin/python3

from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import os

prompt = '一副典雅庄重的对联悬挂于厅堂之中，房间是个安静古典的中式布置，桌子上放着一些青花瓷，对联上左书"书山有路勤为径"，右书"觉知此事要躬行"， 横批"学富五车"，字体飘逸，中间挂在一着一副中国风的画作，内容是龙腾虎跃。'

# 请用百炼API Key
api_key = "sk-d959283bd88e4cfcb407694ea822490e"

print('----同步调用，请等待任务执行----')
rsp = ImageSynthesis.call(api_key=api_key,
                          model="qwen-image",
                          prompt=prompt,
                          n=1,
                          size='1328*1328',
                          prompt_extend=True,
                          watermark=True)
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    # 在当前目录下保存图片
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        with open('./demo/highLevelDemo/ai_image_demo/%s' % file_name, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('同步调用失败, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))
    
'''
输出：
----同步调用，请等待任务执行----
response: {"status_code": 200, "request_id": "2dc37e0c-fca0-44b4-8d2c-6bc1a13600b9", "code": null, "message": "", "output": {"task_id": "a989a26c-e27c-4b9d-b39a-a4c92d3cb977", "task_status": "SUCCEEDED", "results": [{"url": "https://dashscope-result-wlcb-acdr-1.oss-cn-wulanchabu-acdr-1.aliyuncs.com/7d/8b/20251030/d81d59b0/a989a26c-e27c-4b9d-b39a-a4c92d3cb977-1.png?Expires=1762416284&OSSAccessKeyId=LTAI5tKPD3TMqf2Lna1fASuh&Signature=bx5ITZb%2FoSl6IBQxTIn%2FyRXjiVA%3D", "orig_prompt": "一副典雅庄重的对联悬挂于厅堂之中，房间是个安静古典的中式布置，桌子上放着一些青花瓷，对联上左书\"书山有路勤为径\"，右书\"觉 知此事要躬行\"， 横批\"学富五车\"，字体飘逸，中间挂在一着一副中国风的画作，内容是龙腾虎跃。", "actual_prompt": "一副典雅庄重的对联悬挂于厅堂正中，房间为 安静古典的中式布局，整体氛围沉静而富有文人气息。墙壁以深褐色木质雕花板装饰，地面铺着素雅的青砖，角落摆放一盏铜制博山炉，袅袅轻烟缓缓升腾。一张红木雕花茶 桌置于中央，其上陈列着几件精致的青花瓷器：一只敞口梅瓶，瓶身绘有缠枝莲纹；一对玉壶春瓶，釉色温润如玉，纹饰细腻流畅；还有一只小茶杯，杯底隐约可见“景德年制”四字款识。对联左右对称悬挂于门框两侧，左联书写“书山有路勤为径”，右联书写“觉知此事要躬行”，字体为行楷，笔势飘逸流畅，墨色浓淡相宜，透出深厚的文化底蕴。横批“学富五车”居于上方正中，字体端庄大气，与上下联呼应，彰显学识之渊博。对联中间悬挂一幅中国风画作，画面描绘龙腾虎跃之景：一条苍龙自云海中腾起，鳞片熠熠生 辉，双目炯炯有神，龙爪凌空抓握祥云；下方猛虎伏地蓄势，肌肉紧绷，鬃毛飞扬，眼神锐利如炬，二者动态交错，气势磅礴。整幅画作采用中国传统工笔重彩技法，设色典 雅，构图饱满，背景为淡青色云雾缭绕的天际，衬托出天地之间的雄浑气韵。画面整体风格为古典中式写实绘画，光影柔和，细节丰富，体现出浓厚的东方美学意境。"}], "submit_time": "2025-10-30 15:47:53.977", "scheduled_time": "2025-10-30 15:47:54.033", "end_time": "2025-10-30 15:48:05.222"}, "usage": {"image_count": 1}}
'''