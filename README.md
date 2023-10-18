# SPRINT 5: VECTOR DATABASES

# What is Vector Databases?

A vector database, also known as a vectorized database or vector storage, is a type of database system that is designed to efficiently store, manage, and query high-dimensional vector data. In a vector database, data points are represented as vectors, which are mathematical objects that consist of a set of values (coordinates) in a multi-dimensional space. These vectors can represent various types of data, such as images, text documents, sensor readings, or any other structured data.

Vector databases have gained popularity in various applications, particularly those involving machine learning, artificial intelligence, and data analysis.

# Role of Vector Database

![e88ebbacb848b09e477d11eedf4209d10ea4ac0a-1399x537.png](SPRINT%205%20VECTOR%20DATABASES%200e1dece55d294ddd8c426cb19c8d8ab3/e88ebbacb848b09e477d11eedf4209d10ea4ac0a-1399x537.png)

The role of a vector database in the context of embedding models and content indexing involves several key steps:

1. **Generating Vector Embeddings**: The first step is to use an embedding model, which could be a large language model or another machine learning model, to create vector embeddings for the content that you want to index. These vector embeddings represent the content in a numerical format, capturing its semantic information and essential features.
2. **Storing Vector Embeddings**: The generated vector embeddings are then inserted into the vector database. Each vector embedding is associated with some reference to the original content from which it was created. This association ensures that the database can link the embeddings back to their source content.
3. **Querying for Similarities**: When the application issues a query, the same embedding model is employed to generate embeddings for the query input. These query embeddings represent the intent or content of the query.
4. **Searching for Similar Embeddings**: The vector database is queried using the query embeddings to find similar vector embeddings that match the query. The database uses specialized indexing and search algorithms to efficiently retrieve embeddings that are most similar to the query embeddings.
5. **Returning Relevant Results**: The similar embeddings retrieved from the database are associated with the original content items they were created from. Therefore, the database returns references to the original content that matches the query, allowing the application to provide relevant results to the user.

# Difference between Vector Indices and Vector Database

1. **Vector Index**:
    - **Purpose**: A vector index is a data structure or component used to efficiently retrieve similar vectors from a dataset based on a query vector. Its primary purpose is to accelerate the process of searching for nearest neighbors or similar vectors.
    - **Functionality**: A vector index focuses on the indexing and search operations. It is responsible for organizing and structuring the vector data in such a way that it can quickly identify and retrieve vectors that are close in similarity to a given query vector.
    - **Standalone Component**: A vector index is often used as part of a larger system or application, such as a search engine or recommendation system. It is designed to optimize similarity search within a dataset but may not handle the entire database management.
