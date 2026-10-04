---
title: Returning a reference to an inner class
nav: Returning a reference to a...
description: Imported from the java2s.com archive: Returning a reference to an inner class
section: Imported - java2s Archive
order: 1274
source: https://web.archive.org/web/20140829090928/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Returningareferencetoaninnerclass.htm
---
```java title=Example.java
class MyClass {
  private class ClassB implements B {
    private int i = 11;
    public int value() {
      return i;
    }
  }
  protected class ClassA implements A {
    private String label;
    private ClassA(String whereTo) {
      label = whereTo;
    }
    public String readLabel() {
      return label;
    }
  }
  public A dest(String s) {
    return new ClassA(s);
  }
  public B cont() {
    return new ClassB();
  }
}
public class MainClass {
  public static void main(String[] args) {
    MyClass p = new MyClass();
    B c = p.cont();
    A d = p.dest("A");
  }
}
interface B {
  int value();
}
interface A {
  String readLabel();
}
```
