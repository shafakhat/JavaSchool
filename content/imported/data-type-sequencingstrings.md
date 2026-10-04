---
title: Sequencing Strings
nav: Sequencing Strings
description: Imported from the java2s.com archive: Sequencing Strings
section: Imported - java2s Archive
order: 1110
source: https://web.archive.org/web/20070328230522/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/SequencingStrings.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String string1 = "abcde";
    String string2 = "bcdef";
    if(string1.compareTo(string2) > 0) {
      System.out.println("greater");
    }
    if(string1.compareTo(string2) == 0) {
      System.out.println("equal");
    }
    if(string1.compareTo(string2) < 0) {
      System.out.println("less");
    }
  }
}
```

```java title=Example.java
less
```
