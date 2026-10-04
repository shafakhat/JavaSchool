---
title: static section Initializer and logic
nav: static section Initializer...
description: Imported from the java2s.com archive: static section Initializer and logic
section: Imported - java2s Archive
order: 1210
source: https://web.archive.org/web/20140829082604/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/staticsectionInitializerandlogic.htm
---
```java title=Example.java
public class ClassInitializer6 {
  static int classField = 3;
  static {
    System.out.println(" : " + classField);
    classField = 1;
    for (int i = 2; i < 6; i++)
      classField *= i;
  }
  static {
    System.out.println(" = " + classField);
  }
  public static void main(String[] args) {
    System.out.println(classField);
  }
}
```
