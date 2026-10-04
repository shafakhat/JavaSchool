---
title: Java AsynchronousServerSocketChannel create asynchronous echo server
nav: Java AsynchronousServerSoc...
description: Java AsynchronousServerSocketChannel create asynchronous echo server
section: Imported
order: 20003
source: http://www.java2s.com/ref/java/java-asynchronousserversocketchannel-create-asynchronous-echo-server.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousServerSocketChannel create asynchronous echo server

```java title=Example.java
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.CompletionHandler;
import java.nio.charset.Charset;

class ConnectionHandler implementsCompletionHandler<AsynchronousSocketChannel, Attachment> {
  @Override/*fromwww.java2s.com*/publicvoid completed(AsynchronousSocketChannel client, Attachment attach) {
    try {
      // Get the client addressSocketAddress clientAddr = client.getRemoteAddress();
      System.out.format("Accepted a connection from %s%n", clientAddr);

      // Accept another connection
      attach.server.accept(attach, this);

      // Handle the client connection by using an asyn read
      ReadWriteHandler rwHandler = new ReadWriteHandler();
      Attachment newAttach = new Attachment();
      newAttach.server = attach.server;
      newAttach.client = client;
      newAttach.buffer = ByteBuffer.allocate(2048);
      newAttach.isRead = true;
      newAttach.clientAddr = clientAddr;
      client.read(newAttach.buffer, newAttach, rwHandler);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  @Overridepublicvoid failed(Throwable e, Attachment attach) {
    System.out.println("Failed to accept a connection.");
    e.printStackTrace();
  }
}

class ReadWriteHandler implementsCompletionHandler<Integer, Attachment> {
  @Overridepublicvoid completed(Integer result, Attachment attach) {
    if (result == -1) {
      try {
        attach.client.close();
        System.out.format("Stopped listening to the client %s%n", attach.clientAddr);
      } catch (IOException ex) {
        ex.printStackTrace();
      }
      return;
    }

    if (attach.isRead) {
      attach.buffer.flip();

      int limits = attach.buffer.limit();
      byte bytes[] = newbyte[limits];
      attach.buffer.get(bytes, 0, limits);
      Charset cs = Charset.forName("UTF-8");
      String msg = newString(bytes, cs);

      System.out.format("Client at %s says: %s%n", attach.clientAddr, msg);

      attach.isRead = false; // It is a write

      attach.buffer.rewind();
      attach.client.write(attach.buffer, attach, this);
    } else {
      attach.isRead = true;
      attach.buffer.clear();
      attach.client.read(attach.buffer, attach, this);
    }
  }

  @Overridepublicvoid failed(Throwable e, Attachment attach) {
    e.printStackTrace();
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    try (AsynchronousServerSocketChannel server = AsynchronousServerSocketChannel.open()) {
      String host = "localhost";
      int port = 8989;
      InetSocketAddress sAddr = newInetSocketAddress(host, port);
      server.bind(sAddr);

      System.out.format("Server is listening at %s%n", sAddr);

      Attachment attach = new Attachment();
      attach.server = server;

      // Accept new connections
      server.accept(attach, new ConnectionHandler());
      try {
        // Wait until the main thread is interruptedThread.currentThread().join();
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}

class Attachment {
  AsynchronousServerSocketChannel server;
  AsynchronousSocketChannel client;
  ByteBuffer buffer;
  SocketAddress clientAddr;
  boolean isRead;
}
```

PreviousNext

## Related

- Java AsynchronousFileChannel read from file
- Java AsynchronousFileChannel with custom CompletionHandler
- Java AsynchronousFileChannel use Future object
- Java AsynchronousServerSocketChannel create server
- Java AsynchronousServerSocketChannel get supported options
