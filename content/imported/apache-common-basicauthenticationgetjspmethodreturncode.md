---
title: Basic Authentication Get JSP Method Return Code
nav: Basic Authentication Get J...
description: import org.apache.commons.httpclient.UsernamePasswordCredentials;
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20061026233613/http://www.java2s.com/Code/Java/Apache-Common/BasicAuthenticationGetJSPMethodReturnCode.htm
---
```java title=Example.java
import org.apache.commons.httpclient.URI;
import org.apache.commons.httpclient.HttpState;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.Credentials;
import org.apache.commons.httpclient.auth.AuthScope;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.HostConfiguration;
import org.apache.commons.httpclient.UsernamePasswordCredentials;
public class BasicAuthenticationGetJSPMethodReturnCode {
  public static void main(String args[]) throws Exception {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "My Browser");
    HostConfiguration host = client.getHostConfiguration();
    host.setHost(new URI("http://localhost:8080", true));
    GetMethod method = new GetMethod("/commons/folder/protected.jsp");
    try{
      int statusCode = client.executeMethod(host, method);
      if(statusCode == HttpStatus.SC_UNAUTHORIZED) {
        System.err.println("Authorization required by server");
        Credentials credentials =new UsernamePasswordCredentials("tomcat", "tomcat");
        AuthScope authScope = new AuthScope(host.getHost(), host.getPort());
        HttpState state = client.getState();
        state.setCredentials(authScope, credentials);
        client.executeMethod(host, method);
      }
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

Download: BasicAuthenticationGetJSPMethodReturnCode.zip ( 329 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
4. Http Client Simple Demo
5. Get allowed http methods
11. Using Http Client Inside Thread
