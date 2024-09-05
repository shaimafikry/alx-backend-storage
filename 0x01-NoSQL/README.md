# MongoDB
### What is NoSQL?

NoSQL stands for "Not Only SQL" or "Non-relational SQL." It refers to a class of database management systems that are designed to handle large volumes of data, flexible data models, and distributed architecture without relying on the rigid table-based structure of traditional SQL databases. NoSQL databases are often used for big data applications, real-time web apps, and scenarios where high scalability and flexibility are required.

---

### Difference Between SQL and NoSQL

| Feature           | SQL (Relational)              | NoSQL (Non-relational)           |
|-------------------|-------------------------------|----------------------------------|
| **Data Model**     | Structured, tabular data with rows and columns | Unstructured, semi-structured, or flexible schema (documents, key-value pairs, graphs, etc.) |
| **Schema**         | Fixed, predefined schema      | Dynamic, schema-less             |
| **Scaling**        | Vertical scaling (adding resources to a single machine) | Horizontal scaling (adding more machines) |
| **Transactions**   | Supports ACID transactions    | Some NoSQL databases support ACID, but others prioritize availability and partitioning over strict consistency |
| **Query Language** | SQL (Structured Query Language) | No standard query language, depends on the database (e.g., MongoDB uses queries similar to JavaScript) |
| **Examples**       | MySQL, PostgreSQL, SQLite     | MongoDB, Cassandra, Redis, Couchbase |
| **Use Cases**      | Structured data, complex queries, transactions | Big data, real-time apps, distributed systems, flexible data models |

---

### What is ACID?

ACID is a set of properties that ensure reliable processing of database transactions. It stands for:

- **Atomicity**: Ensures that each transaction is all-or-nothing. If any part of the transaction fails, the entire transaction is rolled back.
- **Consistency**: Ensures that a transaction brings the database from one valid state to another valid state, maintaining data integrity.
- **Isolation**: Ensures that concurrent transactions do not interfere with each other. Each transaction is isolated from others until it is complete.
- **Durability**: Ensures that once a transaction is committed, the data remains permanently saved, even in the event of a system failure.

---

### What is Document Storage?

Document storage is a type of NoSQL database that stores, retrieves, and manages semi-structured data in the form of documents. These documents are typically encoded in formats like JSON, BSON, or XML. Each document can contain key-value pairs, arrays, and nested objects, allowing for flexible and hierarchical data structures.

Example: MongoDB is a popular document-based NoSQL database.

---

### Types of NoSQL Databases

1. **Document Stores**: Store data in the form of documents (e.g., MongoDB, Couchbase).
2. **Key-Value Stores**: Store simple key-value pairs (e.g., Redis, DynamoDB).
3. **Column-family Stores**: Store data in columns instead of rows (e.g., Cassandra, HBase).
4. **Graph Databases**: Store data as nodes and edges, representing relationships (e.g., Neo4j, ArangoDB).

---

### Benefits of a NoSQL Database

1. **Scalability**: NoSQL databases can scale horizontally across multiple servers, allowing them to handle vast amounts of data.
2. **Flexibility**: They allow for schema-less design, enabling dynamic data models.
3. **Performance**: Optimized for large-scale data handling and high throughput.
4. **Distributed Architecture**: Built for distributed computing, which makes them fault-tolerant and able to handle data replication across servers.
5. **Big Data and Real-Time Processing**: Ideal for handling large datasets and real-time data with low latency.

---

### How to Query Information from a NoSQL Database

Querying in NoSQL depends on the specific database type. For example, in MongoDB:

- **Basic Query**:
    ```javascript
    db.collection.find({ "field": "value" });
    ```
- **Filtering and Conditions**:
    ```javascript
    db.collection.find({ "age": { $gt: 25 } });
    ```
- **Aggregation**:
    ```javascript
    db.collection.aggregate([
        { $match: { status: "active" } },
        { $group: { _id: "$status", total: { $sum: 1 } } }
    ]);
    ```

Each NoSQL database has its own querying mechanism, and it often involves either key-value lookups or query languages similar to SQL.

---

### How to Insert/Update/Delete Information from a NoSQL Database

#### In MongoDB (as an example):
- **Insert**:
    ```javascript
    db.collection.insertOne({ "name": "John", "age": 30 });
    db.collection.insertMany([{ "name": "Jane" }, { "name": "Doe" }]);
    ```

- **Update**:
    ```javascript
    db.collection.updateOne(
        { "name": "John" },
        { $set: { "age": 31 } }
    );
    ```

- **Delete**:
    ```javascript
    db.collection.deleteOne({ "name": "John" });
    db.collection.deleteMany({ "age": { $gt: 30 } });
    ```

Each NoSQL database has its own methods for inserting, updating, and deleting data, and they often follow simple commands to modify key-value pairs or document structures.

---

### How to Use MongoDB

1. **Installation**: Install MongoDB on your machine or use a cloud-based solution like MongoDB Atlas.
    ```bash
    sudo apt-get install -y mongodb
    ```

2. **Connecting to MongoDB**:
    - Open the Mongo shell by typing `mongo` in your terminal.

3. **Basic Commands**:
    - **Show Databases**:
        ```bash
        show dbs;
        ```
    - **Create or Select a Database**:
        ```bash
        use myDatabase;
        ```
    - **Insert Data**:
        ```javascript
        db.myCollection.insertOne({ "name": "Alice", "age": 25 });
        ```
    - **Query Data**:
        ```javascript
        db.myCollection.find({ "name": "Alice" });
        ```
    - **Update Data**:
        ```javascript
        db.myCollection.updateOne({ "name": "Alice" }, { $set: { "age": 26 } });
        ```
    - **Delete Data**:
        ```javascript
        db.myCollection.deleteOne({ "name": "Alice" });
        ```

4. **Indexes**:
    - MongoDB allows you to create indexes to improve query performance:
        ```javascript
        db.myCollection.createIndex({ "name": 1 });
        ```

5. **Aggregation**:
    - MongoDB supports aggregation pipelines for complex data processing:
        ```javascript
        db.myCollection.aggregate([
            { $match: { age: { $gt: 20 } } },
            { $group: { _id: "$age", count: { $sum: 1 } } }
        ]);
        ```

MongoDB provides a lot of flexibility, making it a popular choice for applications that require flexible schemas, high availability, and scalability.
