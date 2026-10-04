---
title: Nesting a class within a scope.
nav: Nesting a class within a s...
description: Imported from the java2s.com archive: Nesting a class within a scope.
section: Imported - java2s Archive
order: 1271
source: https://web.archive.org/web/20140829090615/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Nestingaclasswithinascope.htm
---
```java title=Example.java
public class MainClass {
  private void method(boolean b) {
    if (b) {
      class A {
        private String id;
        A(String s) {
          id = s;
        }
        String getSlip() {
          return id;
        }
      }
      A ts = new A("slip");
      String s = ts.getSlip();
    }
    // Can't use it here! Out of scope:
    // ! A ts = new A("x");
  }
  public void track() {
    method(true);
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    p.track();
  }
}
```
