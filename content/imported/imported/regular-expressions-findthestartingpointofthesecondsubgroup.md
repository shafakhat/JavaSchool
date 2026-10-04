---
title: Find the starting point of the second subgroup
nav: Find the starting point of...
description: String candidateString = "This is a test. This is another test.";
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20090606190525/http://www.java2s.com:80/Code/Java/Regular-Expressions/Findthestartingpointofthesecondsubgroup.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("t(est)");
    String candidateString = "This is a test. This is another test.";
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    int startIndex = matcher.start(0);
    System.out.println(candidateString);
    System.out.println(startIndex);
  }
}
```

1.  find the starting point of the first subgroup
---  ---
2.  Matcher.group(int) Method Example
3.  Find group number 1 of the second find
4.  Matcher Group Count
5.  Using appendReplacement with Subgroup Replacements
6.  Working with Groups: characters and digits
7.  Working with Subgroups
8.  Capturing Text in a Group in a Regular Expression
9.  Getting the Indices of a Matching Group in a Regular Expression
10.  Using a Non-Capturing Group in a Regular Expression
11.  Using the Captured Text of a Group within a Pattern
12.  Using the Captured Text of a Group within a Replacement Pattern
