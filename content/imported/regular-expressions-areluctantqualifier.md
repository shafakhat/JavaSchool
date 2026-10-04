---
title: A Reluctant qualifier
nav: A Reluctant qualifier
description: Imported from the java2s.com archive: A Reluctant qualifier
section: Imported - java2s Archive
order: 2241
source: https://web.archive.org/web/20140829082339/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/AReluctantqualifier.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String regex = "(\\d+?)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "1234";
    Matcher matcher = pattern.matcher(candidate);
    System.out.println(matcher.group());
  }
}
```
