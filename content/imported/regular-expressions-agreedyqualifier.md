---
title: A greedy qualifier
nav: A greedy qualifier
description: Imported from the java2s.com archive: A greedy qualifier
section: Imported - java2s Archive
order: 2239
source: https://web.archive.org/web/20140829082405/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Agreedyqualifier.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String regex = "(\\w+)(\\d\\d)(\\w+)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "AAA99SuperJava";
    Matcher matcher = pattern.matcher(candidate);
    matcher.find();
    System.out.println(matcher.group(1));
    System.out.println(matcher.group(2));
    System.out.println(matcher.group(3));
  }
}
/*
*/
java title=Example.java
AAA
99
SuperJava
```
