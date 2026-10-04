---
title: Overloading a base-class method name in a derived class does not hide the base-class versions
nav: Overloading a base-class m...
description: Overloading a base-class method name in a derived class does not hide the base-class versions
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20090327130642/http://www.java2s.com:80/Code/Java/Class/Overloadingabaseclassmethodnameinaderivedclassdoesnothidethebaseclassversions.htm
---
Overloading a base-class method name in a derived class does not hide the base-class versions

```java title=Example.java
// : c06:Hide.java
// Overloading a base-class method name in a derived class does not hide the base-class versions.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Homer {
  char doh(char c) {
    System.out.println("doh(char)");
    return 'd';
  }
  float doh(float f) {
    System.out.println("doh(float)");
    return 1.0f;
  }
}
class Milhouse {
}
class Bart extends Homer {
  void doh(Milhouse m) {
    System.out.println("doh(Milhouse)");
  }
}
public class Hide {
  public static void main(String[] args) {
    Bart b = new Bart();
    b.doh(1);
    b.doh('x');
    b.doh(1.0f);
    b.doh(new Milhouse());
  }
} ///:~
```

1.  Demonstration of both constructor and ordinary method overloading
---  ---
2.  Overloaded constructor
3.  Overloaded method
4.  Demonstration of overriding fields
5.  Overloading based on the order of the arguments
6.  Promotion of primitives and overloading
7.  Demotion of primitives and overloading
