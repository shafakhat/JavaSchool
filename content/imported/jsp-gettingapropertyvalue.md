---
title: Getting a Property Value
nav: Getting a Property Value
description: The message is: <jsp:getProperty name="bean1" property="message" />
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20061026220011/http://www.java2s.com/Code/Java/JSP/GettingaPropertyValue.htm
---
```java title=Example.java
//File: index.jsp
<HTML>
  <HEAD>
    <TITLE>Getting a Property Value</TITLE>
  </HEAD>
  <BODY>
    <H1>Getting a Property Value</H1>
    <jsp:useBean id="bean1" class="beans.Message" />
    The message is: <jsp:getProperty name="bean1" property="message" />
  </body>
</html>
////////////////////////////////////////////
//Java Bean Class
package beans;
public class Message
{
    private String message = "Hello from JSP!";
    public String getMessage()
    {
        return message;
    }
    public Message()
    {
    }
}
```

Download: GetAPropertyValue.zip ( 89 K )
---
Related examples in the same category
11. Bean property display
12. Beans with scriptlet
13. EL and Complex JavaBeans
14. JSP with Java bean
15. JSP form and Java beans
16. JSP email valid check
17. JSP and Java beans 3
