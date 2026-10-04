---
title: Using AsynchronousFileChannel to write ByteBuffer and return Future
nav: Using AsynchronousFileChan...
description: Using AsynchronousFileChannel to write ByteBuffer and return Future
section: Imported - java2s Archive
order: 1141
source: https://web.archive.org/web/20130622143433/http://www.java2s.com:80/Code/Java/JDK-7/UsingAsynchronousFileChanneltowriteByteBufferandreturnFuture.htm
---
```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.concurrent.Future;
public class Test {
  public static void main(String[] args) throws Exception {
    AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(
        Paths.get("/asynchronous.txt"), StandardOpenOption.READ,
        StandardOpenOption.WRITE, StandardOpenOption.CREATE);
    Future<Integer> writeFuture1 = fileChannel.write(
        ByteBuffer.wrap("Sample".getBytes()), 0);
    Future<Integer> writeFuture2 = fileChannel.write(
        ByteBuffer.wrap("Box".getBytes()), 0);
    int result;
    result = writeFuture1.get();
    System.out.println("Sample write completed with " + result
        + " bytes written");
    result = writeFuture2.get();
    System.out.println("Box write completed with " + result + " bytes written");
  }
}
```

1.  Using AsynchronousFileChannel and Future to read
---  ---
2.  Using AsynchronousFileChannel and CompletionHandler to read a file
3.  Writing to a file using the AsynchronousFileChannel class
4.  Reading from a file using the AsynchronousFileChannel class
5.  Reading from a file using the AsynchronousFileChannel class
6.  Managing asynchronous communication using the AsynchronousServerSocketChannel
7.  Communication with AsynchronousSocketChannel
