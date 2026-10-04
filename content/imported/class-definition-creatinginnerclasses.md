---
title: Creating inner classes
nav: Creating inner classes
description: Imported from the java2s.com archive: Creating inner classes
section: Imported - java2s Archive
order: 1281
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Creatinginnerclasses.htm
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
  // Using inner classes looks just like
 // using any other class, within MainClass:
 public void ship(String dest) {
    A c = new A();
    B d = new B(dest);
    System.out.println(d.readLabel());
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    p.ship("AAA");
  }
}
```
