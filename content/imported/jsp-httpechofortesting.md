---
title: HTTP Echo For testing : Java examples (example source code) » JSP » JSP Debug
nav: HTTP Echo For testing : Ja...
description: private Socket createClientSocket(String host, int portNum) {
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20060513072242/http://www.java2s.com/Code/Java/JSP/HTTPEchoFortesting.htm
---
HTTP Echo For testing

```java title=Example.java
import java.net.Socket;
import java.net.ServerSocket;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.BufferedInputStream;
public class HTTPEcho {
   private static final int BUF_SIZE = 1024;
   private Socket browserSocket = null;
   private Socket webServerSocket = null;
   private ServerSocket browserListenerSocket = null;
   private OutputStream toWebServer = null;
   private BufferedInputStream fromWebServer = null;
   private OutputStream toBrowser = null;
   private BufferedInputStream fromBrowser = null;
   private ServerSocket createListenerSocket(int portNum)  {
      ServerSocket socket = null;
      try  {
         socket = new ServerSocket(portNum);
      }
      catch (IOException ioe)  {
         System.out.println(ioe.getMessage());
         System.exit(-1);
      }
      return socket;
   }
   private Socket createClientSocket(String host, int portNum)  {
      Socket socket = null;
      try  {
         socket = new Socket(host, portNum);
         toWebServer = socket.getOutputStream();
         fromWebServer =
            new BufferedInputStream(socket.getInputStream());
      }
      catch (IOException ioe)  {
         System.out.println(ioe.getMessage());
         System.exit(-1);
      }
      return socket;
   }
   private Socket accept ()  {
      Socket socket = null;
      try {
         socket = browserListenerSocket.accept();
         toBrowser = socket.getOutputStream();
         fromBrowser =
            new BufferedInputStream(socket.getInputStream());
      }
      catch (IOException e) {
         System.out.println("Accept failed: " +  e.getMessage());
         System.exit(-1);
      }
      return socket;
   }
   private void setBrowserListenerSocket(ServerSocket socket)  {
      browserListenerSocket = socket;
   }
   private void setWebServerSocket(Socket socket)  {
      webServerSocket = socket;
   }
   private void setBrowserSocket(Socket socket)  {
      browserSocket = socket;
   }
   private int readLine(InputStream in, byte[] b, int off, int len) throws IOException {
      if (len <= 0) {
         return 0;
      }
      int count = 0, c;
      while ((c = in.read()) != -1 && count < len) {
         b[off++] = (byte)c;
         count++;
         if (c == '\n') {
            break;
         }
      }
      return count > 0 ? count : -1;
   }
   private void echoBuffer(BufferedInputStream in, OutputStream out)  {
      byte[] readBuf = new byte[BUF_SIZE];
      try  {
         int rlen = -1;
         int bodyLen = 0;
         String line = null;
         do  {
            line = null;
            rlen = readLine(in, readBuf, 0, BUF_SIZE);
            if (rlen > 0)  {
               line = new String(readBuf, 0, rlen);
               System.out.print(line);
               if (line.startsWith("Content-Length: ")) {
                  String size =
                     line.substring("Content-Length: ".length(),
                                    line.length());
                  bodyLen = Integer.parseInt(size.trim());
               }
               out.write(readBuf, 0, rlen);
            }
         } while ((rlen > 0) && !(line.equals("\r\n")));
         if (bodyLen > 0) {
            System.out.println("<Entity-Body>");
            int count = 0;
            do  {
               rlen = in.read(readBuf, 0, BUF_SIZE);
               if (rlen > 0)  {
                  out.write(readBuf, 0, rlen);
                  count += rlen;
               }else break;
            } while (count < bodyLen);
         }
         out.flush();
      }
      catch (IOException ioe)  {
         System.out.println(ioe.getMessage());
      }
      finally  {
         readBuf = null;
      }
   }
   private void echo()  {
      System.out.println("\nHTTP REQUEST:");
      echoBuffer(fromBrowser, toWebServer);
      System.out.println("\nHTTP REPLY:");
      echoBuffer(fromWebServer, toBrowser);
   }
   private void closeClientDescriptors()  {
      try  {
         fromWebServer.close();
         toWebServer.close();
         webServerSocket.close();
         fromBrowser.close();
         toBrowser.close();
         browserSocket.close();
      }
      catch (IOException ioe)  {
         System.out.println(ioe.getMessage());
      }
   }
   public static void main(String [] args) {
      HTTPEcho echo = new HTTPEcho();
      if (args.length > 1)  {
         System.out.println("Starting HTTPEcho on port: " + args[0] + ". ");
         System.out.println("Web server host: " + args[1] + ".");
         System.out.println("Web server is on port: " + args[2] + ".");
      int interceptorPort = Integer.parseInt(args[0]);
      String webServerHost = args[1];
      int webServerPort = Integer.parseInt(args[2]);
      echo.setBrowserListenerSocket(echo.createListenerSocket(interceptorPort));
         while (true)  {
            echo.setBrowserSocket(echo.accept());
            echo.setWebServerSocket(echo.createClientSocket(webServerHost,
                                    webServerPort));
            echo.echo();
            echo.closeClientDescriptors();
         }
      }
      else {
         System.out.println("Usage: java HTTPEcho " +
                            "interceptorPort " +
                            "webServerHost webServerPort");
      }
   }
}
```

Related examples in the same category
---
1. Mainline for the HTTP tracer tool
2. A command-line interface to a Web server
