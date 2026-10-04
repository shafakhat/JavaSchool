---
title: Extracting Characters From a Mutable String
nav: Extracting Characters From...
description: StringBuffer phrase = new StringBuffer("one two three four");
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20070329224151/http://www.java2s.com:80/Tutorial/Java/0120__Development/ExtractingCharactersFromaMutableStringcharAtandgetCharsmethods.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer phrase = new StringBuffer("one two three four");
    System.out.println(phrase.charAt(5));
    char[] textArray = new char[3];
    phrase.getChars(9, 12, textArray, 0);
    for(char ch: textArray){
      System.out.println(ch);
    }
  }
}
```

```java title=Example.java
w
h
r
e
```
