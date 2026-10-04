---
title: Another pattern split
nav: Another pattern split
description: Another pattern split : Java examples (example source code) » Regular Expressions » Pattern
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20060513094139/http://www.java2s.com/Code/Java/Regular-Expressions/Anotherpatternsplit.htm
---
Another pattern split : Java examples (example source code) » Regular Expressions » Pattern

```java title=Example.java
import java.util.regex.Pattern;
public class PatternSplit {
  public static void main(String args[]) {
    String statement = "I will not compromise. I will not "
        + "cooperate. There will be no concession, no conciliation, no "
        + "finding the middle ground, and no give and take.";
    String tokens[] = null;
    String splitPattern = "compromise|cooperate|concession|"
        + "conciliation|(finding the middle ground)|(give and take)";
    Pattern p = Pattern.compile(splitPattern);
    tokens = p.split(statement);
    System.out.println("REGEX PATTERN:\n" + splitPattern + "\n");
    System.out.println("STATEMENT:\n" + statement + "\n");
    System.out.println("TOKENS:");
    for (int i = 0; i < tokens.length; i++) {
      System.out.println(tokens[i]);
    }
  }
}
```

Related examples in the same category
---
1. Simple Pattern
2. Pattern Match
3. Pattern Split
4. Reg Exp Example
5. PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
6. Simple example of using Regular Expressions functionality in String class
7. Show use of Pattern.CANON_EQ
8. A block of text to use as input to the regular expression matcher
9. Allows you to easly try out regular expressions
10. Regular expressions: start End
11. Pattern: Resetting
12. Pattern: flags
