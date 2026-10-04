---
title: Java AsynchronousFileChannel with custom CompletionHandler
nav: Java AsynchronousFileChann...
description: class MyCompletionHandler implementsCompletionHandler<Integer, MyClass> {
section: Imported
order: 20033
source: http://www.java2s.com/ref/java/java-asynchronousfilechannel-with-custom-completionhandler.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousFileChannel with custom CompletionHandler

```java title=Example.java
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

class MyClass {//fromwww.java2s.compublicPath path;
  publicByteBuffer buffer;
  publicAsynchronousFileChannel asyncChannel;
}

class MyCompletionHandler implementsCompletionHandler<Integer, MyClass> {
  @Overridepublicvoid completed(Integer result, MyClass attach) {
    byte[] byteData = attach.buffer.array();
    Charset cs = Charset.forName("UTF-8");
    String data = newString(byteData, cs);
    System.out.println(data);

    try {
      // Close the channel
      attach.asyncChannel.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  @Overridepublicvoid failed(Throwable e, MyClass attach) {
    System.out.format(e.getMessage());
    try {
      attach.asyncChannel.close();
    } catch (IOException e1) {
      e1.printStackTrace();
    }
  }
}

publicclass Main {

  publicstaticvoid main(String[] args) {
    Path path = Paths.get("Main.txt");
    try {
      AsynchronousFileChannel afc = AsynchronousFileChannel.open(path,
          StandardOpenOption.READ);

      MyCompletionHandler handler = new MyCompletionHandler();
      // Get the data size in bytes to readint fileSize = (int) afc.size();
      ByteBuffer dataBuffer = ByteBuffer.allocate(fileSize);

      // Prepare the attachment
      MyClass attach = new MyClass();
      attach.asyncChannel = afc;
      attach.buffer = dataBuffer;
      attach.path = path;

      afc.read(dataBuffer, 0, attach, handler);

      try {
        System.out.println("Sleeping for 5 seconds...");
        Thread.sleep(5000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }

      System.out.println("Done...");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

PreviousNext

## Related

- Java AsynchronousFileChannel create for read and write
- Java AsynchronousFileChannel write to file
- Java AsynchronousFileChannel read from file
- Java AsynchronousFileChannel use Future object
- Java AsynchronousServerSocketChannel create asynchronous echo server
