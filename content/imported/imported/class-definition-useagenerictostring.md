---
title: Use a generic toString()
nav: Use a generic toString()
description: Imported from the java2s.com archive: Use a generic toString()
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20101027013124/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/UseagenerictoString.htm
---
```java title=Example.java
import java.lang.reflect.Field;
public class Main {
  public static void main(String args[]) {
    System.out.println(new MyClass().toString());
  }
}
class MyClass {
  String hello = "hi";
  int i = 0;
  public String toString() {
    StringBuilder sb = new StringBuilder();
    Class cls = getClass();
    Field[] f = cls.getDeclaredFields();
    for (int i = 0; i < f.length; i++) {
      f[i].setAccessible(true);
      try {
        sb.append(f[i].getName()+"="+ f[i].get(this)+"\n");
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
    if (cls.getSuperclass().getSuperclass() != null) {
      sb.append("super:"+ super.toString()+"\n");
    }
    return cls.getName()+"\n" + sb.toString();
  }
}
```
