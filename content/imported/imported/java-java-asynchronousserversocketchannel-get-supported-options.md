---
title: Java AsynchronousServerSocketChannel get supported options
nav: Java AsynchronousServerSoc...
description: try {//fromwww.java2s.comfinalAsynchronousServerSocketChannel listener = AsynchronousServerSocketChannel.open();
section: Imported
order: 20035
source: http://www.java2s.com/ref/java/java-asynchronousserversocketchannel-get-supported-options.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousServerSocketChannel get supported options

```java title=Example.java
import java.net.InetSocketAddress;
import java.net.SocketOption;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.util.Set;

publicclass Main {

   publicstaticvoid main(String[] args) {
      try {//fromwww.java2s.comfinalAsynchronousServerSocketChannel listener = AsynchronousServerSocketChannel.open();
         InetSocketAddress address = newInetSocketAddress("localhost", 5000);
         listener.bind(address);

         Set<SocketOption<?>> options = listener.supportedOptions();
         for (SocketOption<?> socketOption : options) {
            System.out.println(socketOption.toString() + ": " + listener.getOption(socketOption));
         }
      } catch (Exception e) {
         e.printStackTrace();
      }
   }
}
```

PreviousNext

## Related

- Java AsynchronousFileChannel use Future object
- Java AsynchronousServerSocketChannel create asynchronous echo server
- Java AsynchronousServerSocketChannel create server
- Java AsynchronousServerSocketChannel read object from client
- Java AsynchronousServerSocketChannel send object
