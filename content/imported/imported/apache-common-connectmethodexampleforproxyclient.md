---
title: Connect Method Example For Proxy Client
nav: Connect Method Example For...
description: import org.apache.commons.httpclient.ProxyClient.ConnectResponse;
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20061026233617/http://www.java2s.com/Code/Java/Apache-Common/ConnectMethodExampleForProxyClient.htm
---
```java title=Example.java
import org.apache.commons.httpclient.ProxyClient;
import org.apache.commons.httpclient.ConnectMethod;
import org.apache.commons.httpclient.ProxyClient.ConnectResponse;
import java.net.Socket;
public class ConnectMethodExampleForProxyClient {
  public static void main(String args[]) {
    ProxyClient client = new ProxyClient();
    client.getParams().setParameter("http.useragent","Proxy Test Client");
    client.getHostConfiguration().setHost("www.somehost.com");
    client.getHostConfiguration().setProxy("localproxyaddress",80);
    Socket socket = null;
    try{
      ConnectResponse response = client.connect();
      socket = response.getSocket();
      if(socket == null) {
        ConnectMethod method = response.getConnectMethod();
        System.err.println("Socket not created: " + method.getStatusLine());
      }
      // do something
    } catch (Exception e) {
      System.err.println(e);
    } finally {
      if(socket != null)
          try {
              socket.close();
          } catch (Exception fe) {}
    }
  }
}
```

Download: ConnectMethodExampleForProxyClient.zip ( 328 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
4. Http Client Simple Demo
5. Get allowed http methods
11. Using Http Client Inside Thread
