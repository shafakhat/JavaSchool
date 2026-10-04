---
title: Static field, constructor and exception
nav: Static field, constructor ...
description: Imported from the java2s.com archive: Static field, constructor and exception
section: Imported - java2s Archive
order: 1214
source: https://web.archive.org/web/20140829084055/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Staticfieldconstructorandexception.htm
---
```java title=Example.java
public class Main {
  static Bar bar;
  static {
    try {
      bar = new Bar();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  public static void main(String[] argv) {
    System.out.println(bar);
  }
}
class Bar {
  public Bar() throws Exception {
  }
  public String toString() {
    return "Bar";
  }
}
```
