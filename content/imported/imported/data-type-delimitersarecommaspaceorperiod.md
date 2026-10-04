---
title: Delimiters are comma, space, or period
nav: Delimiters are comma, spac...
description: String delimiters = "[, .]"; // Delimiters are comma, space, and period
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20070328231934/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Delimitersarecommaspaceorperiod.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String text = "To be or not to be, that is the question.";
    String delimiters = "[, .]"; // Delimiters are comma, space, and period
    int[] limits = { 0, -1 }; // Limit values to try
    for (int limit : limits) {
      System.out.println("\nAnalysis with limit = " + limit);
      String[] tokens = text.split(delimiters, limit);
      System.out.println("Number of tokens: " + tokens.length);
      for (String token : tokens) {
        System.out.println(token);
      }
    }
  }
}
```

```java title=Example.java

Analysis with limit = 0
Number of tokens: 11
To
be
or
not
to
be

that
is
the
question

Analysis with limit = -1
Number of tokens: 12
To
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
