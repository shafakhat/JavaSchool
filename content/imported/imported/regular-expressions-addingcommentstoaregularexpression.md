---
title: Adding Comments to a Regular Expression
nav: Adding Comments to a Regul...
description: 6. PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090422124057/http://www.java2s.com:80/Code/Java/Regular-Expressions/AddingCommentstoaRegularExpression.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Use COMMENTS but include a character class with a space
    CharSequence inputStr = "a b";
    String patternStr = "a b";
    // Compile without comments
    Pattern pattern = Pattern.compile(patternStr);
    Matcher matcher = pattern.matcher(inputStr);
    boolean matchFound = matcher.matches();
    // Compile with comments
    pattern = Pattern.compile(patternStr, Pattern.COMMENTS);
    matcher = pattern.matcher(inputStr);
    matchFound = matcher.matches();
    patternStr = "a  [\\ ]  b";
    pattern = Pattern.compile(patternStr, Pattern.COMMENTS);
    matcher = pattern.matcher(inputStr);
    matchFound = matcher.matches();
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
