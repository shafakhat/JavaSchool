---
title: Use a generic constructor.
nav: Use a generic constructor.
description: Imported from the java2s.com archive: Use a generic constructor.
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20090227183655/http://www.java2s.com:80/Code/Java/Generics/Useagenericconstructor.htm
---
Use a generic constructor.

```java title=Example.java
class GenCons {
  private double val;
  <T extends Number> GenCons(T arg) {
    val = arg.doubleValue();
  }
  void showval() {
    System.out.println("val: " + val);
  }
}
public class GenConsDemo {
  public static void main(String args[]) {
    GenCons test = new GenCons(100);
    GenCons test2 = new GenCons(123.5F);
    test.showval();
    test2.showval();
  }
}
```
