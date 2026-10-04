---
title: Construct string from subset of char array.
nav: Construct string from subs...
description: Imported from the java2s.com archive: Construct string from subset of char array.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Constructstringfromsubsetofchararray.htm
---
```java title=Example.java
class SubStringCons {
  publicstaticvoid main(String args[]) {
    byte ascii[] = { 65, 66, 67, 68, 69, 70 };

    String s1 = new String(ascii);
    System.out.println(s1);

    String s2 = new String(ascii, 2, 3);
    System.out.println(s2);
  }
}
```
