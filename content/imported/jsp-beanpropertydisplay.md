---
title: Bean property display
nav: Bean property display
description: <strong>SMTP host: </strong><c:out value="${emailer.smtpHost}" /><br />
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20060829134528/http://www.java2s.com:80/Code/Java/JSP/Beanpropertydisplay.htm
---
```java title=Example.java
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<jsp:useBean id="emailer" class="com.java2s.EmailBean"/>
<jsp:setProperty name="emailer" property="*" />
<html>
<head><title>Bean property display</title></head>
<body>
<h2>Here are the EmailBean properties</h2>
<strong>SMTP host: </strong><c:out value="${emailer.smtpHost}" /><br />
<strong>Email recipient: </strong><c:out value="${emailer.to}" /><br />
<strong>Email sender: </strong><c:out value="${emailer.from}" /><br />
<strong>Email subject: </strong><c:out value="${emailer.subject}" /><br />
<strong>Email content: </strong><c:out value="${emailer.content}" /><br />
</body>
</html>
```

Related examples in the same category
---
1. Calling a Private Method
2. Jsp Form And Bean
3. Get Set Properties JSTL
4. Getting a Property Value
5. Using a Constructor
6. Using Bean Counter JSP
7. Using a Java Bean Jsp
8. Using Package Jsp
9. Using UseBean in Jsp
10. Set Property Value
11. Jsp Using Bean Scope Session
12. Beans with scriptlet
13. EL and Complex JavaBeans
14. JSP with Java bean
15. JSP form and Java beans
16. JSP email valid check
17. JSP and Java beans 3
18. JSP Standard Actions: set property
19. JSP and Java beans (JavaBeans) 1
20. JSP and Java beans (JavaBeans) 2
