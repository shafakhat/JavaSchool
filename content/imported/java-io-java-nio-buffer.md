---
title: Java IO Tutorial - Java I/O Buffer
nav: Java IO Tutorial - Java I/...
description: In NIO, we deal with channels and buffers for I/O operations.
section: Imported - java2s Archive
order: 50222
source: https://www.java2s.com/Tutorials/Java/Java_io/0900__Java_nio_Buffer.html
---
## What Is NIO?

In NIO, we deal with channels and buffers for I/O operations.

A channel, like a stream represents a connection between a data source/sink and a Java program for data transfer.

A channel provides a two-way data transfer facility. We can use a channel to read data as well as to write data. We can obtain a read-only channel, a write-only channel, or a read-write channel depending on our needs.

In stream-based I/O, the basic unit of data transfer is a byte. In channel-based NIO, the basic unit of data transfer is a buffer.

A buffer has a fixed capacity that determines the upper limit of the data it may contain.

In channel-based I/O, we write data into a buffer and we pass that buffer to the channel, which writes the data.

To read data from a data source, we pass a buffer to a channel. The channel reads data from the data source into a buffer.

## Buffers

A buffer is a fixed-length data container. There is a separate buffer type to hold data for each type of primitive value, except for boolean type values.

A buffer is an object in our program. We have a separate class to represent each type of buffer.

All buffer classes are inherited from an abstract Buffer class. Buffer classes that hold primitive values are as follows:

- ByteBuffer
- ShortBuffer
- CharBuffer
- IntBuffer
- LongBuffer
- FloatBuffer
- DoubleBuffer

Different buffer holds data in different data type. For example, a ByteBuffer holds byte values; a ShortBuffer holds short values; a CharBuffer holds characters, and so on.

## Buffer Properties

The following are the four important properties of a buffer.

- Capacity
- Position
- Limit
- Mark

The capacity of a buffer is the maximum number of elements that it can hold. and it is fixed when the buffer is created.

We can check if a buffer is backed by an array by calling its hasArray() method that returns true if the buffer is backed by an array.

We can get access to the backing array by using the array() method of the buffer object.

Once we get access to the backing array, any changes made to that array will be reflected in the buffer.

A buffer has a capacity() method that returns its capacity.

## Buffer Create

We can create a buffer by using the allocate() factory method of a particular buffer class as follows:

The following code creates a byte buffer with the capacity as 8

```java title=Example.java
ByteBuffer bb  = ByteBuffer.allocate(8);
```

To get the capacity

```java title=Example.java
int capacity = bb.capacity();
```

The following code creates a character buffer with the capacity as 1024

```java title=Example.java
CharBuffer cb  = CharBuffer.allocate(1024);
```

A byte buffer has a method called allocateDirect() which creates a byte buffer for which the memory is allocated from the operating system memory, not from the JVM heap.

We can use the isDirect() method of the ByteBuffer class to check if a buffer is direct or non-direct.

```java title=Example.java
// Create a  direct byte   buffer of  512  bytes capacity
ByteBuffer bbd = ByteBuffer.allocateDirect(512);
```

Another way to create a buffer is to wrap an array using the buffer's static wrap() method.

```java title=Example.java
byte[]  byteArray = new byte[512];
ByteBuffer bb  = ByteBuffer.wrap(byteArray);
```

We can use the same technique to create a buffer to store other primitive values.

When we create a buffer, all elements of the buffer are initialized to a value of zero.

## Buffer Index Position

Each element of a buffer has an index. The first element has an index of 0 and the last element has an index of capacity - 1.

When a buffer is created, its position is set to 0 and its limit is equal to its capacity.

We can get/set the position of a buffer using its overloaded position() method.

The position() method returns the current value of the position of a buffer.

The position(int newPosition) method sets the position of the buffer to the specified newPosition value and returns the reference of the buffer.

We can get/set the limit of a buffer using its overloaded limit() method.

The limit() method returns the current value of the limit of a buffer. The limit(int newLimit) method sets the limit of a buffer to the specified newLimit value and returns the reference of the buffer.

We can bookmark a position of a buffer by using the mark() method. When we call the mark() method, the buffer stores the current value of its position as its mark value. We can set the position of a buffer to its previously bookmarked value by using the reset() method.

The buffer's mark is not defined when it is created. We must call the reset() method on a buffer only when its mark is defined. Otherwise, the reset() method throws an InvalidMarkException.

The following code creates a new buffer and display its four properties.

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.InvalidMarkException;
publicclass Main {
  publicstaticvoid main(String[] args) {
    ByteBuffer bb = ByteBuffer.allocate(8);
    System.out.println("Capacity: " + bb.capacity());
    System.out.println("Limit: " + bb.limit());
    System.out.println("Position: " + bb.position());
    // The mark is not set for a new buffer. Calling the
// reset() method throws a runtime exception if the mark is not set.
try {
      bb.reset();
      System.out.println("Mark: " + bb.position());
    } catch (InvalidMarkException e) {
      System.out.println("Mark is not  set");
    }
  }
}
```

The code above generates the following result.

- « Previous
