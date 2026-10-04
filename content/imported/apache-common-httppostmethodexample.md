---
title: Http post method Example
nav: Http post method Example
description: client.getParams().setParameter("http.useragent", "Test Client");
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20060822142759/http://www.java2s.com:80/Code/Java/Apache-Common/HttppostmethodExample.htm
---
Http post method Example

```java title=Example.java
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.methods.PostMethod;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class PostMethodExample {
  public static void main(String args[]) {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "Test Client");
    BufferedReader br = null;
    PostMethod method = new PostMethod("http://search.yahoo.com/search");
    method.addParameter("p", "\"java2s\"");
    try{
      int returnCode = client.executeMethod(method);
      if(returnCode == HttpStatus.SC_NOT_IMPLEMENTED) {
        System.err.println("The Post method is not implemented by this URI");
        // still consume the response body
        method.getResponseBodyAsString();
      } else {
        br = new BufferedReader(new InputStreamReader(method.getResponseBodyAsStream()));
        String readLine;
        while(((readLine = br.readLine()) != null)) {
          System.err.println(readLine);
      }
      }
    } catch (Exception e) {
      System.err.println(e);
    } finally {
      method.releaseConnection();
      if(br != null) try { br.close(); } catch (Exception fe) {}
    }
  }
}
```

Download: PostMethodExample.zip ( 336 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
3. Execute Http method (post/get)
4. Http Client Simple Demo
5. Get allowed http methods
6. Connect Method Example For Proxy Client
7. Basic Authentication Execute JSP Method
8. Basic Authentication For JSP Page
9. Basic Authentication Get JSP Method Return Code
10. Get Cookie value and set cookie value
11. Using Http Client Inside Thread
