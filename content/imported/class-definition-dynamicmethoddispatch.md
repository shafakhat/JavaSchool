---
title: Dynamic Method Dispatch
nav: Dynamic Method Dispatch
description: Imported from the java2s.com archive: Dynamic Method Dispatch
section: Imported - java2s Archive
order: 1474
source: https://web.archive.org/web/20140829082456/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DynamicMethodDispatch.htm
---
```java title=Example.java
class A {
  void callme() {
    System.out.println("Inside A's callme method");
  }
}
class B extends A {
  void callme() {
    System.out.println("Inside B's callme method");
  }
}
class C extends A {
  void callme() {
    System.out.println("Inside C's callme method");
  }
}
class Dispatch {
  public static void main(String args[]) {
    A a = new A(); // object of type A
    B b = new B(); // object of type B
    C c = new C(); // object of type C
    A r; // obtain a reference of type A
    r = a; // r refers to an A object
    r.callme(); // calls A's version of callme
    r = b; // r refers to a B object
    r.callme(); // calls B's version of callme
    r = c; // r refers to a C object
    r.callme(); // calls C's version of callme
  }
}
```

| 5.24.1. | Polymorphism |
|---|---|
| 5.24.2. | An example of polymorphism |
| 5.24.3. | Downcasting and Run-Time Type Identification (RTTI) |
| 5.24.4. | Constructors and polymorphism don't produce what you might expect |
| 5.24.5. | Dynamic Method Dispatch |
| 5.24.6. | Using run-time polymorphism. |
