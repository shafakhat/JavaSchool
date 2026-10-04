---
title: Construct one String from another.
nav: Construct one String from ...
description: Imported from the java2s.com archive: Construct one String from another.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConstructoneStringfromanother.htm
---
```java title=Example.java
class MakeString {
  publicstaticvoid main(String args[]) {
    char c[] = { 'J', 'a', 'v', 'a' };
    String s1 = new String(c);
    String s2 = new String(s1);
    System.out.println(s1);
    System.out.println(s2);
  }
}
```
