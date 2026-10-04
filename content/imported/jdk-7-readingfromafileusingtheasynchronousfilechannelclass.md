---
title: Reading from a file using the AsynchronousFileChannel class
nav: Reading from a file using ...
description: AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(
section: Imported - java2s Archive
order: 1117
source: https://web.archive.org/web/20130620171555/http://www.java2s.com:80/Code/Java/JDK-7/ReadingfromafileusingtheAsynchronousFileChannelclass.htm
---
Reading from a file using the AsynchronousFileChannel class

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.EnumSet;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ScheduledThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
public class Test {
  public static void main(String args[]) throws Exception {
    ExecutorService pool = new ScheduledThreadPoolExecutor(3);
    AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(
        Paths.get("data.txt"), EnumSet.of(StandardOpenOption.READ),
        pool);
    CompletionHandler<Integer, ByteBuffer> handler = new CompletionHandler<Integer, ByteBuffer>() {
      @Override
      public synchronized void completed(Integer result, ByteBuffer attachment) {
        for (int i = 0; i < attachment.limit(); i++) {
          System.out.println((char) attachment.get(i));
        }
      }
      @Override
      public void failed(Throwable e, ByteBuffer attachment) {
      }
    };
    final int bufferCount = 5;
    ByteBuffer buffers[] = new ByteBuffer[bufferCount];
    for (int i = 0; i < bufferCount; i++) {
      buffers[i] = ByteBuffer.allocate(10);
      fileChannel.read(buffers[i], i * 10, buffers[i], handler);
    }
    pool.awaitTermination(1, TimeUnit.SECONDS);
    for (ByteBuffer byteBuffer : buffers) {
      for (int i = 0; i < byteBuffer.limit(); i++) {
        System.out.print((char) byteBuffer.get(i));
      }
    }
  }
}
```

1.  Using AsynchronousFileChannel and Future to read
---  ---
2.  Using AsynchronousFileChannel and CompletionHandler to read a file
3.  Writing to a file using the AsynchronousFileChannel class
4.  Using AsynchronousFileChannel to write ByteBuffer and return Future
5.  Reading from a file using the AsynchronousFileChannel class
6.  Managing asynchronous communication using the AsynchronousServerSocketChannel
7.  Communication with AsynchronousSocketChannel
