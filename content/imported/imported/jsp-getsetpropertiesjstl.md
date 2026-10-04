---
title: Get Set Properties JSTL
nav: Get Set Properties JSTL
description: I have a <jsp:getProperty name="myCar" property="make" /> <br />
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20061026215655/http://www.java2s.com/Code/Java/JSP/GetSetPropertiesJSTL.htm
---
```java title=Example.java
//File: index.jsp
<html>
    <head>
        <title>Using a JavaBean</title>
    </head>
    <body>
    <h2>Using a JavaBean</h2>
    <jsp:useBean id="myCar" class="beans.CarBean" />
    I have a <jsp:getProperty name="myCar" property="make" /> <br />
    <jsp:setProperty name="myCar" property="make" value="Ferrari" />
    Now I have a <jsp:getProperty name="myCar" property="make" />
    </body>
</html>
//////////////////////////////////////////////////////////////
//Java Bean
package beans;
import java.io.Serializable;
public class CarBean implements Serializable
{
  private String make = "Company";
  private double cost = 100.00;
  private double taxRate = 17.5;
  public CarBean() {}
  public String getMake()
  {
    return make;
  }
  public void setMake(String make)
  {
    this.make = make;
  }
  public double getPrice()
  {
    double price = (cost + (cost * (taxRate/100)));
    return price;
  }
}
```

Download: GetSetPropertiesJSTL.zip ( 89 K )
---
Related examples in the same category
11. Bean property display
12. Beans with scriptlet
13. EL and Complex JavaBeans
14. JSP with Java bean
15. JSP form and Java beans
16. JSP email valid check
17. JSP and Java beans 3
