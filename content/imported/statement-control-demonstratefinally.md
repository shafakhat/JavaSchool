---
title: Demonstrate finally.
nav: Demonstrate finally.
description: Imported from the java2s.com archive: Demonstrate finally.
section: Imported - java2s Archive
order: 1194
source: https://web.archive.org/web/20140829080159/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Demonstratefinally.htm
---
```java title=Example.java
class FinallyDemo {
  static void procA() {
    try {
      System.out.println("inside procA");
      throw new RuntimeException("demo");
    } finally {
      System.out.println("procA's finally");
    }
  }
  static void procB() {
    try {
      System.out.println("inside procB");
      return;
    } finally {
      System.out.println("procB's finally");
    }
  }
  static void procC() {
    try {
      System.out.println("inside procC");
    } finally {
      System.out.println("procC's finally");
    }
  }
  public static void main(String args[]) {
    try {
      procA();
    } catch (Exception e) {
      System.out.println("Exception caught");
    }
    procB();
    procC();
  }
}
```
