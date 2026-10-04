---
title: Auto-unboxing
nav: Auto-unboxing
description: Imported from the java2s.com archive: Auto-unboxing
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autounboxingmixdifferenttypesofnumericobjectsinanexpression.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Integer intObject = 100;;
    Double doubleObject = 98.6;
    doubleObject = doubleObject + intObject;
    System.out.println("dOb after expression: " + doubleObject);
  }
}
java title=Example.java
dOb after expression: 198.6
```
