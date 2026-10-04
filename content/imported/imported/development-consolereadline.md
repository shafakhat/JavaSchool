---
title: Console.ReadLine
nav: Console.ReadLine
description: System.err.println("Unable to create server socket: " + ioe);
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20110130081232/http://java2s.com:80/Tutorial/Java/0120__Development/ConsoleReadLine.htm
---
```java title=Example.java
import java.io.Console;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.MessageFormat;
import java.util.Date;
import java.util.Locale;
public class DateServer {
  public final static int PORT = 5000;
  private ServerSocket ss;
  public DateServer(int port) {
    try {
      ss = new ServerSocket(port);
    } catch (IOException ioe) {
      System.err.println("Unable to create server socket: " + ioe);
      System.exit(1);
    }
  }
  private void runServer() {
    Console console = System.console();
    Handler h = new Handler(ss);
    h.start();
    while (true) {
      String cmd = console.readLine(">");
      if (cmd == null)
        continue;
      if (cmd.equals("exit"))
        System.exit(0);
    }
  }
  public static void main(String[] args) {
    new DateServer(PORT).runServer();
  }
}
class Handler extends Thread {
  private ServerSocket ss;
  Handler(ServerSocket ss) {
    this.ss = ss;
  }
  public void run() {
    while (true) {
      try {
        Socket s = ss.accept();
        ObjectInputStream ois;
        ois = new ObjectInputStream(s.getInputStream());
        Locale l = (Locale) ois.readObject();
        PrintWriter pw;
        pw = new PrintWriter(s.getOutputStream());
        MessageFormat mf;
        mf = new MessageFormat("The date is {0, date, long}", l);
        Object[] args = { new Date() };
        pw.println(mf.format(args));
        pw.close();
      } catch (Exception e) {
        System.err.println(e);
      }
    }
  }
}
```
