---
title: Explicit static initialization with the static clause
nav: Explicit static initializa...
description: Imported from the java2s.com archive: Explicit static initialization with the static clause
section: Imported - java2s Archive
order: 1268
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Explicitstaticinitializationwiththestaticclause.htm
---
```java title=Example.java
class MyClass {
  MyClass(int marker) {
    System.out.println("Cup(" + marker + ")");
  }
  void f(int marker) {
    System.out.println("f(" + marker + ")");
  }
}
class MyStatic {
  static MyClass c1;
  static MyClass c2;
  static {
    c1 = new MyClass(1);
    c2 = new MyClass(2);
  }
  MyStatic() {
    System.out.println("Cups()");
  }
}
public class MainClass {
  public static void main(String[] args) {
    System.out.println("Inside main()");
    MyStatic.c1.f(99); // (1)
  }
}
java title=Example.java
Inside main()
Cup(1)
Cup(2)
f(99)
```
