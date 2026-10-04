---
title: Nesting a class within a method
nav: Nesting a class within a m...
description: Imported from the java2s.com archive: Nesting a class within a method
section: Imported - java2s Archive
order: 1267
source: https://web.archive.org/web/20140829090945/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Nestingaclasswithinamethod.htm
---
```java title=Example.java
public class MainClass {
  public A dest(String s) {
    class B implements A {
      private String label;
      private B(String whereTo) {
        label = whereTo;
      }
      public String readLabel() {
        return label;
      }
    }
    return new B(s);
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    A d = p.dest("A");
  }
}
interface A {
  String readLabel();
}
```
