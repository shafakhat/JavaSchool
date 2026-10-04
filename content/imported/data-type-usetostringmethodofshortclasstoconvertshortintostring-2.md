---
title: Use toString method of Short class to convert Short into String.
nav: Use toString method of Sho...
description: Imported from the java2s.com archive: Use toString method of Short class to convert Short into String.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20101020202412/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/UsetoStringmethodofShortclasstoconvertShortintoString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    short s = 10;
    Short sObj = new Short(s);
    String str = sObj.toString();
    System.out.println(str);
  }
}
```
