---
title: Matcher Start and End
nav: Matcher Start and End
description: String[] input = new String[] { "Java has regular expressions in 1.4",
section: Imported - java2s Archive
order: 1825
source: https://web.archive.org/web/20140829080636/http://www.java2s.com/Tutorial/Java/0120__Development/MatcherStartandEnd.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    String[] input = new String[] { "Java has regular expressions in 1.4",
        "regular expressions now expressing in Java", "Java represses oracular expressions" };
    Pattern p1 = Pattern.compile("re\\w*"), p2 = Pattern.compile("Java.*");
    for (int i = 0; i < input.length; i++) {
      System.out.println("input " + i + ": " + input[i]);
      Matcher m1 = p1.matcher(input[i]), m2 = p2.matcher(input[i]);
      while (m1.find())
        System.out.println("m1.find() '" + m1.group() + "' start = " + m1.start() + " end = "
            + m1.end());
    }
  }
}
/*
*/
java title=Example.java
input 0: Java has regular expressions in 1.4
m1.find() 'regular' start = 9 end = 16
m1.find() 'ressions' start = 20 end = 28
input 1: regular expressions now expressing in Java
m1.find() 'regular' start = 0 end = 7
m1.find() 'ressions' start = 11 end = 19
m1.find() 'ressing' start = 27 end = 34
input 2: Java represses oracular expressions
m1.find() 'represses' start = 5 end = 14
m1.find() 'ressions' start = 27 end = 35
```

| 6.33.1. | Matcher Start and End |
|---|---|
| 6.33.2. | Matcher.LookingAt |
| 6.33.3. | Matcher Find |
