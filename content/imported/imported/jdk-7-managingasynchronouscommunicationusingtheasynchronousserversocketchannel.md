---
title: Managing asynchronous communication using the AsynchronousServerSocketChannel
nav: Managing asynchronous comm...
description: Managing asynchronous communication using the AsynchronousServerSocketChannel
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20130622125757/http://www.java2s.com:80/Code/Java/JDK-7/ManagingasynchronouscommunicationusingtheAsynchronousServerSocketChannel.htm
---
```java title=Example.java
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousSocketChannel;
import java.util.Scanner;
import java.util.concurrent.Future;
public class Test {
  public static void main(String[] args) throws Exception {
    AsynchronousSocketChannel client = AsynchronousSocketChannel.open();
    InetSocketAddress address = new InetSocketAddress("localhost", 5000);
    Future<Void> future = client.connect(address);
    System.out.println("Client: Waiting for the connection to complete");
    future.get();
    String message = "";
    while (!message.equals("quit")) {
      System.out.print("Enter a message: ");
      Scanner scanner = new Scanner(System.in);
      message = scanner.nextLine();
      System.out.println("Client: Sending ...");
      ByteBuffer buffer = ByteBuffer.wrap(message.getBytes());
      System.out.println("Client: Message sent: " + new String(buffer.array()));
      client.write(buffer);
    }
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
7.  Communication with AsynchronousSocketChannel
