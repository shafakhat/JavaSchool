---
title: Using AsynchronousFileChannel and Future to read
nav: Using AsynchronousFileChan...
description: AsynchronousFileChannel channel = AsynchronousFileChannel.open(file);
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20130618052503/http://www.java2s.com:80/Code/Java/JDK-7/UsingAsynchronousFileChannelandFuturetoread.htm
---
Using AsynchronousFileChannel and Future to read

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.Future;
public class Test {
  public static void main(String[] args) throws Exception {
    Path file = Paths.get("/usr/a.txt");
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(file);
    ByteBuffer buffer = ByteBuffer.allocate(100_000);
    Future<Integer> result = channel.read(buffer, 0);
    while (!result.isDone()) {
      ProfitCalculator.calculateTax();
    }
    Integer bytesRead = result.get();
    System.out.println("Bytes read [" + bytesRead + "]");
  }
}
class ProfitCalculator {
  public ProfitCalculator() {
  }
  public static void calculateTax() {
  }
}
```

1.  Using AsynchronousFileChannel and CompletionHandler to read a file
---  ---
2.  Writing to a file using the AsynchronousFileChannel class
3.  Using AsynchronousFileChannel to write ByteBuffer and return Future
4.  Reading from a file using the AsynchronousFileChannel class
5.  Reading from a file using the AsynchronousFileChannel class
6.  Managing asynchronous communication using the AsynchronousServerSocketChannel
7.  Communication with AsynchronousSocketChannel
