---
title: Matcher Find
nav: Matcher Find
description: Matcher m = Pattern.compile("\\w+").matcher("Today is Sunday");
section: Imported - java2s Archive
order: 1830
source: https://web.archive.org/web/20140829080508/http://www.java2s.com/Tutorial/Java/0120__Development/MatcherFind.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    Matcher m = Pattern.compile("\\w+").matcher("Today is Sunday");
    while (m.find())
      System.out.println(m.group());
    int i = 0;
    while (m.find(i)) {
      System.out.print(m.group() + " ");
      i++;
    }
  }
}
/* */
java title=Example.java
Today
is
Sunday
Today oday day ay y is is s Sunday Sunday unday nday day ay y
```

| 6.33.1. | Matcher Start and End |
|---|---|
| 6.33.2. | Matcher.LookingAt |
| 6.33.3. | Matcher Find |
