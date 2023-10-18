"""
Python module to perform different operation with VectorDB.
    
"""
# importing necessary dependecies
from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)


FMT = "\n=== {:30} ===\n"
SEARCH_LATENCY_FMT = "search latency = {:.4f}s"
NUM_ENTITIES, DIM = 3000, 8


class VectorDB:
    """Class to perform different operationd for VectorDB(Milvus).
    """
    def __init__(
        self, alias='default',
        user='username',
        password='password',
        host='localhost',
        port=19530,
        collection_name='my_collection',
        dimension=128
    ):
        self.user = user
        self.password = password
        self.alias =alias
        self.host = host
        self.port = port
        self.collection_name = collection_name
        self.dimension = dimension
    
    # function to connect with vectorDB
    def connect(self):
        connections.connect(
            alias=self.alias,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
            )
    
    # function to create collection
    def create_collection(self):
        if utility.has_collection(self.collection_name):
            return "Collection already exists."
        else:
            fields = [
                FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
                FieldSchema(name="random",dtype=DataType.DOUBLE),
                FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=DIM)
            ]
            schema = CollectionSchema(fields)
            Collection(self.collection_name, schema, consistency_level="Strong")
        
    # function to create index
    def create_index(self, index_type='IVF_FLAT'):
        if not utility.has_collection(self.collection_name):
            return "Collection doesn't exist. Create the collection first."

        collection = Collection(name=self.collection_name)
        collection.create_index(field_name='vector', index_type=index_type)

    # function to store data
    def store_data(self, data):
        collection = Collection(name=self.collection_name)
        collection.insert(data)

    # function to perform semantic similarity search
    def semantic_similarity_search(self, query_vector, top_k=5):
        collection = Collection(name=self.collection_name)
        results = collection.search(query_records=[query_vector], top_k=top_k)
        return results[0]

    # function to  update data
    def update_data(self, id, new_vector):
        collection = Collection(name=self.collection_name)
        collection.update(ids=[id], records=[new_vector])

    # function to delete data
    def delete_data(self, id):
        collection = Collection(name=self.collection_name)
        collection.delete(ids=[id])

    # function to disconnect vectorDB
    def disconnect(self):
        connections.disconnect()

if __name__ == '__main__':
    vector_db = VectorDB()
    vector_db.connect()
    vector_db.create_collection()
    
    # Example data
    data = [{"pk": 1, "random":20, "embeddings": [0.1, 0.2, 0.3]},
            {"pk": 2, "random":30, "embeddings": [0.4, 0.5, 0.6]}]

    vector_db.store_data(data)
    
    query_vector = [0.2, 0.3, 0.4]
    search_results = vector_db.semantic_similarity_search(query_vector)
    print("Search Results:", search_results)
    
    # Update data
    updated_vector = [0.3, 0.4, 0.5]
    vector_db.update_data(1, updated_vector)
    
    # Delete data
    vector_db.delete_data(2)
    
    vector_db.disconnect()
