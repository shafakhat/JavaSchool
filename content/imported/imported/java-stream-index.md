---
title: Java Streams - Java Stream Introduction
nav: Java Streams - Java Stream...
description: A stream is a sequence of data values supporting sequential and parallel aggregate operations.
section: Imported - java2s Archive
order: 50049
source: https://www.java2s.com/Tutorials/Java/Java_Stream/index.html
---
- Next »

A stream is a sequence of data values supporting sequential and parallel aggregate operations.

We use the aggregate functions in SQL more often. For example we can sum all sale figures for a month or a year. We can also get the max value for a give range.

An aggregate operation works on a list of item and results in a single value.

The result of an aggregate operation on stream may be a primitive value, an object, or a void for Stream. Like SQL we can calculate sum for all integers in a stream of integers.

## Collections vs Streams

Java Collections focus on how to store data elements for efficient access.

Java streams focus on aggregate operations on data elements from a data source.

## Streams Features

Java Streams have its own features.

## No Storage

Java Streams have no storage.

A collection is an in-memory data structure that stores all its elements.

A stream has no storage. A stream pulls elements from a data source on-demand and passes them to a pipeline of operations for processing.

For a collection we talk about the storage or how the data elements are stored, how to access data elements.

For a stream we focus on the operations, for example, how to sum a stream.

## Infinite Streams

A collection cannot represent a group of infinite elements whereas a stream can.

A stream can pull its elements from a data source. The data source can be a collection, a function that generates data, an I/O channel, etc.

A stream can pull data from from a function which generates infinite number of elements.

## Not Reusable

Streams Are Not Reusable

A stream cannot be reused after calling a terminal operation.

To perform a computation on the same elements from the same data source, we have to recreate the stream pipeline.

A stream may throw an IllegalStateException in case of reusing.

- Next »
