---
title: String concatenation
nav: String concatenation
description: String myString = numHands + " " + secondString + thirdString;
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringconcatenationConvertanintegertoStringandjoinwithtwootherstrings.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
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
