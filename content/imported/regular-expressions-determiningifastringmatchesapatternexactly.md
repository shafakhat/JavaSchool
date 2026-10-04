---
title: Determining If a String Matches a Pattern Exactly
nav: Determining If a String Ma...
description: Determining If a String Matches a Pattern Exactly : String Operation « Regular Expressions « Java
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20090826174239/http://www.java2s.com:80/Code/Java/Regular-Expressions/DeterminingIfaStringMatchesaPatternExactly.htm
---
Determining If a String Matches a Pattern Exactly : String Operation « Regular Expressions « Java
Determining If a String Matches a Pattern Exactly

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Compile regular expression
    String patternStr = "b";
    Pattern pattern = Pattern.compile(patternStr);
    // Determine if there is an exact match
    CharSequence inputStr = "a b c";
    Matcher matcher = pattern.matcher(inputStr);
    boolean matchFound = matcher.matches();
    // Try a different input
    matcher.reset("b");
    matchFound = matcher.matches();
    // Determine if pattern matches beginning of input
    matchFound = matcher.lookingAt();
  }
}
```

1.  Regular expression: Split Demo
---  ---
2.  Replacing String Tokenizer
3.  String replace
4.  String split
5.  Simple split
6.  Calculating Word Frequencies with Regular Expressions
7.  Print all the strings that match a given pattern from a file
8.  Quick demo of Regular Expressions substitution
9.  Parse an Apache log file with StringTokenizer
10.  StringConvenience -- demonstrate java.lang.String convenience routine
11.  Split a String into a Java Array of Strings divided by an Regular Expressions
12.  Regular Expression Replace
13.  Java Regular Expression : Split text
14.  Java Regular Expression :split 2
15.  Get all digits from a string
16.  Strip extra spaces in a XML string
17.  Remove trailing white space from a string
18.  Create a string search and replace using regex
19.  Split-up string using regular expression
20.  Apply proper uppercase and lowercase on a String
21.  Regular Expression Search and Replace Program
22.  Searching and Replacing with Nonconstant Values Using a Regular Expression
23.  Use Matcher.appendReplacement() to match [a-zA-Z]+[0-9]+
24.  Ignore case differences when searching for or replacing substrings.
25.  Use replaceAll() to ignore case when replacing one substring with another
26.  Extract a substring by matching a regular expression.
27.  Match string ends
28.  Match words
29.  Match punct
30.  Match space
31.  Removing Duplicate Whitespace in a String
32.  Split the supplied content into lines, returning each line as an element in the returned list.
33.  Get First Found regex
34.  Get Found regex
35.  Get First Not Empty String in a String list
