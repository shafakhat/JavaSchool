---
title: Adding Members to an Enumeration Class
nav: Adding Members to an Enume...
description: small(36), medium(40), large(42), extra_large(46), extra_extra_large(48);
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20070428024431/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/AddingMemberstoanEnumerationClass.htm
---
```java title=Example.java
enum JacketSize {
  small(36), medium(40), large(42), extra_large(46), extra_extra_large(48);
  JacketSize(int chestSize) {
    this.chestSize = chestSize;
  }
  public int chestSize() {
    return chestSize;
  }
  private int chestSize;
}
class Jacket {
  public Jacket(JacketSize size) {
    this.size = size;
  }
  public String toString() {
    switch (this.size) {
    case small:
      return "S";
    case medium:
      return "M";
    case large:
      return "L";
    case extra_large:
      return "XL";
    case extra_extra_large:
      return "XXL";
    default:
      return "";
    }
  }
  private JacketSize size;
}
public class MainClass {
  public static void main(String[] args) {
    Jacket[] jackets = { new Jacket(JacketSize.medium),
                         new Jacket(JacketSize.extra_large),
                         new Jacket(JacketSize.small),
                         new Jacket(JacketSize.extra_extra_large) };
    System.out.println("\n\nJackets sizes available are:\n");
    for (JacketSize size : JacketSize.values()) {
      System.out.print(" " + size);
    }
    System.out.println("\n\nJackets in stock are:");
    for (Jacket jacket : jackets) {
      System.out.println(jacket);
    }
  }
}
java title=Example.java
Jackets sizes available are:
 small medium large extra_large extra_extra_large
Jackets in stock are:
M
XL
S
XXL
```
