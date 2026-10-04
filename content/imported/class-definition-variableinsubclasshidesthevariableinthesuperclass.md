---
title: Variable in subclass hides the variable in the super class
nav: Variable in subclass hides...
description: 5.23.1. Variable in subclass hides the variable in the super class
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Variableinsubclasshidesthevariableinthesuperclass.htm
---
```java title=Example.java
class A {
  int i;
}
class B extends A {
  int i; // this i hides the i in A
  B(int a, int b) {
    super.i = a; // i in A
    i = b; // i in B
  }
  void show() {
    System.out.println("i in superclass: " + super.i);
    System.out.println("i in subclass: " + i);
  }
}
class UseSuper {
  public static void main(String args[]) {
    B subOb = new B(1, 2);
    subOb.show();
  }
}
```

5.23.1.  Variable in subclass hides the variable in the super class
