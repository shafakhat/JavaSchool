---
title: Calling a Private Method
nav: Calling a Private Method
description: The message is: <jsp:getProperty name="bean1" property="message" />
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20061026215614/http://www.java2s.com/Code/Java/JSP/CallingaPrivateMethod.htm
---
Calling a Private Method

```java title=Example.java
// JSP file
<HTML>
    <HEAD>
        <TITLE>Calling a Private Method</TITLE>
    </HEAD>
    <BODY>
        <H1>Calling a Private Method</H1>
        <jsp:useBean id="bean1" class="beans.Message" />
        The message is: <jsp:getProperty name="bean1" property="message" />
        <BR>
        <jsp:setProperty name="bean1" property="message" value="Hello again!" />
        Now the message is: <jsp:getProperty name="bean1" property="message" />
    </BODY>
</HTML>
///////////////////////////////////////
//Java Source Code
package beans;
import java.io.Serializable;
public class Message implements Serializable
{
    private String message = "Hello from JSP!";
    public void setMessage(String m)
    {
        this.message = m;
    }
    public String getMessage()
    {
        return privateMessage();
    }
    private String privateMessage()
    {
        return this.message;
    }
    public Message()
    {
    }
}
```

Download: CallAPrivateMethod.zip ( 89 K )
---
Related examples in the same category
11. Bean property display
12. Beans with scriptlet
13. EL and Complex JavaBeans
14. JSP with Java bean
15. JSP form and Java beans
16. JSP email valid check
17. JSP and Java beans 3
