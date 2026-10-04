---
title: gets and sets a primitive type property
nav: gets and sets a primitive ...
description: Expression expr = new Expression(o, "getProp2", new Object[0]);
section: Imported
order: 20030
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/getsandsetsaprimitivetypeproperty.htm
---
```java title=Example.java
import java.beans.Expression;
import java.beans.Statement;
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new MyBean();
    // Get the value of prop2
    Expression expr = new Expression(o, "getProp2", new Object[0]);
    expr.execute();
    int i = ((Integer) expr.getValue()).intValue();
    // Set the value of prop2
    Statement stmt = new Statement(o, "setProp2", new Object[] { new Integer(123) });
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
