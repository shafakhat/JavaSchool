---
title: Java IO Tutorial - Java I/O
nav: Java IO Tutorial - Java I/O
description: Java Input/output (I/O) deals with reading data from a source and writing data to a destination.
section: Imported - java2s Archive
order: 50003
source: https://www.java2s.com/Tutorials/Java/Java_io/index.html
---
Java Input/output (I/O) deals with reading data from a source and writing data to a destination.

Typically, we read data stored in a file or write data to a file using I/O.

The java.io and java.nio packages contain Java classes that deal with I/O.

The java.io package has classes to perform I/O.

The java.nio package is new I/O package.

The classes in the java.io package are all about the stream based I/O operations. The stream-based I/O uses streams to transfer byte data between a data source and a Java program.

The Java program reads from or writes to a stream a byte at a time. This approach to performing I/O operations is slow. A stream can be used for one-way data transfer. An input stream can only transfer data from a data source to a Java program and an output stream can only transfer data from a Java program to a data destination.

The New Input/Ouput (NIO) solves the slow speed problem in the stream-based I/O.

In NIO, we deal with channels and buffers for I/O operations.

A channel is like a stream. It represents a connection between a data source and a Java program.

A channel provides a two-way data transfer facility. We can use a channel to read data as well as to write data.

We can obtain a read-only channel, a write-only channel, or a read-write channel.

A buffer is a bounded data container and has a fixed capacity that determines the upper limit of the data it may contain.

In stream-based I/O, we write data directly to the stream. In channel-based I/O, we write data into a buffer and we pass that buffer to the channel, which writes the data to the data destination.

When reading data from a data source, we pass a buffer to a channel. The channel reads data from the data source into a buffer.

Java 7 introduced New Input/Output 2 API, which provides a new I/O API. It provides many features that were lacking in the original File I/O API.

It adds three packages to the Java class library: java.nio.file, java.nio.file.attribute, and java.nio.file.spi.

New Input/Output 2 API deals with all file systems in a uniform way. The file system support provided by New Input/Output 2 API is extensible.

New Input/Output 2 API supports basic file operations (copy, move, and delete) on all file systems. It has support for symbolic links.

It supports for accessing the attributes of file systems and files.

We can creates a watch service to watch for any events on a directory such as adding a new file or a subdirectory, deleting a file, etc.
