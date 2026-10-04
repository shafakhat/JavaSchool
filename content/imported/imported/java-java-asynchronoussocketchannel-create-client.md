---
title: Java AsynchronousSocketChannel create client
nav: Java AsynchronousSocketCha...
description: try {//fromwww.java2s.comAsynchronousSocketChannel client = AsynchronousSocketChannel.open();
section: Imported
order: 20043
source: http://www.java2s.com/ref/java/java-asynchronoussocketchannel-create-client.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousSocketChannel create client

```java title=Example.java
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousSocketChannel;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

publicclass Main {

   publicstaticvoid main(String[] args) {
      try {//fromwww.java2s.comAsynchronousSocketChannel client = AsynchronousSocketChannel.open();
         InetSocketAddress address = newInetSocketAddress("localhost", 5000);

         Future<Void> future = client.connect(address);
         System.out.println("Client: Waiting for the connection to complete");
         future.get();

         String message = "";
         while (!message.equals("quit")) {
            System.out.print("Enter a message: ");
            Scanner scanner = newScanner(System.in);
            message = scanner.nextLine();
            System.out.println("Client: Sending ...");
            ByteBuffer buffer = ByteBuffer.wrap(message.getBytes());
            System.out.println("Client: Message sent: " + newString(buffer.array()));
            client.write(buffer);
         }

      } catch (IOException | InterruptedException | ExecutionException ex) {
         ex.printStackTrace();
      }
   }

}
```

PreviousNext

## Related

- Java AsynchronousServerSocketChannel send object
- Java AsynchronousServerSocketChannel use Future object in a server
- Java AsynchronousSocketChannel create asynchronous client socket channel
- Java AsynchronousSocketChannel send object
- Java CompletionHandler implement
