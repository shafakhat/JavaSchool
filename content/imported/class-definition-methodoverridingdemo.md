---
title: Method overriding Demo
nav: Method overriding Demo
description: Imported from the java2s.com archive: Method overriding Demo
section: Imported - java2s Archive
order: 1198
source: https://web.archive.org/web/20140829082407/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MethodoverridingDemo.htm
---
```java title=Example.java
class A {
  int i, j;
  A(int a, int b) {
    i = a;
    j = b;
  }
  // display i and j
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
  void show() {
    System.out.println("k: " + k);
  }
}
class Override {
  public static void main(String args[]) {
    B subOb = new B(1, 2, 3);
    subOb.show(); // this calls show() in B
  }
}
```
