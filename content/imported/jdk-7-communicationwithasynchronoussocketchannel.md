---
title: Communication with AsynchronousSocketChannel
nav: Communication with Asynchr...
description: InetSocketAddress hostAddress = new InetSocketAddress(InetAddress.getByName("127.0.0.1"),
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20130622144858/http://www.java2s.com:80/Code/Java/JDK-7/CommunicationwithAsynchronousSocketChannel.htm
---
```java title=Example.java
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.channels.AsynchronousServerSocketChannel;
import java.nio.channels.AsynchronousSocketChannel;
import java.nio.channels.Channels;
import java.util.concurrent.Future;
public class Test {
  private static void clientStart() {
    try {
      InetSocketAddress  hostAddress = new InetSocketAddress(InetAddress.getByName("127.0.0.1"),
          2583);
      AsynchronousSocketChannel clientSocketChannel = AsynchronousSocketChannel
          .open();
      Future<Void> connectFuture = clientSocketChannel.connect(hostAddress);
      connectFuture.get(); // Wait until connection is done.
      OutputStream os = Channels.newOutputStream(clientSocketChannel);
      ObjectOutputStream oos = new ObjectOutputStream(os);
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
  private static void serverStart() {
    try {
      InetSocketAddress  hostAddress = new InetSocketAddress(InetAddress.getByName("127.0.0.1"),
          2583);
      AsynchronousServerSocketChannel serverSocketChannel = AsynchronousServerSocketChannel
          .open().bind(hostAddress);
      Future<AsynchronousSocketChannel> serverFuture = serverSocketChannel
          .accept();
      final AsynchronousSocketChannel clientSocket = serverFuture.get();
      if ((clientSocket != null) && (clientSocket.isOpen())) {
        InputStream connectionInputStream = Channels
            .newInputStream(clientSocket);
        ObjectInputStream ois = null;
        ois = new ObjectInputStream(connectionInputStream);
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
  public static void main(String[] args) throws Exception{
    Thread serverThread = new Thread(new Runnable() {
      @Override
      public void run() {
        serverStart();
      }
    });
    serverThread.start();
    Thread clientThread = new Thread(new Runnable() {
      @Override
      public void run() {
        clientStart();
      }
    });
    clientThread.start();
 }
}
```

1.  Using AsynchronousFileChannel and Future to read
---  ---
2.  Using AsynchronousFileChannel and CompletionHandler to read a file
3.  Writing to a file using the AsynchronousFileChannel class
4.  Using AsynchronousFileChannel to write ByteBuffer and return Future
5.  Reading from a file using the AsynchronousFileChannel class
6.  Reading from a file using the AsynchronousFileChannel class
7.  Managing asynchronous communication using the AsynchronousServerSocketChannel
