---
title: Get Cookie value and set cookie value
nav: Get Cookie value and set c...
description: client.getParams().setParameter("http.useragent", "My Browser");
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20061026233630/http://www.java2s.com/Code/Java/Apache-Common/GetCookievalueandsetcookievalue.htm
---
Get Cookie value and set cookie value

```java title=Example.java
import org.apache.commons.httpclient.Cookie;
import org.apache.commons.httpclient.HttpState;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
public class GetCookiePrintAndSetValue {
  public static void main(String args[]) throws Exception {
    HttpClient client = new HttpClient();
    client.getParams().setParameter("http.useragent", "My Browser");
    GetMethod method = new GetMethod("http://localhost:8080/");
    try{
      client.executeMethod(method);
      Cookie[] cookies = client.getState().getCookies();
      for (int i = 0; i < cookies.length; i++) {
        Cookie cookie = cookies[i];
        System.err.println(
          "Cookie: " + cookie.getName() +
          ", Value: " + cookie.getValue() +
          ", IsPersistent?: " + cookie.isPersistent() +
          ", Expiry Date: " + cookie.getExpiryDate() +
          ", Comment: " + cookie.getComment());
        cookie.setValue("My own value");
      }
      client.executeMethod(method);
    } catch(Exception e) {
      System.err.println(e);
    } finally {
      method.releaseConnection();
    }
  }
}
```

Download: GetCookiePrintAndSetValue.zip ( 328 K )
---
Related examples in the same category
1. Get Http methods
2. Get Http client parameters
4. Http Client Simple Demo
5. Get allowed http methods
11. Using Http Client Inside Thread
