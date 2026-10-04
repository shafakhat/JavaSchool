---
title: Try out regular expressions
nav: Try out regular expressions
description: System.out.println("Usage:\n" + "java MainClass " + "characterSequence regularExpression+");
section: Imported - java2s Archive
order: 1900
source: https://web.archive.org/web/20140829082124/http://www.java2s.com/Tutorial/Java/0120__Development/Tryoutregularexpressions.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    if (args.length < 2) {
      System.out.println("Usage:\n" + "java MainClass " + "characterSequence regularExpression+");
      System.exit(0);
    }
    System.out.println("Input: \"" + args[0] + "\"");
    for (int i = 1; i < args.length; i++) {
      System.out.println("Regular expression: \"" + args[i] + "\"");
      Pattern p = Pattern.compile(args[i]);
      Matcher m = p.matcher(args[0]);
      while (m.find()) {
        System.out.println("Match \"" + m.group() + "\" at positions " + m.start() + "-"
            + (m.end() - 1));
      }
    }
  }
}
```
