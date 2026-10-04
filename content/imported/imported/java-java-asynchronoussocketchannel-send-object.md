---
title: Java AsynchronousSocketChannel send object
nav: Java AsynchronousSocketCha...
description: privatevoid start() throwsIOException, ExecutionException, TimeoutException, InterruptedException {
section: Imported
order: 20037
source: http://www.java2s.com/ref/java/java-asynchronoussocketchannel-send-object.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousSocketChannel send object

```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.Channels;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeoutException;

publicclass Main {

   InetSocketAddress hostAddress;

   privatevoid start() throwsIOException, ExecutionException, TimeoutException, InterruptedException {
      hostAddress = newInetSocketAddress(InetAddress.getByName("127.0.0.1"), 2583);

      Thread serverThread = newThread(newRunnable() {
         @Override//fromwww.java2s.compublicvoid run() {
            serverStart();
         }
      });

      serverThread.start();

      Thread clientThread = newThread(newRunnable() {
         @Overridepublicvoid run() {
            clientStart();
         }
      });
      clientThread.start();

   }

   privatevoid clientStart() {
      try {
         AsynchronousSocketChannel clientSocketChannel = AsynchronousSocketChannel.open();
         Future<Void> connectFuture = clientSocketChannel.connect(hostAddress);
         connectFuture.get(); // Wait until connection is done.OutputStream os = Channels.newOutputStream(clientSocketChannel);
         ObjectOutputStream oos = newObjectOutputStream(os);
         for (int i = 0; i < 5; i++) {
            oos.writeObject("Look at me " + i);
            Thread.sleep(1000);
         }
         oos.writeObject("EOF");
         oos.close();
         clientSocketChannel.close();
      } catch (Exception e) {
         e.printStackTrace();
      }

   }

   privatevoid serverStart() {
      try {
         AsynchronousServerSocketChannel serverSocketChannel = AsynchronousServerSocketChannel.open().bind(hostAddress);
         Future<AsynchronousSocketChannel> serverFuture = serverSocketChannel.accept();
         finalAsynchronousSocketChannel clientSocket = serverFuture.get();
         System.out.println("Connected!");
         if ((clientSocket != null) && (clientSocket.isOpen())) {
            InputStream connectionInputStream = Channels.newInputStream(clientSocket);
            ObjectInputStream ois = null;
            ois = newObjectInputStream(connectionInputStream);
            while (true) {
               Object object = ois.readObject();
               if (object.equals("EOF")) {
                  clientSocket.close();
                  break;
               }
               System.out.println("Received :" + object);
            }
            ois.close();
            connectionInputStream.close();
         }

      } catch (Exception e) {
         e.printStackTrace();
      }

   }

   publicstaticvoid main(String[] args)
         throwsIOException, ExecutionException, TimeoutException, InterruptedException {
      Main example = new Main();
      example.start();
   }

}
```

PreviousNext

## Related

- Java AsynchronousServerSocketChannel use Future object in a server
- Java AsynchronousSocketChannel create asynchronous client socket channel
- Java AsynchronousSocketChannel create client
- Java CompletionHandler implement
- Java DatagramChannel class
