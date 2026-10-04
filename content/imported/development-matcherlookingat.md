---
title: Matcher.LookingAt
nav: Matcher.LookingAt
description: String[] input = new String[] { "Java has regular expressions in 1.4",
section: Imported - java2s Archive
order: 1826
source: https://web.archive.org/web/20140829080226/http://www.java2s.com/Tutorial/Java/0120__Development/MatcherLookingAt.htm
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
      if (m1.lookingAt()) // No reset() necessary
        System.out.println("m1.lookingAt() start = " + m1.start() + " end = " + m1.end());
    }
  }
}
/*
*/
java title=Example.java
input 0: Java has regular expressions in 1.4
input 1: regular expressions now expressing in Java
m1.lookingAt() start = 0 end = 7
input 2: Java represses oracular expressions
```

| 6.33.1. | Matcher Start and End |
|---|---|
| 6.33.2. | Matcher.LookingAt |
| 6.33.3. | Matcher Find |
