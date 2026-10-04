---
title: Java IO Tutorial - Java Asynchronous I/O
nav: Java IO Tutorial - Java As...
description: In a synchronous file I/O, the request to the I/O operation waits until the I/O operation is complete.
section: Imported - java2s Archive
order: 50238
source: https://www.java2s.com/Tutorials/Java/Java_io/1050__Java_nio_Asynchronous.html
---
```java title=Example.java
```

In a synchronous file I/O, the request to the I/O operation waits until the I/O operation is complete.

In an asynchronous file I/O, the request for an I/O operation is performed by the system asynchronously.

When the system finishes the file I/O, it notifies the application about the completion of its request.

java.nio.channels.AsynchronousFileChannel class represents an asynchronous file channel.

The static open() method of the AsynchronousFileChannel class gets an instance of the AsynchronousFileChannel class.

The following code shows how to get an asynchronous file channel for WRITE.

```java title=Example.java
Path  path   = Paths.get("C:\\Java_Dev\\rainbow.txt");
AsynchronousFileChannel afc   = AsynchronousFileChannel.open(path, WRITE,  CREATE);
```

The AsynchronousFileChannel provides two ways to handle the result of an asynchronous file I/O operation.

- Using a java.util.concurrent.Future object.
- Using a java.nio.channels.CompletionHandler object.

Each method of the AsynchronousFileChannel class that supports asynchronous file I/O operation has two versions.

One version returns a Future object, which we can use to handle the result of the requested asynchronous operation.

The get() method of the Future object returns the number of bytes written to the file channel.

The following code uses the version of the write() method that returns a Future object:

```java title=Example.java
ByteBuffer dataBuffer  = a buffer;
long  startPosition = 0;
Future<Integer> result = afc.write(dataBuffer, startPosition);
```

Once we get a Future object, we can use a polling method or a blocked waiting method to handle the result of the asynchronous file I/O.

The following code shows the polling method, where it keeps calling the isDone() method of the Future object to check if the I/O operation is finished:

```java title=Example.java
while (!result.isDone()) {
}
int writtenNumberOfBytes = result.get();
```

Another version of the methods of the AsynchronousFileChannel class gets a CompletionHandler object whose methods are called when the requested asynchronous I/O operation completes or fails.

The CompletionHandler interface has two methods: completed() and failed().

The completed() method is called when the requested I/O operation completes successfully.

When the requested I/O operation fails, the failed() method is called.

The following code uses an object of the Attachment class as an attachment to completion handler:

```java title=Example.java
class  Attachment {
    public Path  path;
    public  ByteBuffer buffer;
    public  AsynchronousFileChannel asyncChannel;
}
class MyHandler implements CompletionHandler<Integer,  Attachment>   {
    @Override
    public void  completed(Integer result, Attachment attach)  {
        // Handle  completion of  the   I/O  operation
    }
    @Override
    public void  failed(Throwable e,  Attachment attach)  {
        // Handle  failure of  the   I/O  operation
    }
}
```

The following code uses a MyHandler instance as a completion handler for an asynchronous write operation.

```java title=Example.java
MyHandler handler = new MyHandler();
ByteBuffer dataBuffer  = get   a  data buffer;
Attachment attach  = new Attachment();
attach.asyncChannel = afc;
attach.buffer = dataBuffer;
attach.path = path;
// Perform  the   asynchronous write operation
afc.write(dataBuffer, 0, attach, handler);
```

The following code demonstrates how to use a CompletionHandler object to handle the results of an asynchronous write to a file.

```java title=Example.java
import static java.nio.file.StandardOpenOption.CREATE;
import static java.nio.file.StandardOpenOption.WRITE;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    Path path = Paths.get("test.txt");
    AsynchronousFileChannel afc = AsynchronousFileChannel.open(path, WRITE,
        CREATE);
    WriteHandler handler = new WriteHandler();
    ByteBuffer dataBuffer = getDataBuffer();
    Attachment attach = new Attachment();
    attach.asyncChannel = afc;
    attach.buffer = dataBuffer;
    attach.path = path;
    afc.write(dataBuffer, 0, attach, handler);
    System.out.println("Sleeping for 5  seconds...");
    Thread.sleep(5000);
  }
  publicstatic ByteBuffer getDataBuffer() {
    String lineSeparator = System.getProperty("line.separator");
    StringBuilder sb = new StringBuilder();
    sb.append("test");
    sb.append(lineSeparator);
    sb.append("test");
    sb.append(lineSeparator);
    String str = sb.toString();
    Charset cs = Charset.forName("UTF-8");
    ByteBuffer bb = ByteBuffer.wrap(str.getBytes(cs));
    return bb;
  }
}
class Attachment {
  public Path path;
  public ByteBuffer buffer;
  public AsynchronousFileChannel asyncChannel;
}
class WriteHandler implements CompletionHandler<Integer, Attachment> {
  @Override
  public void completed(Integer result, Attachment attach) {
    System.out.format("%s bytes written  to  %s%n", result,
        attach.path.toAbsolutePath());
    try {
       attach.asyncChannel.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  @Override
  public void failed(Throwable e, Attachment attach) {
    try {
      attach.asyncChannel.close();
    } catch (IOException e1) {
      e1.printStackTrace();
    }
  }
}
```

