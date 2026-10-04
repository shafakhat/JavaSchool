---
title: Split a string
nav: Split a string
description: String sentence = "This is a test, and that is another test.";
section: Imported - java2s Archive
order: 2260
source: https://web.archive.org/web/20140829090418/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Splitastring.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    String splitPattern = ",";
    String sentence = "This is a test, and that is another test.";
    String[] tokens = sentence.split(splitPattern);
    for (String s : tokens) {
      System.out.println(s);
    }
  }
}
```

8.8.1.  Split a string
