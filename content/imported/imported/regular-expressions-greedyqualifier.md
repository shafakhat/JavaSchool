---
title: Greedy Qualifier
nav: Greedy Qualifier
description: Imported from the java2s.com archive: Greedy Qualifier
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20100206192627/http://java2s.com/Code/Java/Regular-Expressions/GreedyQualifier.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main  {
  public static void main(String args[]) {
    String regex = "(\\w+)(\\d\\d)(\\w+)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "X99 asdf 44";
    Matcher matcher = pattern.matcher(candidate);
    matcher.find();
    System.out.println(matcher.group(1));
    System.out.println(matcher.group(2));
    System.out.println(matcher.group(3));
  }
}
```

1.  Greedy and Nongreedy Matching in a Regular Expression
---  ---
2.  Reluctant Qualifier Example
3.  Nongreedy quantifiers
