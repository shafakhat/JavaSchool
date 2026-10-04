---
title: Overloading a base-class method name in a derived class does not hide the base-class versions.
nav: Overloading a base-class m...
description: Imported from the java2s.com archive: Overloading a base-class method name in a derived class does not hide the base-class versions.
section: Imported - java2s Archive
order: 1291
source: https://web.archive.org/web/20140829075549/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Overloadingabaseclassmethodnameinaderivedclassdoesnothidethebaseclassversions.htm
---
```java title=Example.java
class A {
  char doh(char c) {
    System.out.println("doh(char)");
    return 'd';
  }
  float doh(float f) {
    System.out.println("doh(float)");
    return 1.0f;
  }
}
class B {}
class C extends A {
  void doh(B m) {
    System.out.println("doh(B)");
  }
}
public class MainClass {
  public static void main(String[] args) {
    C b = new C();
    b.doh(1);
    b.doh('x');
    b.doh(1.0f);
    b.doh(new B());
  }
}
java title=Example.java
doh(float)
doh(char)
doh(float)
doh(B)
```
