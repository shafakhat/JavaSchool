---
title: Allows you to easly try out regular expressions
nav: Allows you to easly try ou...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20060903221603/http://www.java2s.com:80/Code/Java/Regular-Expressions/Allowsyoutoeaslytryoutregularexpressions.htm
---
Allows you to easly try out regular expressions

```java title=Example.java
// : c12:TestRegularExpression.java
// Allows you to easly try out regular expressions.
// {Args: abcabcabcdefabc "abc+" "(abc)+" "(abc){2,}" }
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class TestRegularExpression {
  public static void main(String[] args) {
    if (args.length < 2) {
      System.out.println("Usage:\n" + "java TestRegularExpression "
          + "characterSequence regularExpression+");
      System.exit(0);
    }
    System.out.println("Input: \"" + args[0] + "\"");
    for (int i = 1; i < args.length; i++) {
      System.out.println("Regular expression: \"" + args[i] + "\"");
      Pattern p = Pattern.compile(args[i]);
      Matcher m = p.matcher(args[0]);
      while (m.find()) {
        System.out.println("Match \"" + m.group() + "\" at positions "
            + m.start() + "-" + (m.end() - 1));
      }
    }
  }
} ///:~
```

Related examples in the same category
---
1. Simple Pattern
2. Pattern Match
3. Pattern Split
4. Another pattern split
5. Reg Exp Example
6. PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
7. Simple example of using Regular Expressions functionality in String class
8. Show use of Pattern.CANON_EQ
9. A block of text to use as input to the regular expression matcher
10. Regular expressions: start End
11. Pattern: Resetting
12. Pattern: flags