2. **Vector Database**:
    - **Purpose**: A vector database is a comprehensive database management system specifically designed for storing, managing, and querying high-dimensional vector data, such as vector embeddings or feature vectors.
    - **Functionality**: A vector database provides a complete set of database functionalities, including data storage, indexing, query processing, and retrieval. It is capable of handling the entire lifecycle of vector data, from storage to retrieval.
    - **Integrated Solution**: Unlike a standalone vector index, a vector database is a self-contained solution for managing vector data. It often includes features like data persistence, scaling capabilities, and sometimes even integrated machine learning models for generating embeddings.
    - **Use Cases**: Vector databases are suitable for applications that rely heavily on vector data, such as recommendation systems, content-based search, and AI-driven applications that require real-time retrieval of similar items.
    
    # Working Pipeline of Vector Database
    
    ![ff9ba425d0c78d696372e0a43ce57851b4f1d4b7-1307x233.png](SPRINT%205%20VECTOR%20DATABASES%200e1dece55d294ddd8c426cb19c8d8ab3/ff9ba425d0c78d696372e0a43ce57851b4f1d4b7-1307x233.png)
    
    - **Indexing**: The vector database indexes vectors using an algorithm such as PQ, LSH, or HNSW (more on these below). This step maps the vectors to a data structure that will enable faster searching.
    - **Querying**: The vector database compares the indexed query vector to the indexed vectors in the dataset to find the nearest neighbors (applying a similarity metric used by that index)
    - **Post Processing**: In some cases, the vector database retrieves the final nearest neighbors from the dataset and post-processes them to return the final results. This step can include re-ranking the nearest neighbors using a different similarity measure.
    
    # 1. Pinecone:
    
    - **Use Case**: Pinecone is a real-time vector database that specializes in similarity search and retrieval. It is well-suited for applications like recommendation systems, content-based search, and personalization.
    - **Key Features**:
        - Real-time capabilities for immediate results.
        - Support for embedding models and similarity search.
        - Scalability for handling large datasets and high query loads.
        - Integration with machine learning frameworks and APIs.
    - **Managed Service**: Pinecone offers a fully managed cloud-based solution for vector database needs.
    - ***Source Code Availability*:** Closed-source.
    - ***Hosting Methods***: Fully cloud-native, no self-hosting option.
    - ***Indexing Methods*:** Not specified in the information.
    - ***Pros*:** Easy to set up, cloud-native, and does not require users to understand vectorization or vector indexes.
    - ***Cons*:** Proprietary, lacks transparency in terms of its technology and roadmap, limited control for developers, potentially higher long-term costs.
    
    # 2. FAISS
    
    - **Use Case**: Faiss (Facebook AI Similarity Search) is an open-source library for similarity search and clustering of large datasets. It is designed for offline and batch processing.
    - **Key Features**:
        - Efficient and highly optimized for similarity search.
        - Customizable indexing methods (e.g., LSH, IVF).
        - Support for GPU acceleration.
        - Suitable for research and custom deployments.
    - **Open Source**: Faiss is an open-source project, which provides flexibility for customization and integration.
    - ***Source Code Availability*:** Open source.
    - ***Hosting Methods*:** Supports cloud-native and managed offerings.
    - ***Indexing Methods*:** Utilizes its own versions of DiskANN.
    - ***Pros*:** Mature with a wide range of algorithms, scalable, and efficient on-disk indexing. Offers a variety of vector indexing options.
    - ***Cons*:** Complex architecture, less intuitive client APIs compared to some newer databases.
    
    # 3. Milvus
    
    - **Use Case**: Milvus is an open-source vector database platform designed for various vector data management tasks. It is suitable for both similarity search and data storage.
    - **Key Features**:
        - Scalability and support for distributed deployment.
        - Plug-and-play indexing methods and storage engines.
        - GPU acceleration for efficient similarity search.
        - Integration with machine learning frameworks.
    - **Open Source**: Milvus is an open-source project that can be self-hosted or used as a managed service.
    - ***Source Code Availability*:** Open source.
    - ***Hosting Methods*:** Supports cloud-native and managed offerings.
    - ***Indexing Methods*:** Custom implementations, including DiskANN.
    - ***Pros*:** Mature with a variety of algorithms, highly scalable.
    - ***Cons*:** Complex architecture, less intuitive client APIs compared to some newer databases.
    
    # 4. ChromaDB
    
- **Use Case**: ChromaDB is a blockchain-based, decentralized database system for managing various data types, including vector data. It offers a unique approach to data storage and sharing.
- **Key Features**:
    - Built on blockchain technology for data integrity and trust.
    - Enables data sharing across organizations and networks.
    - Supports multiple data types, including vector data.
    - Use cases often involve supply chain, property management, and more.
- **Blockchain Integration**: ChromaDB leverages blockchain principles for data security and decentralization.
- ***Source Code Availability*:** Not explicitly mentioned, but appears to build on open-source components.
- ***Hosting Methods*:** Offers embedded mode (default), managed cloud-native, and server-less cloud-hosted distributed options.
- ***Indexing Methods*:** Not specified.
- ***Pros*:** Offers a server-less, embedded option. Plans for different hosting methods, including server-less and cloud-native.
- ***Cons*:** Wraps around existing open-source components, lacks its own storage layer.