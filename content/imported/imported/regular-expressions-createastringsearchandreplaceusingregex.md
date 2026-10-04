---
title: Create a string search and replace using regex
nav: Create a string search and...
description: String source = "The quick brown fox jumps over the brown lazy dog.";
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20090502015357/http://www.java2s.com:80/Code/Java/Regular-Expressions/Createastringsearchandreplaceusingregex.htm
---
Create a string search and replace using regex

```java title=Example.java
import java.util.regex.Pattern;
import java.util.regex.Matcher;
public class Main {
  public static void main(String[] args) {
    String source = "The quick brown fox jumps over the brown lazy dog.";
    String find = "brown";
    String replace = "red";
    Pattern pattern = Pattern.compile(find);
    Matcher matcher = pattern.matcher(source);
    String output = matcher.replaceAll(replace);
    System.out.println("Source = " + source);
    System.out.println("Output = " + output);
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
18.  Split-up string using regular expression
19.  Apply proper uppercase and lowercase on a String
20.  Regular Expression Search and Replace Program
21.  Searching and Replacing with Nonconstant Values Using a Regular Expression
22.  Use Matcher.appendReplacement() to match [a-zA-Z]+[0-9]+
23.  Ignore case differences when searching for or replacing substrings.
24.  Use replaceAll() to ignore case when replacing one substring with another
25.  Extract a substring by matching a regular expression.
26.  Match string ends
27.  Match words
28.  Match punct
29.  Match space
30.  Determining If a String Matches a Pattern Exactly
31.  Removing Duplicate Whitespace in a String
