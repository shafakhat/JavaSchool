---
title: Java AsynchronousFileChannel write to file
nav: Java AsynchronousFileChann...
description: try (AsynchronousFileChannel afc = AsynchronousFileChannel.open(path,
section: Imported
order: 20034
source: http://www.java2s.com/ref/java/java-asynchronousfilechannel-write-to-file.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousFileChannel write to file

```java title=Example.java
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("Main.txt");

    try (AsynchronousFileChannel afc = AsynchronousFileChannel.open(path,
        StandardOpenOption.WRITE,
        StandardOpenOption.CREATE)) {

      ByteBuffer dataBuffer = ByteBuffer.wrap(newbyte[] {63,64,65,66});

      // Perform the asynchronous write operationFuture<Integer> result = afc.write(dataBuffer, 0);

      while (!result.isDone()) {
        try {//fromwww.java2s.comSystem.out.println("Sleeping for 2 seconds...");
          Thread.sleep(2000);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
      }

      try {
        int writtenBytes = result.get();
        System.out.format("%s bytes written to %s%n", writtenBytes,
            path.toAbsolutePath());
      } catch (InterruptedException | ExecutionException e) {
        e.printStackTrace();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

publicclass Main {
   publicstaticvoid main(String[] args) {
      try (AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(Paths.get("Main.java"),
            StandardOpenOption.READ, StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
         CompletionHandler<Integer, Object> handler = newCompletionHandler<Integer, Object>() {

            @Override/*fromwww.java2s.com*/publicvoid completed(Integer result, Object attachment) {
               System.out.println("Attachment: " + attachment + " " + result + " bytes written");
               System.out.println("CompletionHandler Thread ID: " + Thread.currentThread().getId());
            }

            @Overridepublicvoid failed(Throwable e, Object attachment) {
               System.err.println("Attachment: " + attachment + " failed with:");
               e.printStackTrace();
            }
         };

         System.out.println("Main Thread ID: " + Thread.currentThread().getId());
         fileChannel.write(ByteBuffer.wrap("Sample".getBytes()), 0, "First Write", handler);
         fileChannel.write(ByteBuffer.wrap("Box".getBytes()), 0, "Second Write", handler);

      } catch (Exception ex) {
         ex.printStackTrace();
      }
   }
}
```

PreviousNext

## Related

- Java ShortBuffer compare with ByteBuffer for byte content
- Java ShortBuffer convert from ByteBuffer
- Java AsynchronousFileChannel create for read and write
- Java AsynchronousFileChannel read from file
- Java AsynchronousFileChannel with custom CompletionHandler
