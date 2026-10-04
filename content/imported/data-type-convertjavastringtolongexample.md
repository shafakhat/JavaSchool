---
title: Convert Java String to Long example
nav: Convert Java String to Lon...
description: Imported from the java2s.com archive: Convert Java String to Long example
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20090912060545/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConvertJavaStringtoLongexample.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Long lObj1 = new Long("100");
    System.out.println(lObj1);
    String str = "100";
    Long lObj2 = Long.valueOf(str);
    System.out.println(lObj2);
  }
}
```
