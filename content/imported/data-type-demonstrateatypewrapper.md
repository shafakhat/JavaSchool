---
title: Demonstrate a type wrapper.
nav: Demonstrate a type wrapper.
description: Imported from the java2s.com archive: Demonstrate a type wrapper.
section: Imported - java2s Archive
order: 1113
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Demonstrateatypewrapper.htm
---
```java title=Example.java
class Wrap {
  public static void main(String args[]) {
    Integer iOb = new Integer(100);
    int i = iOb.intValue();
    System.out.println(i + " " + iOb); // displays 100 100
  }
}
```
