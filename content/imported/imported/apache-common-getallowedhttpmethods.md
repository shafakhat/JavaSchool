---
title: Get allowed http methods
nav: Get allowed http methods
description: client.getParams().setParameter("http.useragent", "Test Client");
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20061026233622/http://www.java2s.com/Code/Java/Apache-Common/Getallowedhttpmethods.htm
---
Get allowed http methods

```java title=Example.java
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.methods.OptionsMethod;
import java.util.Enumeration;
public class OptionsMethodExample {
  public static void main(String args[]) {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "Test Client");
    OptionsMethod method = new OptionsMethod("http://www.google.com");
    try{
      int returnCode = client.executeMethod(method);
      Enumeration list = method.getAllowedMethods();
      while(list.hasMoreElements()) {
        System.err.println(list.nextElement());
          }
    } catch (Exception e) {
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
11. Using Http Client Inside Thread
