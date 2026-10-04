---
title: is White space
nav: is White space
description: space (' '), tab ('\t'), newline ('\n'), carriage return ('\r'),form feed ('\f')
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/isWhitespace.htm
---
isWhitespace():true if the argument is whitespace.

which is any one of the following characters:

space (' '), tab ('\t'), newline ('\n'), carriage return ('\r'),form feed ('\f')

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    char symbol = 'A';
    if (Character.isWhitespace(symbol)) {
      System.out.println("true");
    }else{
      System.out.println("false");
    }
  }
}
java title=Example.java
false
```
