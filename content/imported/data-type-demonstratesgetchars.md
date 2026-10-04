---
title: demonstrates getChars( )
nav: demonstrates getChars( )
description: Imported from the java2s.com archive: demonstrates getChars( )
section: Imported - java2s Archive
order: 1162
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/demonstratesgetChars.htm
---
```java title=Example.java
class getCharsDemo {
  public static void main(String args[]) {
    String s = "This is a demo of the getChars method.";
    int start = 10;
    int end = 14;
    char buf[] = new char[end - start];
    s.getChars(start, end, buf, 0);
    System.out.println(buf);
  }
}
```
