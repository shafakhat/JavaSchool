---
title: Calling append() method to construct a StringBuffer object
nav: Calling append() method to...
description: proverb.append("A").append("B").append("C").append("D").append("E");
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070329220021/http://www.java2s.com:80/Tutorial/Java/0120__Development/CallingappendmethodtoconstructaStringBufferobject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer proverb = new StringBuffer(); // Capacity is 16
    proverb.append("A").append("B").append("C").append("D").append("E");
    System.out.println(proverb);
  }
}
java title=Example.java
ABCDE
```
