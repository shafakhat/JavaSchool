---
title: Appending a subset of the elements from a char array
nav: Appending a subset of the ...
description: char[] text = { 'i', 's', ' ', 'e', 'x', 'a', 'c', 't', 'l', 'y'};
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20070329234004/http://www.java2s.com:80/Tutorial/Java/0120__Development/Appendingasubsetoftheelementsfromachararray.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer buf = new StringBuffer("::");
    char[] text = { 'i', 's', ' ', 'e', 'x', 'a', 'c', 't', 'l', 'y'};
    buf.append(text, 2, 8);
    System.out.println(buf);
  }
}
```

```java title=Example.java
:: exactly
```
