---
title: Using AsynchronousFileChannel and CompletionHandler to read a file
nav: Using AsynchronousFileChan...
description: Using AsynchronousFileChannel and CompletionHandler to read a file
section: Imported - java2s Archive
order: 1139
source: https://web.archive.org/web/20130622230817/http://www.java2s.com:80/Code/Java/JDK-7/UsingAsynchronousFileChannelandCompletionHandlertoreadafile.htm
---
Using AsynchronousFileChannel and CompletionHandler to read a file

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path file = Paths.get("/usr/a/foobar.txt");
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(file);
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    channel.read(buffer, 0, buffer,
        new CompletionHandler<Integer, ByteBuffer>() {
          public void completed(Integer result, ByteBuffer attachment) {
            System.out.println("Bytes read [" + result + "]");
          }
          public void failed(Throwable exception, ByteBuffer attachment) {
            System.out.println(exception.getMessage());
          }
        });
  }
}
```

1.  Using AsynchronousFileChannel and Future to read
---  ---
2.  Writing to a file using the AsynchronousFileChannel class
3.  Using AsynchronousFileChannel to write ByteBuffer and return Future
4.  Reading from a file using the AsynchronousFileChannel class
5.  Reading from a file using the AsynchronousFileChannel class
6.  Managing asynchronous communication using the AsynchronousServerSocketChannel
7.  Communication with AsynchronousSocketChannel
