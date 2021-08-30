import elasticsearch


def get_instance():
    return elasticsearch.Elasticsearch(
        hosts=['localhost'],
        http_auth=None,
        scheme='http',
        port=9200
    )
