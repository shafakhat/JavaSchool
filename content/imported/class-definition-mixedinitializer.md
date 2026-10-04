---
title: Mixed Initializer
nav: Mixed Initializer
description: Imported from the java2s.com archive: Mixed Initializer
section: Imported - java2s Archive
order: 1256
source: https://web.archive.org/web/20140829084652/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MixedInitializer.htm
---
```java title=Example.java
public class MixedInitializer {
  int i1;
  static int i2;
  int i3 = 2;
  static int i4 = 4;
  {
    System.out.println("i1 = " + i1);
    i1 = 6;
    System.out.println("i1 = 6");
  }
  static {
    System.out.println("i2 = " + i2);
    i2 = 8;
    System.out.println("i2 = 8");
  }
  public static void main(String[] args) {
    System.out.println("main() entered");
    MixedInitializer mi = new MixedInitializer();
    System.out.println("mi.i1 = " + mi.i1);
    System.out.println("i2 = " + i2);
    System.out.println("mi.i3 = " + mi.i3);
    System.out.println("i4 = " + i4);
    System.out.println("main() exited");
  }
  {
    i1 += 6;
    System.out.println("6 + i1");
  }
  static {
    i2 -= 3;
    System.out.println("i2 -= 3");
  }
}
```
