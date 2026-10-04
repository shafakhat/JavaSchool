---
title: A demonstration of abstract.
nav: A demonstration of abstract.
description: Imported from the java2s.com archive: A demonstration of abstract.
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20140829074955/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Ademonstrationofabstract.htm
---
```java title=Example.java
abstract class A {
  abstract void callme();
  void callmetoo() {
    System.out.println("This is a concrete method.");
  }
}
class B extends A {
  void callme() {
    System.out.println("B's implementation of callme.");
  }
}
class AbstractDemo {
  public static void main(String args[]) {
    B b = new B();
    b.callme();
    b.callmetoo();
  }
}
```

| 5.28.1. | Abstract Classes |
|---|---|
| 5.28.2. | A demonstration of abstract. |
| 5.28.3. | Using abstract methods and classes. |
