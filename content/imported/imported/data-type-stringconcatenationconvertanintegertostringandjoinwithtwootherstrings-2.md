---
title: String concatenation
nav: String concatenation
description: String myString = numHands + " " + secondString + thirdString;
section: Imported - java2s Archive
order: 1208
source: https://web.archive.org/web/20070328185948/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/StringconcatenationConvertanintegertoStringandjoinwithtwootherstrings.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int numHands = 99;
    String secondString = "secondString";
    String thirdString = "thirdString";
    String myString = numHands + " " + secondString + thirdString;
    System.out.println(myString);
  }
}
```

```java title=Example.java
99 secondStringthirdString
```
