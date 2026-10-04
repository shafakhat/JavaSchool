---
title: MongoDB Tutorial - MongoDB Introduction
nav: MongoDB Tutorial - MongoDB...
description: MongoDB written in c++ is an open-source document/NoSQL database.
section: Imported - java2s Archive
order: 50040
source: https://www.java2s.com/Tutorials/Java/MongoDB/index.html
---
MongoDB written in c++ is an open-source document/NoSQL database.

Relational database has a schema and keeps the relationship between tables. While in MongoDB is schema-less.

MongoDB uses collections to hold documents. MongoDB is easy to scale out.

In MongoDB, Data is stored in the form of JSON style documents. We can create index on any attribute and and we can do Replication and Sharding.

## Core concepts in MongoDB

MongoDB uses Database to organize data. Database is a container for collections. Each database has its own set of files on the file system. A single MongoDB server typically has multiple databases.

Collection is a group of MongoDB documents. It is the equivalent of an RDBMS table. A collection exists within a database. Unlike RDBMS table, collections has no schema. Documents within a collection can have different fields. All documents in a collection have similar or related purpose.

A document is a set of key-value pairs. Documents have dynamic schema. Documents in the same collection do not need to have the same set of fields, and common fields in a collection's documents may hold different types of data.

## MongoDB vs RDBMS

Below given table shows the relationship of RDBMS terminology with MongoDB.

RDBMS  MongoDB
---  ---
Database  Database
Table  Collection
Tuple/Row  Document
column  Field
Table Join  Embedded Documents
Primary Key  Primary Key (Default key _id provided by mongodb itself)

## Sample document

The following code has an example showing the document structure of a website used in MongoDB.

```java title=Example.java

{
   _id: ObjectId(7df22ad2222c)
   title: 'MongoDB Tutorial',
   description: 'MongoDB is no sql database',
   by: 'java2s.com',
   url: 'http://www.java2s.com',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 222,
   comments: [
      {
         user:'user1',
         message: 'My first comment',
         dateCreated: new Date(2014,1,21,2,15),
         like: 0
      },
      {
         user:'user2',
         message: 'My second comments',
         dateCreated: new Date(2011,1,20,7,45),
         like: 5
      }
   ]
}
```

_id is a 12 bytes hexadecimal number which assures the uniqueness of every document.

We can provide _id when inserting the document. MongoDB can generate a unique id for every document if we don't provide.

In those 12 bytes, first 4 bytes for the current timestamp, next 3 bytes for machine id, next 2 bytes for process id of mongodb server and remaining 3 bytes are incremental value.
