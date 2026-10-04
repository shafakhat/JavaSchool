---
title: Auto-unboxing allows you to mix different types of numeric objects in an expression.
nav: Auto-unboxing allows you t...
description: Imported from the java2s.com archive: Auto-unboxing allows you to mix different types of numeric objects in an expression.
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autounboxingallowsyoutomixdifferenttypesofnumericobjectsinanexpression.htm
---
```java title=Example.java
class AutoBox4 {
  publicstaticvoid main(String args[]) {

    Integer iOb = 100;
    Double dOb = 98.6;

    dOb = dOb + iOb;
    System.out.println("dOb after expression: " + dOb);
  }
}
```
