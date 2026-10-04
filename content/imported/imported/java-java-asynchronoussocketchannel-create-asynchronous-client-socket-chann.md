---
title: Java AsynchronousSocketChannel create asynchronous client socket channel
nav: Java AsynchronousSocketCha...
description: Java AsynchronousSocketChannel create asynchronous client socket channel
section: Imported
order: 20038
source: http://www.java2s.com/ref/java/java-asynchronoussocketchannel-create-asynchronous-client-socket-chann.html
---
- java.nio.channels
- java.nio.channels AsynchronousFileChannel AsynchronousServerSocketChannel AsynchronousSocketChannel CompletionHandler DatagramChannel FileChannel FileLock ReadableByteChannel SeekableByteChannel Selector

## Description

Java AsynchronousSocketChannel create asynchronous client socket channel

```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.CompletionHandler;
import java.nio.charset.Charset;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

class Attachment {
  AsynchronousSocketChannel channel;
  ByteBuffer buffer;//fromwww.java2s.comThread mainThread;
  boolean isRead;
}

class ReadWriteHandler implementsCompletionHandler<Integer, Attachment> {
  @Overridepublicvoid completed(Integer result, Attachment attach) {
    if (attach.isRead) {
      attach.buffer.flip();

      // Get the text read from the serverCharset cs = Charset.forName("UTF-8");

      int limits = attach.buffer.limit();
      byte bytes[] = newbyte[limits];
      attach.buffer.get(bytes, 0, limits);
      String msg = newString(bytes, cs);

      System.out.println("Server Responded:"+ msg);

      msg = this.getTextFromUser();
      if (msg.equalsIgnoreCase("bye")) {
        attach.mainThread.interrupt();
        return;
      }
      attach.buffer.clear();
      byte[] data = msg.getBytes(cs);
      attach.buffer.put(data);

      attach.buffer.flip();

      attach.isRead = false;

      attach.channel.write(attach.buffer, attach, this);
    } else {
      attach.isRead = true;

      attach.buffer.clear();

      attach.channel.read(attach.buffer, attach, this);
    }
  }

  @Overridepublicvoid failed(Throwable e, Attachment attach) {
    e.printStackTrace();
  }

  privateString getTextFromUser() {
    System.out.print("Please enter a message (Bye to quit):");
    String msg = null;

    BufferedReader consoleReader = newBufferedReader(newInputStreamReader(System.in));
    try {
      msg = consoleReader.readLine();
    } catch (IOException e) {
      e.printStackTrace();
    }

    return msg;
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    try (AsynchronousSocketChannel channel = AsynchronousSocketChannel.open()) {
      String serverName = "localhost";
      int serverPort = 8989;
      SocketAddress serverAddr = newInetSocketAddress(serverName, serverPort);

      Future<Void> result = channel.connect(serverAddr);
      System.out.println("Connecting to the server...");

      result.get();

      System.out.println("Connected to the server...");

      Attachment attach = new Attachment();
      attach.channel = channel;
      attach.buffer = ByteBuffer.allocate(2048);
      attach.isRead = false;
      attach.mainThread = Thread.currentThread();

      // Place the "Hello" message in the bufferCharset cs = Charset.forName("UTF-8");
      String msg = "Hello";
      byte[] data = msg.getBytes(cs);
      attach.buffer.put(data);
      attach.buffer.flip();

      // Write to the server
      ReadWriteHandler readWriteHandler = new ReadWriteHandler();
      channel.write(attach.buffer, attach, readWriteHandler);

      // Let this thread wait for ever on its own death until interrupted
      attach.mainThread.join();
    } catch (ExecutionException | IOException e) {
      e.printStackTrace();
    } catch (InterruptedException e) {
      System.out.println("Disconnected from the server.");
    }
  }
}
```

PreviousNext

## Related

- Java AsynchronousServerSocketChannel read object from client
- Java AsynchronousServerSocketChannel send object
- Java AsynchronousServerSocketChannel use Future object in a server
- Java AsynchronousSocketChannel create client
- Java AsynchronousSocketChannel send object
