---
title: A string can be compared with a StringBuffer
nav: A string can be compared w...
description: Imported from the java2s.com archive: A string can be compared with a StringBuffer
section: Imported - java2s Archive
order: 1149
source: https://web.archive.org/web/20090526042229/http://www.java2s.com:80/Code/Java/Data-Type/AstringcanbecomparedwithaStringBuffer.htm
---
A string can be compared with a StringBuffer

```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    String s1 = "s1";
    StringBuffer sbuf = new StringBuffer("a");
    boolean b = s1.contentEquals(sbuf);
  }
}
```

1.  How to compare String instances
---  ---
2.  String.compareTo
3.  Check order of two strings
4.  Check order of two strings ignoring case
5.  Compare Strings
6.  Comparing Strings
