---
title: Creating instances of inner classes
nav: Creating instances of inne...
description: Imported from the java2s.com archive: Creating instances of inner classes
section: Imported - java2s Archive
order: 1265
source: https://web.archive.org/web/20140829090540/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Creatinginstancesofinnerclasses.htm
---
```java title=Example.java
public class MainClass {
  class A {
    private int i = 11;
    public int value() {
      return i;
    }
  }
  class B {
    private String label;
    B(String whereTo) {
      label = whereTo;
    }
    String readLabel() {
      return label;
    }
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    // Must use instance of outer class
    // to create an instances of the inner class:
    MainClass.A c = p.new A();
    MainClass.B d = p.new B("A");
  }
}
```
