import json
from pprint import pprint
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

class Search:
    def __init__(self):
        # Connect to Elasticsearch
        self.es = Elasticsearch("http://localhost:9200")
        client_info = self.es.info()
        print('Connected to Elasticsearch!')
        pprint(client_info.body)

        # Only create index if it doesn't exist
        if not self.es.indices.exists(index='my_documents'):
            self.es.indices.create(index='my_documents')

    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({'index': {'_index': 'my_documents'}})
            operations.append(document)
        return self.es.bulk(operations=operations)

    def search(self, **query_args):
        return self.es.search(index='my_documents', **query_args)

    def reindex(self):
        # Safely delete and recreate the index
        self.es.indices.delete(index='my_documents', ignore_unavailable=True)
        self.es.indices.create(index='my_documents')

        with open('data.json', 'rt') as f:
            documents = json.loads(f.read())

        return self.insert_documents(documents)
    
    def retrieve_document(self, id):
        return self.es.get(index='my_documents', id=id)