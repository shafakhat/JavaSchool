---
title: Pattern.compile('!!').split
nav: Pattern.compile('!!').split
description: System.out.println(Arrays.asList(Pattern.compile("!!").split(input)));
section: Imported - java2s Archive
order: 1889
source: https://web.archive.org/web/20140829082127/http://www.java2s.com/Tutorial/Java/0120__Development/Patterncompilesplit.htm
---
```java title=Example.java
import java.util.Arrays;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    String input = "This!!unusual use!!of exclamation!!points";
    System.out.println(Arrays.asList(Pattern.compile("!!").split(input)));
    System.out.println(Arrays.asList(Pattern.compile("!!").split(input, 3)));
    System.out.println(Arrays.asList("Aha! String has a split() built in!".split(" ")));
  }
}
/**/
java title=Example.java
[This, unusual use, of exclamation, points]
[This, unusual use, of exclamation!!points]
[Aha!, String, has, a, split(), built, in!]
```
