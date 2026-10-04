---
title: Http Client Simple Demo
nav: Http Client Simple Demo
description: Imported from the java2s.com archive: Http Client Simple Demo
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20061026233635/http://www.java2s.com/Code/Java/Apache-Common/HttpClientSimpleDemo.htm
---
```java title=Example.java
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
public class HttpClientTest {
 public static void main(String args[]) throws Exception {
      HttpClient client = new HttpClient();
      GetMethod method = new GetMethod("http://www.google.com");
      int returnCode = client.executeMethod(method);
      System.err.println(method.getResponseBodyAsString());
      method.releaseConnection();
 }
}
```

Related examples in the same category
---
1. Get Http methods
2. Get Http client parameters
4. Get allowed http methods
11. Using Http Client Inside Thread
