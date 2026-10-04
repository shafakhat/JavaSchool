---
title: Execute Http method (post/get)
nav: Execute Http method (post/...
description: System.err.println("The User Agent before changing it is: " + client.getParams().getParameter("http.useragent"));
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20061026233639/http://www.java2s.com/Code/Java/Apache-Common/ExecuteHttpmethodpostget.htm
---
```java title=Example.java
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HostConfiguration;
import org.apache.commons.httpclient.methods.GetMethod;
public class HttpClientPreferences {
 public static void main(String args[]) throws Exception {
      HttpClient client = new HttpClient();
      System.err.println("The User Agent before changing it is: " + client.getParams().getParameter("http.useragent"));
      client.getParams().setParameter("http.useragent","Browser at Client level");
      System.err.println("Client's User Agent is: " + client.getParams().getParameter("http.useragent"));
      GetMethod method = new GetMethod("http://www.google.com");
      method.getParams().setParameter("http.useragent","Browser at Method level");
      try{
          client.executeMethod(method);
      }catch(Exception e) {
          System.err.println(e);
      }finally {
          method.releaseConnection();
      }
      System.err.println("Method's User Agent is: " +  method.getParams().getParameter("http.useragent"));
 }
}
```

Download: HttpClientPreferences.zip ( 336 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
3. Http Client Simple Demo
4. Get allowed http methods
11. Using Http Client Inside Thread
