---
title: Demonstrate when constructors are called in a Multilevel Hierarchy
nav: Demonstrate when construct...
description: Imported from the java2s.com archive: Demonstrate when constructors are called in a Multilevel Hierarchy
section: Imported - java2s Archive
order: 1294
source: https://web.archive.org/web/20140829075552/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DemonstratewhenconstructorsarecalledinaMultilevelHierarchy.htm
---
```java title=Example.java
class A {
  A() {
    System.out.println("Inside A's constructor.");
  }
}
class B extends A {
  B() {
    System.out.println("Inside B's constructor.");
  }
}
class C extends B {
  C() {
    System.out.println("Inside C's constructor.");
  }
}
class CallingCons {
  public static void main(String args[]) {
    C c = new C();
  }
}
```
