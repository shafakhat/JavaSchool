---
title: Java AsynchronousServerSocketChannel use Future object in a server
nav: Java AsynchronousServerSoc...
description: Java AsynchronousServerSocketChannel use Future object in a server
section: Imported
order: 20042
source: http://www.java2s.com/ref/java/java-asynchronousserversocketchannel-use-future-object-in-a-server.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousServerSocketChannel use Future object in a server

```java title=Example.java
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.nio.channels.AsynchronousSocketChannel;
import java.util.concurrent.Future;

publicclass Main {

   publicstaticvoid main(String[] args) {
      try {//fromwww.java2s.comfinalAsynchronousServerSocketChannel listener = AsynchronousServerSocketChannel.open();
         InetSocketAddress address = newInetSocketAddress("localhost", 5000);
         listener.bind(address);
         // Using the Future object in a serverFuture<AsynchronousSocketChannel> future = listener.accept();
         AsynchronousSocketChannel worker = future.get();

         while (true) {
            // WaitSystem.out.println("Server: Receiving ...");
            ByteBuffer buffer = ByteBuffer.allocate(32);
            Future<Integer> readFuture = worker.read(buffer);
            Integer number = readFuture.get();
            System.out.println(number);
            System.out.println("Server: Message received: " + newString(buffer.array()));
         }

      } catch (Exception ex) {

         ex.printStackTrace();
      }
   }
}
```

PreviousNext

## Related

- Java AsynchronousServerSocketChannel get supported options
- Java AsynchronousServerSocketChannel read object from client
- Java AsynchronousServerSocketChannel send object
- Java AsynchronousSocketChannel create asynchronous client socket channel
- Java AsynchronousSocketChannel create client
