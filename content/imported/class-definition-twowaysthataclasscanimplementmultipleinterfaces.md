---
title: Two ways that a class can implement multiple interfaces
nav: Two ways that a class can ...
description: Imported from the java2s.com archive: Two ways that a class can implement multiple interfaces
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20070709034118/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Twowaysthataclasscanimplementmultipleinterfaces.htm
---
```java title=Example.java
interface A {
}
interface B {
}
class X implements A, B {
}
class Y implements A {
  B makeB() {
    // Anonymous inner class:
    return new B() {
    };
  }
}
public class MainClass {
  static void takesA(A a) {
  }
  static void takesB(B b) {
  }
  public static void main(String[] args) {
    X x = new X();
    Y y = new Y();
    takesA(x);
    takesA(y);
    takesB(x);
    takesB(y.makeB());
  }
}
```
