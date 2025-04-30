# -*- coding: UTF-8 -*-

# filename : test_elasticsearch.py
# description : 操作es索引更新数据
# author by : peanut
# date : 2025/4/29

from elasticsearch import Elasticsearch,RequestsHttpConnection
from elasticsearch.exceptions import NotFoundError
import json

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


# 更新数据
def update_document(index_name, doc_id, update_data):
    try:
        response = es.update(index=index_name, doc_type='_doc', id=doc_id, body=update_data)
        print(f"文档 {doc_id} 更新成功: {response}")
    except Exception as e:
        print(f"更新文档时发生错误: {e}")


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



if __name__ == '__main__':
    index_name = "post_v1"
    start_time = 1735660800000  # 2025-01-01 00:00:00
    end_time = 1745769600000    # 2025-04-28 00:00:00
    size = 100
    get_document_by_create_time(index_name, start_time, end_time, size)
