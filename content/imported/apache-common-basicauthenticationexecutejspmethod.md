---
title: Basic Authentication Execute JSP Method
nav: Basic Authentication Execu...
description: GetMethod method = new GetMethod("/commons/folder/protected.jsp");
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20061026233605/http://www.java2s.com/Code/Java/Apache-Common/BasicAuthenticationExecuteJSPMethod.htm
---
```java title=Example.java
import org.apache.commons.httpclient.URI;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.HostConfiguration;
public class BasicAuthenticationExecuteJSPMethod {
  public static void main(String args[]) throws Exception {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("parameterKey", "value");
    HostConfiguration host = client.getHostConfiguration();
    host.setHost(new URI("http://localhost:8080", true));
    GetMethod method = new GetMethod("/commons/folder/protected.jsp");
    try{
      client.executeMethod(host, method);
      System.err.println(method.getStatusLine());
      System.err.println(method.getResponseBodyAsString());
    } catch(Exception e) {
      System.err.println(e);
    } finally {
      method.releaseConnection();
    }
  }
}
```

Download: BasicAuthenticationExecuteJSPMethod.zip ( 328 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
4. Http Client Simple Demo
5. Get allowed http methods
11. Using Http Client Inside Thread
