---
title: Nested classes can access all members of all levels of the classes they are nested within
nav: Nested classes can access ...
description: Imported from the java2s.com archive: Nested classes can access all members of all levels of the classes they are nested within
section: Imported - java2s Archive
order: 1272
source: https://web.archive.org/web/20140829090609/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Nestedclassescanaccessallmembersofalllevelsoftheclassestheyarenestedwithin.htm
---
```java title=Example.java
class MyClass {
  private void f() {}
  class A {
    private void g() {}
    public class B {
      void h() {
        g();
        f();
      }
    }
  }
}
public class MainClass {
  public static void main(String[] args) {
    MyClass a = new MyClass();
    MyClass.A innerA = a.new A();
    MyClass.A.B innerb = innerA.new B();
    innerb.h();
  }
}
```
