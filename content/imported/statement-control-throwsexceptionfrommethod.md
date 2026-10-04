---
title: throws Exception from method
nav: throws Exception from method
description: Imported from the java2s.com archive: throws Exception from method
section: Imported - java2s Archive
order: 1189
source: https://web.archive.org/web/20140829085252/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/throwsExceptionfrommethod.htm
---
```java title=Example.java
class ThrowsDemo {
  static void throwOne() throws IllegalAccessException {
    System.out.println("Inside throwOne.");
    throw new IllegalAccessException("demo");
  }
  public static void main(String args[]) {
    try {
      throwOne();
    } catch (IllegalAccessException e) {
      System.out.println("Caught " + e);
    }
  }
}
```
