---
title: Tokenizing a String
nav: Tokenizing a String
description: String[] words = text.split("[, .]", 0); // Delimiters are comma, space, or period
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/TokenizingaString.htm
---
```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
    String text = "to be or not to be, that is the question.";
    String[] words = text.split("[, .]", 0); // Delimiters are comma, space, or period
 for(String s: words){
      System.out.println(s);
    }
  }
}
java title=Example.java
to
be
or
not
to
be
that
is
the
question
```
