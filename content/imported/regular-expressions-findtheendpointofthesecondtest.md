---
title: Find the end point of the second 'test'
nav: Find the end point of the ...
description: String candidateString = "This is a test. This is another test.";
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20090418182238/http://www.java2s.com:80/Code/Java/Regular-Expressions/Findtheendpointofthesecondtest.htm
---
Find the end point of the second 'test'

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String args[]) {
    String candidateString = "This is a test. This is another test.";
    Pattern p = Pattern.compile("test");
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    int nextIndex = matcher.end();
    System.out.println(nextIndex);
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
