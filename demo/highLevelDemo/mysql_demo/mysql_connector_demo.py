#!/usr/bin/python3

import mysql.connector

# 连接数据库主机地址
def connect():
    return mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="sa"   # 数据库密码
    )
    
# 创建数据库
def create_db(dbname):
    db = connect()
    cur = db.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{dbname}`")
    db.commit()
    cur.close()
    db.close()
    print(f"数据库 {dbname} 创建成功")

# 输出所有数据库列表：
def show_databases():
    db = connect()
    cur = db.cursor()
    cur.execute("SHOW DATABASES")
    rows = cur.fetchall()   # 一次性取出
    cur.close()
    db.close()
    return rows             # 返回列表，而不是游标


# 直接连接数据库，如果数据库不存在，会输出错误信息
from mysql.connector import Error

def get_connection(dbname, **kw):
    """
    尝试连接指定数据库。
    库不存在 -> 打印提示并返回 None
    其他异常 -> 抛出
    返回：连接对象 或 None
    """
    try:
        return mysql.connector.connect(
            host=kw.get('host', 'localhost'),
            user=kw.get('user', 'root'),
            passwd=kw.get('passwd', 'sa'),
            port=kw.get('port', 3306),
            database=dbname,
            charset='utf8', # 写utf8mb4 mysql8.0才不会报错
            # 结果集需要回读；最稳妥：连接或游标加 buffered=True，永绝后患！
            buffered=True          # 一次性拉取全部结果,不加这行直接 fetchone() 会由于数据未取完，直接cur.close()导致报错.
        )
    except Error as e:
        if e.errno == 1049:          # Unknown database
            print(f'库 "{dbname}" 不存在')
            return None
        raise                         # 其余异常继续抛出

# 看警告条数，判断
def get_warning_count(cur):
    cur.execute("SHOW WARNINGS")
    warns = cur.fetchall()      # 先取空结果集
    print(warns)
    return len(warns)# 警告条数    

def create_table(dbname, sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql)               # 含 IF NOT EXISTS
        conn.commit()
        # 看警告数
        warn_cnt = get_warning_count(cur)
        if warn_cnt:
            print('表已存在，未重复创建')
            return True
        else:
            print('表创建成功')
            return True
    except Exception as e:
        print('创建失败：', e)
        return False
    finally:
        cur.close(); conn.close()

def show_tables(dbname):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return None
    try:
        cur = conn.cursor(buffered=True) # 结果集需要回读；最稳妥：连接或游标加 buffered=True，永绝后患！
        cur.execute("SHOW TABLES")
        conn.commit()
        rows = cur.fetchall()   # 一次性取出
        return rows             # 返回列表，而不是游标
    except Exception as e:
        print('查询失败：', e)
        return None
    finally:
        cur.close(); conn.close()

def alter_table(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql)             
        warn_cnt = get_warning_count(cur)
        if warn_cnt == 0:
            print('创建成功')
        conn.commit()
    except Exception as e:
        print('表修改失败：', e)
        return False
    finally:
        cur.close(); conn.close()
    return True


def drop_table(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql)             
        warn_cnt = get_warning_count(cur)
        if warn_cnt == 0:
            print('操作成功')
        conn.commit()
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()
    return True

# 插入单条
def insert_one(dbname,sql,val):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql,val)             
        conn.commit()
        # 看影响行数
        if cur.rowcount > 0:
            print(f'插入成功，影响 {cur.rowcount} 行')
            return cur.lastrowid
        else:
            print('插入 0 行，视为失败')
            return False          # 按业务返回失败
        '''
| 场景                                         | 异常？                | rowcount | 说明       |
| ------------------------------------------   | ------------------ | -------- | -------- |
| 正常插入成功                                  | ❌                  | 1        | 最常见      |
| 唯一键冲突，无忽略/无更新                      | ✅ 抛 IntegrityError | ——       | 走 except |
| `INSERT IGNORE ...` 冲突跳过                  | ❌                  | 0        | 不抛，0 行   |
| `INSERT ... ON DUPLICATE KEY UPDATE id=id`   | ❌                  | 0        | 不抛，0 行   |

        '''
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()

# 批量插入
def batch_insert(dbname,sql,val):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.executemany(sql,val)             
        conn.commit()
        # 看影响行数
        if cur.rowcount > 0:
            print(f'插入成功，影响 {cur.rowcount} 行')
            return True
        else:
            print('插入 0 行，视为失败')
            return False          # 按业务返回失败
        '''
| 场景                                         | 异常？                | rowcount | 说明       |
| ------------------------------------------   | ------------------ | -------- | -------- |
| 正常插入成功                                  | ❌                  | 1        | 最常见      |
| 唯一键冲突，无忽略/无更新                      | ✅ 抛 IntegrityError | ——       | 走 except |
| `INSERT IGNORE ...` 冲突跳过                  | ❌                  | 0        | 不抛，0 行   |
| `INSERT ... ON DUPLICATE KEY UPDATE id=id`   | ❌                  | 0        | 不抛，0 行   |

        '''
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()

def select_all(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print('查询失败：', e)
        return None
    finally:
        cur.close(); conn.close()

def select_one(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return None
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row
    except Exception as e:
        print('查询失败：', e)
        return None
    finally:
        cur.close(); conn.close()

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件
def get_one(dbname,sql,val):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return None
    try:
        cur = conn.cursor()
        cur.execute(sql,val)
        row = cur.fetchone()
        return row
    except Exception as e:
        print('查询失败：', e)
        return None
    finally:
        cur.close(); conn.close()

# 删除操作
def delete(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # 看影响行数
        if cur.rowcount > 0:
            print(f'删除成功，影响 {cur.rowcount} 行')
            return True
        else:
            print('删除 0 行，视为失败')
            return False          # 按业务返回失败
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()


# 更新操作
def update(dbname,sql):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # 看影响行数
        if cur.rowcount > 0:
            print(f'更新成功，影响 {cur.rowcount} 行')
            return True
        else:
            print('更新 0 行，视为失败')
            return False          # 按业务返回失败
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()

def update2(dbname,sql,val):
    conn = get_connection(dbname)
    if not conn:
        print('未建立连接，请检查库名')
        return False
    try:
        cur = conn.cursor()
        cur.execute(sql,val)
        conn.commit()
        # 看影响行数
        if cur.rowcount > 0:
            print(f'更新成功，影响 {cur.rowcount} 行')
            return True
        else:
            print('更新 0 行，视为失败')
            return False          # 按业务返回失败
    except Exception as e:
        print('操作失败：', e)
        return False
    finally:
        cur.close(); conn.close()

if __name__ == '__main__':
    # print(connect())
    # create_db('python_test_db')
    # res = show_databases()
    # for x in res:
    #     print(x)
    # conn = get_connection('python_test_db1')
    # if conn:
    #     print('连接成功：', conn)
    #     conn.close()
    # else:
    #     print('未建立连接，请检查库名')
    # create_table('python_test_db',"CREATE TABLE IF NOT EXISTS sites2 (name VARCHAR(255), url VARCHAR(255))")
    res = show_tables('python_test_db')
    for x in res:
        print(x)
    # res = alter_table('python_test_db',"ALTER TABLE sites2 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    # print(res)
    # res = drop_table('python_test_db',"DROP TABLE IF EXISTS sites")
    # print(res)
    # insertId = insert_one('python_test_db',"INSERT INTO sites(name, url) VALUES (%s, %s)",("菜鸟教程", "https://www.runoob.com"))
    # print(insertId) # 8
    # batch_insert('python_test_db',
    #             "INSERT INTO sites(name, url) VALUES (%s, %s)",
    #             [('Google', 'https://www.google.com'),
    #             ('Github', 'https://www.github.com'),
    #             ('Taobao', 'https://www.taobao.com')]) # 批量插入时，charset='utf8' 必须写utf8,而单条插入可以写utf8mb4, # 写utf8mb4 mysql8.0才不会报错
    # res = select_all('python_test_db',"SELECT * FROM sites")
    # res = select_all('python_test_db',"SELECT name, url FROM sites")
    # for x in res:
    #     print(x)
    # res = select_one('python_test_db',"SELECT name, url FROM sites") # buffered=True 一次性拉取全部结果,不加这行直接 fetchone() 会由于数据未取完，直接cur.close()导致报错
    # res = select_one('python_test_db',"SELECT name, url FROM sites limit 1") 
    # res = select_one('python_test_db',"SELECT name, url FROM sites WHERE name = 'Google' limit 1") 
    # print(res)
    # res = get_one('python_test_db',"SELECT * FROM sites WHERE name = %s limit 1",('Google',)) 
    # print(res) # True
    # res = delete('python_test_db',"DELETE FROM sites WHERE name = 'Github'")
    # res = delete2('python_test_db',"DELETE FROM sites WHERE name = %s",('Google',))
    # print(res) # True
    # res = update('python_test_db',"UPDATE sites SET name = 'TM' WHERE name = 'Taobao'")
    # res = update2('python_test_db',"UPDATE sites SET name = %s WHERE name = %s",('Taobao','TM'))
    # print(res) # True