---
title: Methods with differing type signatures are overloaded - not overridden.
nav: Methods with differing typ...
description: Imported from the java2s.com archive: Methods with differing type signatures are overloaded - not overridden.
section: Imported - java2s Archive
order: 1206
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Methodswithdifferingtypesignaturesareoverloadednotoverridden.htm
---
```java title=Example.java
class A {
  int i, j;
  A(int a, int b) {
    i = a;
    j = b;
  }
  void show() {
    System.out.println("i and j: " + i + " " + j);
  }
}
class B extends A {
  int k;
  B(int a, int b, int c) {
    super(a, b);
    k = c;
  }
  void show(String msg) {
    System.out.println(msg + k);
  }
}
class Override {
  public static void main(String args[]) {
    B subOb = new B(1, 2, 3);
    subOb.show("This is k: "); // this calls show() in B
    subOb.show(); // this calls show() in A
  }
}
```
