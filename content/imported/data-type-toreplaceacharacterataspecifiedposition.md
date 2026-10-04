---
title: To replace a character at a specified position
nav: To replace a character at ...
description: publicstatic String replaceCharAt(String s, int pos, char c) {
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toreplaceacharacterataspecifiedposition.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
     String str = "this is a test";
     System.out.println(replaceCharAt(str, 5, 'c'));
  }
  publicstatic String replaceCharAt(String s, int pos, char c) {
    return s.substring(0, pos) + c + s.substring(pos + 1);
  }
}
//this cs a test
```
