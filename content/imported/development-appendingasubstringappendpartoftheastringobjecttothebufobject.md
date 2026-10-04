---
title: Appending a Substring
nav: Appending a Substring
description: Imported from the java2s.com archive: Appending a Substring
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20070329230315/http://www.java2s.com:80/Tutorial/Java/0120__Development/AppendingaSubstringappendpartoftheaStringobjecttothebufobject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer buf = new StringBuffer("1234567890");
    String aString = "abcdefghijk";
    buf.append(aString, 3, 4);
    System.out.println(buf);
  }
}
java title=Example.java
1234567890d
```