## Example

The following code demonstrates how to use a Future object to handle the results of an asynchronous write to a file.

```java title=Example.java
importstatic java.nio.file.StandardOpenOption.CREATE;
importstatic java.nio.file.StandardOpenOption.WRITE;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.Future;
publicclass Main {
  publicstatic ByteBuffer getDataBuffer() {
    String lineSeparator = System.getProperty("line.separator");
    StringBuilder sb = new StringBuilder();
    sb.append("test");
    sb.append(lineSeparator);
    String str = sb.toString();
    Charset cs = Charset.forName("UTF-8");
    ByteBuffer bb = ByteBuffer.wrap(str.getBytes(cs));
    return bb;
  }
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("test.txt");
    try (AsynchronousFileChannel afc = AsynchronousFileChannel.open(path,
        WRITE, CREATE)) {
      ByteBuffer dataBuffer = getDataBuffer();
      Future<Integer> result = afc.write(dataBuffer, 0);
      while (!result.isDone()) {
        System.out.println("Sleeping for 2  seconds...");
        Thread.sleep(2000);
      }
      int writtenBytes = result.get();
      System.out.format("%s bytes written  to  %s%n", writtenBytes,
          path.toAbsolutePath());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Example 2

The following code demonstrates how to use a CompletionHandler object to handle the results of an asynchronous read from a file.

```java title=Example.java
importstatic java.nio.file.StandardOpenOption.READ;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception{
    Path path = Paths.get("test.txt");
    AsynchronousFileChannel afc = AsynchronousFileChannel.open(path, READ);
    ReadHandler handler = new ReadHandler();
    int fileSize = (int) afc.size();
    ByteBuffer dataBuffer = ByteBuffer.allocate(fileSize);
    Attachment attach = new Attachment();
    attach.asyncChannel = afc;
    attach.buffer = dataBuffer;
    attach.path = path;
    afc.read(dataBuffer, 0, attach, handler);
    System.out.println("Sleeping for 5  seconds...");
    Thread.sleep(5000);
  }
}
class Attachment {
  public Path path;
  public ByteBuffer buffer;
  public AsynchronousFileChannel asyncChannel;
}
class ReadHandler implements CompletionHandler<Integer, Attachment> {
  @Override
  publicvoid completed(Integer result, Attachment attach) {
    System.out.format("%s bytes read   from  %s%n", result, attach.path);
    System.out.format("Read data is:%n");
    byte[] byteData = attach.buffer.array();
    Charset cs = Charset.forName("UTF-8");
    String data = new String(byteData, cs);
    System.out.println(data);
    try {
      // Close the channel
      attach.asyncChannel.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  @Override
  publicvoid failed(Throwable e, Attachment attach) {
    System.out.format("Read operation  on  %s  file failed."
        + "The  error is: %s%n", attach.path, e.getMessage());
    try {
      // Close the channel
      attach.asyncChannel.close();
    } catch (IOException e1) {
      e1.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Example 3

The following code shows how to use a Future object to handle the results of an asynchronous read from a file. It uses the wait method (a Future.get() method call) to wait for the asynchronous file I/O to complete.

```java title=Example.java
importstatic java.nio.file.StandardOpenOption.READ;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("test.txt");
    try (AsynchronousFileChannel afc = AsynchronousFileChannel.open(path, READ)) {
      int fileSize = (int) afc.size();
      ByteBuffer dataBuffer = ByteBuffer.allocate(fileSize);
      Future<Integer> result = afc.read(dataBuffer, 0);
      int readBytes = result.get();
      System.out.format("%s bytes read   from  %s%n", readBytes, path);
      System.out.format("Read data is:%n");
      byte[] byteData = dataBuffer.array();
      Charset cs = Charset.forName("UTF-8");
      String data = new String(byteData, cs);
      System.out.println(data);
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
