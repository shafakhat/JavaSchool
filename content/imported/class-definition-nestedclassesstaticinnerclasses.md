---
title: Nested classes (static inner classes)
nav: Nested classes (static inn...
description: Imported from the java2s.com archive: Nested classes (static inner classes)
section: Imported - java2s Archive
order: 1289
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Nestedclassesstaticinnerclasses.htm
---
```java title=Example.java
public class MainClass {
  private static class ClassA implements A {
    private int i = 11;
    public int value() {
      return i;
    }
  }
  protected static class ClassB implements B {
    private String label;
    private ClassB(String whereTo) {
      label = whereTo;
    }
    public String readLabel() {
      return label;
    }
    // Nested classes can contain other static elements:
 public static void f() {
    }
    static int x = 10;
    static class InnerInnerClass {
      public static void f() {
      }
      static int x = 10;
    }
  }
  public static B dest(String s) {
    return new ClassB(s);
  }
  public static A cont() {
    return new ClassA();
  }
  public static void main(String[] args) {
    A c = cont();
    B d = dest("A");
  }
}
interface A {
  int value();
}
interface B {
  String readLabel();
}
```
