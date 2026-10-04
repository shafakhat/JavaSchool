---
title: Java Networking
nav: Networking
description: TCP sockets, HTTP clients and URL handling in Java - with working client/server examples.
section: Advanced Java
order: 10
---

## The networking stack

Java ships a complete networking API in `java.net` (and `java.net.http` since Java 11):

| Task | API |
|---|---|
| Raw TCP client/server | `Socket` / `ServerSocket` |
| UDP datagrams | `DatagramSocket` |
| Read a URL | `URL`, `URLConnection` |
| Modern HTTP | `java.net.http.HttpClient` (Java 11+) |
| URI handling | `java.net.URI` |

## A TCP server and client

The server listens; the client connects, sends a line, reads the reply:

```java title=TcpServer.java
import java.io.*;
import java.net.*;

public class TcpServer {
    public static void main(String[] args) throws IOException {
        try (ServerSocket server = new ServerSocket(9090)) {
            System.out.println("listening on 9090...");
            while (true) {
                try (Socket client = server.accept();            // blocks until a client connects
                     BufferedReader in = new BufferedReader(
                         new InputStreamReader(client.getInputStream()));
                     PrintWriter out = new PrintWriter(client.getOutputStream(), true)) {

                    String line = in.readLine();                 // client sent this
                    System.out.println("received: " + line);
                    out.println("echo: " + line.toUpperCase());  // reply
                }
            }
        }
    }
}
```

```java title=TcpClient.java
import java.io.*;
import java.net.*;

public class TcpClient {
    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket("localhost", 9090);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()))) {

            out.println("hello server");
            System.out.println(in.readLine());    // echo: HELLO SERVER
        }
    }
}
```

Run the server first, then the client. Key points:

- `accept()` **blocks** until someone connects - in real servers it runs on a thread pool.
- Always close sockets with try-with-resources.
- `PrintWriter(..., true)` enables auto-flush (otherwise messages sit in the buffer).

> **Warning:** `readLine()` returns `null` when the peer closes the connection - don't loop on it blindly or you'll spin forever.

## Modern HTTP client (Java 11+)

```java title=HttpDemo.java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HttpDemo {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        // GET
        HttpRequest get = HttpRequest.newBuilder()
            .uri(URI.create("https://httpbin.org/get?lang=java"))
            .header("Accept", "application/json")
            .GET()
            .build();
        HttpResponse<String> res = client.send(get, HttpResponse.BodyHandlers.ofString());
        System.out.println("status = " + res.statusCode());
        System.out.println(res.body().substring(0, Math.min(120, res.body().length())));

        // POST JSON
        HttpRequest post = HttpRequest.newBuilder()
            .uri(URI.create("https://httpbin.org/post"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString("{\"name\":\"Ada\"}"))
            .build();
        HttpResponse<String> res2 = client.send(post, HttpResponse.BodyHandlers.ofString());
        System.out.println("post status = " + res2.statusCode());
    }
}
```

Features worth knowing:

- `send` is synchronous; `sendAsync(...).thenApply(...)` is non-blocking.
- HTTP/2 is negotiated automatically (fall back to 1.1).
- Body handlers: `ofString()`, `ofInputStream()`, `ofByteArray()`.

## Reading a URL the classic way

```java title=UrlRead.java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class UrlRead {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://httpbin.org/robots.txt");
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(url.openStream()))) {
            String line;
            int n = 0;
            while ((line = br.readLine()) != null && n++ < 5) {
                System.out.println(line);
            }
        }
    }
}
```

For anything beyond trivial use, prefer `HttpClient` - it handles cookies, timeouts and HTTP/2 properly.

## UDP in 20 lines

```java title=Udp.java
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Udp {
    public static void main(String[] args) throws Exception {
        // server-ish side
        try (DatagramSocket socket = new DatagramSocket(9999)) {
            byte[] buf = new byte[256];
            DatagramPacket packet = new DatagramPacket(buf, buf.length);
            socket.receive(packet);                       // blocks
            String msg = new String(packet.getData(), 0, packet.getLength());
            System.out.println("got: " + msg);

            byte[] reply = ("pong from " + msg).getBytes();
            DatagramPacket out = new DatagramPacket(
                reply, reply.length, packet.getAddress(), packet.getPort());
            socket.send(out);
        }
    }

    // client: new DatagramSocket().send(...) with InetAddress.getByName("localhost")
    static void ping() throws Exception {
        try (DatagramSocket socket = new DatagramSocket()) {
            byte[] data = "ping".getBytes();
            DatagramPacket p = new DatagramPacket(
                data, data.length, InetAddress.getByName("localhost"), 9999);
            socket.send(p);
        }
    }
}
```

UDP is connectionless: no guarantees on order or delivery - use TCP unless you truly need speed over reliability (games, metrics, streaming).

## Timeouts and good manners

```java title=Timeouts.java
import java.net.Socket;

public class Timeouts {
    public static void main(String[] args) throws Exception {
        try (Socket s = new Socket()) {
            s.connect(new java.net.InetSocketAddress("example.com", 80), 3000); // 3s connect
            s.setSoTimeout(2000);   // 2s read timeout -> SocketTimeoutException
            System.out.println("connected: " + s.isConnected());
        }
    }
}
```

Always set connect/read timeouts - a production service without them hangs forever on a dead peer.

Next: [Regular Expressions](regex.html) or [Reflection](reflection.html).
