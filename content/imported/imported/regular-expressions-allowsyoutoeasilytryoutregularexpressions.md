---
title: Allows you to easily try out regular expressions
nav: Allows you to easily try o...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20090814170858/http://www.java2s.com:80/Code/Java/Regular-Expressions/Allowsyoutoeasilytryoutregularexpressions.htm
---
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

1.  Simple Pattern
---  ---
2.  Pattern Match
3.  Pattern Split
4.  Another pattern split
5.  Reg Exp Example
6.  PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
7.  Simple example of using Regular Expressions functionality in String class
8.  Show use of Pattern.CANON_EQ
9.  A block of text to use as input to the regular expression matcher
10.  Regular expressions: start End
11.  Pattern: Resetting
12.  Pattern: flags
13.  Setting Case Sensitivity in a Regular Expression
14.  Use enclosing form
15.  Use a character set
16.  Adding Comments to a Regular Expression
17.  The inline modifier can also contain pattern characters using the form (?x:abc)
18.  Use an inline modifier: (?x)a [\\ ] b
19.  Use an inline modifier: x)a \\s b
20.  Use an inline modifier: a (?x: b)
21.  Tabs and newlines in the pattern are ignored as well
22.  Compiling a Pattern with Multiple Flags
23.  Matching Across Line Boundaries in a Regular Expression
24.  Match Duplicate Words
25.  Validation Test With Pattern And Matcher
26.  Match one or more
27.  Matcher.reset: restart
28.  Matcher.reset(CharSequence)
29.  Matcher.start(): Find the starting point
30.  Matcher.start(int) Example
31.  Matcher.end(): find the end point
32.  Find the end point of the second 'test'
33.  Using the find() Method from Matcher
34.  Using the find(int) Method
35.  Using the lookingAt Method
36.  Possessive Qualifier Example
37.  Simple Positive Lookahead
38.  Finding Every Occurrence of the Letter A
39.  Simple Negative Lookahead
40.  Simple Positive Lookbehind
41.  Regular expression search program
42.  Find all matches
43.  Implement a pattern matcher for regular expressions
44.  Regular expression and CharSequence
45.  Regular Expression search and replace program
46.  Pattern helper
