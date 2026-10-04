---
title: Use a generic toString()
nav: Use a generic toString()
description: 1. ShowToString -- demo program to show default toString methods
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20090531211331/http://www.java2s.com:80/Code/Java/Class/UseagenerictoString.htm
---
Use a generic toString()

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

1.  ShowToString -- demo program to show default toString methods
---  ---
2.  ToString -- demo program to show a toString method
3.  Demonstrate toString() without an override
4.  To String Demo
5.  Reflection based toString() utilities
