---
title: Pattern.compile(^java, Pattern.CASE_INSENSITIVE | Pattern.MULTILINE)
nav: Pattern.compile(^java, Pat...
description: Pattern p = Pattern.compile("^java", Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
section: Imported - java2s Archive
order: 1891
source: https://web.archive.org/web/20140829082114/http://www.java2s.com/Tutorial/Java/0120__Development/PatterncompilejavaPatternCASEINSENSITIVEPatternMULTILINE.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    Pattern p = Pattern.compile("^java", Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
    Matcher m = p.matcher("java has regex\nJava has regex\n"
        + "JAVA has pretty good regular expressions\n" + "Regular expressions are in Java");
    while (m.find())
      System.out.println(m.group());
  }
}
/*
 */
java title=Example.java
java
 Java
 JAVA
```
