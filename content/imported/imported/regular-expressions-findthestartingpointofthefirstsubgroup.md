---
title: find the starting point of the first subgroup
nav: find the starting point of...
description: String candidateString = "This is a test. This is another test.";
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20090606190555/http://www.java2s.com:80/Code/Java/Regular-Expressions/findthestartingpointofthefirstsubgroup.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("t(est)");
    String candidateString = "This is a test. This is another test.";
    Matcher matcher = p.matcher(candidateString);
    int nextIndex = matcher.start(1);
    System.out.println(candidateString);
    System.out.println(nextIndex);
  }
}
```

1.  Find the starting point of the second subgroup
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
