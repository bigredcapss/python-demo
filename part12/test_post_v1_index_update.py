# -*- coding: UTF-8 -*-

# filename : test_post_v1_index_update.py
# description : 读取存量帖子信息更新ES中的帖子数据
# author by : peanut
# date : 2025/4/29


import pymysql
from elasticsearch import Elasticsearch,RequestsHttpConnection
from elasticsearch.exceptions import NotFoundError

# db连接信息
db_info = {
    "host": "mysql.c.t.soulapp-inc.cn",
    "port": 3306,
    "user": "root",
    "password": "Soul-Ops-Team", 
    "database": "post-ext-service",
    "charset": "utf8"
}


# ES连接信息
es_info = {
    "host": "xx",
    "port": 80,
    "token": "xx"
}

# 创建ES客户端
es = Elasticsearch(
    [f"http://{es_info['host']}:{es_info['port']}"],
    http_auth=('Bearer', es_info['token']),
    connection_class=RequestsHttpConnection
)


cur = None
db = None
post_location_tables = []
post_info_tables = []

# 读取帖子位置信息
def read_db_table_post_location(post_id):
    global cur
    global db
    global post_location_tables
    try:
        print("db_info:", db_info)
        # 连接到数据库
        db = pymysql.connect(
            host=db_info["host"],
            port=db_info["port"],
            user=db_info["user"],
            password=db_info["password"],
            database=db_info["database"],
            charset=db_info["charset"]
        )
        cur = db.cursor()

        # 获取符合条件的表
        show_tables = "show tables;"
        cur.execute(show_tables)
        tables = cur.fetchall()
        for table in tables:
            if table[0].startswith("post_location_info_"):
                post_location_tables.append(table[0])

        if not post_location_tables:
            print("没有符合条件的表")
            return

        # 查询符合条件的表
        for post_location_table in post_location_tables:
            sql = "select post_id, position from " + post_location_table + " where post_id = " + post_id
            cur.execute(sql)
            # 获取所有结果
            results = cur.fetchall()
            # 遍历结果
            if results:
                row = results[0]
                return row.get("position")
            else:
                continue
        return None
    
    except Exception as e:
        print(e)

    finally:
        # 关闭游标和数据库连接
        if cur:
            cur.close()
        if db:
            db.close()

# 读取帖子信息
def read_db_table_post_info():
    global cur
    global db
    global post_info_tables
    try:
        print("db_info:", db_info)
        # 连接到数据库
        db = pymysql.connect(
            host=db_info["host"],
            port=db_info["port"],
            user=db_info["user"],
            password=db_info["password"],
            database=db_info["database"],
            charset=db_info["charset"]
        )
        cur = db.cursor()

        # 获取符合条件的表
        show_tables = "show tables;"
        cur.execute(show_tables)
        tables = cur.fetchall()
        for table in tables:
            if table[0].startswith("post_"):
                post_info_tables.append(table[0])

        if not post_info_tables:
            print("没有符合条件的表")
            return

        # 查询符合条件的表
        for post_info_table in post_info_tables:
            sql = "select id, position from " + post_info_table + " where id > 281820 and id < 285675" 
            cur.execute(sql)
            # 获取所有结果
            results = cur.fetchall()
            # 遍历结果
            if results:
                for row in results:
                    post_id = row[0]
                    position = row[1]
                    doc = get_document_by_id("post_v1", post_id)
                    if doc:
                        if "position" not in doc:
                            new_doc = dict(doc)
                            new_doc["position"] = position
                            insert_document("post_v1", row[0], new_doc)
                            print(f"帖子 {row[0]} 插入成功")
                        else:
                            print(f"帖子 {row[0]} 位置属性在ES中已存在")
                    else:
                        print(f"帖子 {row[0]} 在ES中不存在")
                else:
                    continue
            else:
                continue
        return None
    
    except Exception as e:
        print(e)

    finally:
        # 关闭游标和数据库连接
        if cur:
            cur.close()
        if db:
            db.close()

# 更新数据
def update_document(index_name, doc_id, update_data):
    try:
        response = es.update(index=index_name, doc_type='_doc', id=doc_id, body=update_data)
        print(f"文档 {doc_id} 更新成功: {response}")
    except Exception as e:
        print(f"更新文档时发生错误: {e}")

# 插入数据
def insert_document(index_name, doc_id, insert_data):
    try:
        response = es.index(index=index_name, doc_type='_doc', id=doc_id, body=insert_data)
        print(f"文档 {doc_id} 插入成功: {response}")
    except Exception as e:
        print(f"插入文档时发生错误: {e}")

# 按id查询数据
def get_document_by_id(index_name,  doc_id):
    try:
        response = es.get(index=index_name, doc_type='_doc', id=doc_id)
        print(f"文档 {doc_id} 查询成功: {response['_source']}")
        return response['_source']
    except NotFoundError as e:
        print(f"文档 {doc_id} 未找到: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# 按创建时间查询数据
def get_document_by_create_time(index_name, start_time, end_time, size):
    try:
        # 查询条件
        query = {
            "query": {
                "range": {
                    "create_time": {
                        "gte": start_time,
                        "lte": end_time
                    }
                }
            },
            "sort": [
                {
                    "id": {
                        "order": "desc"
                    }
                }
            ],
            "size": size
        }

        # 执行查询
        response = es.search(
            index=index_name,  
            body=query,
            scroll='2m')
        
        print(f"查询语句: {query}")

        # 获取第一批结果
        scroll_id = response['_scroll_id']
        hits = response['hits']['hits']
        total_hits = response['hits']['total']

        # 获取总文档数
        if isinstance(total_hits, dict):
            total_count = total_hits['value']
        else:
            total_count = total_hits

        print(f"总文档数: {total_count}")
        print(f"查询条件: 开始时间={start_time}, 结束时间={end_time}")

        # 处理第一批结果
        process_results(hits)
        
        # 继续获取剩余结果
        while len(hits) > 0:
            response = es.scroll(scroll_id=scroll_id, scroll='2m')
            scroll_id = response['_scroll_id']
            hits = response['hits']['hits']
            
            if not hits:
                break
                
            print(f"获取下一批结果: {len(hits)}个文档")
            process_results(hits)
            
        # 清理scroll上下文
        es.clear_scroll(scroll_id=scroll_id)
        return total_count
    except NotFoundError as e:
        print(f"未找到符合条件的文档: {e}")
        return 0  # 添加返回值
    except Exception as e:
        print(f"发生错误: {e}")
        return 0  # 添加返回值 

# 处理批量结果的函数
def process_results(hits):
    for hit in hits:
        doc = hit['_source']
        doc_id = hit['_id']
        # 打印每条记录
        print(f"处理文档 ID: {doc_id}, 创建时间: {doc.get('create_time')}, 可见性: {doc.get('visibility')}, "
              f"状态: {doc.get('state')}, 作者id: {doc.get('author_id')}, 类型: {doc.get('type')}, "
              f"帖子内容: {doc.get('content')}")
        # 将每条记录转为字典
        doc_dict = dict(doc)
        # 查询帖子位置信息
        position = read_db_table_post_location(doc_id)
        print(f"帖子 {doc_id} 位置信息: {position}")
        if position:
            doc_dict["position"] = position
            # 更新数据
            update_document("post_v1", doc_id, doc_dict)



if __name__ == '__main__':
    read_db_table_post_info()
