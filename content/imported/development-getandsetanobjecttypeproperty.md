---
title: Get and set an Object type property
nav: Get and set an Object type...
description: Expression expr = new Expression(o, "getProp1", new Object[0]);
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20100624051709/http://www.java2s.com:80/Tutorial/Java/0120__Development/GetandsetanObjecttypeproperty.htm
---
```java title=Example.java
import java.beans.Expression;
import java.beans.Statement;
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new MyBean();
    // Get the value of prop1
    Expression expr = new Expression(o, "getProp1", new Object[0]);
    expr.execute();
    String s = (String) expr.getValue();
    // Set the value of prop1
    Statement stmt = new Statement(o, "setProp1", new Object[] { "new string" });
    stmt.execute();
  }
}
class MyBean {
  String prop1;
  public String getProp1() {
    return prop1;
  }
  public void setProp1(String s) {
    prop1 = s;
  }
  int prop2;
  public int getProp2() {
    return prop2;
  }
  public void setProp2(int i) {
    prop2 = i;
  }
  byte[] prop3;
  public byte[] getProp3() {
    return prop3;
  }
  public void setProp3(byte[] bytes) {
    prop3 = bytes;
  }
}
```
