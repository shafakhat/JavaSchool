---
title: Pattern.compile('(?m)(\\S+)\\s+((\\S+)\\s+(\\S+))$').matcher
nav: Pattern.compile('(?m)(\\S+...
description: static public final String poem = "PC Bird Cow Slow Doe Hole Joe\n"
section: Imported - java2s Archive
order: 1885
source: https://web.archive.org/web/20140829081831/http://www.java2s.com/Tutorial/Java/0120__Development/PatterncompilemSsSsSmatcher.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  static public final String poem = "PC Bird Cow Slow Doe Hole Joe\n"
      + "Shy Shift Sleep Do Down Doing.\n" + "Yes No How Whose\n";
  public static void main(String[] args) {
    Matcher m = Pattern.compile("(?m)(\\S+)\\s+((\\S+)\\s+(\\S+))$").matcher(poem);
    while (m.find()) {
      for (int j = 0; j <= m.groupCount(); j++)
        System.out.print("[" + m.group(j) + "]");
      System.out.println();
    }
  }
}
/**/
java title=Example.java
[Doe Hole Joe][Doe][Hole Joe][Hole][Joe]
[Do Down Doing.][Do][Down Doing.][Down][Doing.]
[No How Whose][No][How Whose][How][Whose]
```
