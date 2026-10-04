---
title: Get Http client parameters
nav: Get Http client parameters
description: client.getParams().setParameter("http.useragent", "My Browser");
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20061026233648/http://www.java2s.com/Code/Java/Apache-Common/GetHttpclientparameters.htm
---
```java title=Example.java
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpVersion;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.HostConfiguration;
public class HttpClientParameter {
  public static void main(String args[]) throws Exception {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "My Browser");
    HostConfiguration host = client.getHostConfiguration();
    host.setHost("www.google.com");
    GetMethod method = new GetMethod("http://www.yahoo.com");
    int returnCode = client.executeMethod(host, method);
    System.err.println(method.getResponseBodyAsString());
    System.err.println("User-Agent: " + method.getHostConfiguration().getParams().getParameter("http.useragent"));
    System.err.println("User-Agent: " + method.getParams().getParameter("http.useragent"));
    method.releaseConnection();
  }
}
```

Related examples in the same category
---
1. Get Http methods
3. Http Client Simple Demo
4. Get allowed http methods
11. Using Http Client Inside Thread
