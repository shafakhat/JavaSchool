---
title: Initialization order
nav: Initialization order
description: Imported from the java2s.com archive: Initialization order
section: Imported - java2s Archive
order: 1254
source: https://web.archive.org/web/20140829084353/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Initializationorder.htm
---
```java title=Example.java
class MyClass {
  MyClass(int marker) {
    System.out.println("Tag(" + marker + ")");
  }
}
class MyInit {
  MyClass t1 = new MyClass(1); // Before constructor
  MyInit() {
    System.out.println("Card()");
    t3 = new MyClass(33);
  }
  MyClass t2 = new MyClass(2); // After constructor
  void f() {
    System.out.println("f()");
  }
  MyClass t3 = new MyClass(3); // At end
}
public class MainClass {
  public static void main(String[] args) {
    MyInit t = new MyInit();
    t.f();
  }
}
java title=Example.java
Tag(1)
Tag(2)
Tag(3)
Card()
Tag(33)
f()
```
