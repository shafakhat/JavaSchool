---
title: To unbox an object
nav: To unbox an object
description: Simply assign that object reference to a variable of its corresponding primitive type
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Tounboxanobject.htm
---
Simply assign that object reference to a variable of its corresponding primitive type

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Integer iOb = 100; // autobox an int
int i = iOb; // auto-unbox
    System.out.println(i + " " + iOb);
  }
}
```
