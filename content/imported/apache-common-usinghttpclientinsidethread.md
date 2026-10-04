---
title: Using Http Client Inside Thread
nav: Using Http Client Inside T...
description: client.getParams().setParameter("http.useragent", "Test Client");
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20061026233609/http://www.java2s.com/Code/Java/Apache-Common/UsingHttpClientInsideThread.htm
---
Using Http Client Inside Thread

```java title=Example.java
import org.apache.commons.httpclient.URI;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.HostConfiguration;
public class UsingHttpClientInsideThread {
  public static void main(String args[]) throws Exception {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "Test Client");
    HostConfiguration host = new HostConfiguration();
    host.setHost(new URI("http://localhost:8080", true));
    // first Get a big file
    MethodThread bigDataThread =  new MethodThread(client, host, "/big_movie.wmv");
    bigDataThread.start();
    // next try and get a small file
    MethodThread normalThread = new MethodThread(client, host, "/");
    normalThread.start();
  }
}
class MethodThread extends Thread {
  private HttpClient client;
  private HostConfiguration host;
  private GetMethod method;
  public MethodThread(HttpClient client, HostConfiguration host, String resource) {
    this.client = client;
    this.host = host;
    this.method = new GetMethod(resource);
  }
  public void run() {
    System.err.println("Connecting to: " + host);
    try{
      client.executeMethod(host, method);
      method.getResponseBodyAsStream();
    } catch(Exception e) {
      System.err.println(e);
    } finally {
      method.releaseConnection();
    }
  }
}
```

Related examples in the same category
---
1. Get Http methods
2. Get Http client parameters
4. Http Client Simple Demo
5. Get allowed http methods
