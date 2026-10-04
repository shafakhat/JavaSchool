---
title: Defining references to inner classes
nav: Defining references to inn...
description: Imported from the java2s.com archive: Defining references to inner classes
section: Imported - java2s Archive
order: 1269
source: https://web.archive.org/web/20140829090644/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Definingreferencestoinnerclasses.htm
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
  public B to(String s) {
    return new B(s);
  }
  public A cont() {
    return new A();
  }
  public void ship(String dest) {
    A c = cont();
    B d = to(dest);
    System.out.println(d.readLabel());
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    p.ship("A");
    MainClass q = new MainClass();
    MainClass.A c = q.cont();
    MainClass.B d = q.to("A");
  }
}
```
