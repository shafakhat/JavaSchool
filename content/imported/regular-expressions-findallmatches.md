---
title: Find all matches
nav: Find all matches
description: 6. PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20090422123407/http://www.java2s.com:80/Code/Java/Regular-Expressions/Findallmatches.htm
---
Find all matches

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    Pattern pattern = Pattern.compile("pattern");
    Matcher matcher = pattern.matcher("infile.txt");
    // Find all matches
    while (matcher.find()) {
      // Get the matching string
      String match = matcher.group();
    }
  }
}
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
10.  Allows you to easly try out regular expressions
11.  Regular expressions: start End
12.  Pattern: Resetting
13.  Pattern: flags
14.  Setting Case Sensitivity in a Regular Expression
15.  Use enclosing form
16.  Use a character set
17.  Adding Comments to a Regular Expression
18.  The inline modifier can also contain pattern characters using the form (?x:abc)
19.  Use an inline modifier: (?x)a [\\ ] b
20.  Use an inline modifier: x)a \\s b
21.  Use an inline modifier: a (?x: b)
22.  Tabs and newlines in the pattern are ignored as well
23.  Compiling a Pattern with Multiple Flags
24.  Matching Across Line Boundaries in a Regular Expression
25.  Match Duplicate Words
26.  Validation Test With Pattern And Matcher
27.  Match one or more
28.  Matcher.reset: restart
29.  Matcher.reset(CharSequence)
30.  Matcher.start(): Find the starting point
31.  Matcher.start(int) Example
32.  Matcher.end(): find the end point
33.  Find the end point of the second 'test'
34.  Using the find() Method from Matcher
35.  Using the find(int) Method
36.  Using the lookingAt Method
37.  Possessive Qualifier Example
38.  Simple Positive Lookahead
39.  Finding Every Occurrence of the Letter A
40.  Simple Negative Lookahead
41.  Simple Positive Lookbehind
42.  Regular expression search program
43.  Implement a pattern matcher for regular expressions
44.  Regular expression and CharSequence
45.  Regular Expression search and replace program
