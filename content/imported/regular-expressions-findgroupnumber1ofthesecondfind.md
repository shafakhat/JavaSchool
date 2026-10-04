---
title: Find group number 1 of the second find
nav: Find group number 1 of the...
description: 9. Getting the Indices of a Matching Group in a Regular Expression
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20090606185135/http://www.java2s.com:80/Code/Java/Regular-Expressions/Findgroupnumber1ofthesecondfind.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    Pattern p = Pattern.compile("t(est)");
    String candidateString = "This is a test. This is a test.";
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    String group_0 = matcher.group(0);
    String group_1 = matcher.group(1);
    System.out.println("Group 0 " + group_0);
    System.out.println("Group 1 " + group_1);
  }
}
```

1.  find the starting point of the first subgroup
---  ---
2.  Find the starting point of the second subgroup
3.  Matcher.group(int) Method Example
4.  Matcher Group Count
5.  Using appendReplacement with Subgroup Replacements
6.  Working with Groups: characters and digits
7.  Working with Subgroups
8.  Capturing Text in a Group in a Regular Expression
9.  Getting the Indices of a Matching Group in a Regular Expression
10.  Using a Non-Capturing Group in a Regular Expression
11.  Using the Captured Text of a Group within a Pattern
12.  Using the Captured Text of a Group within a Replacement Pattern
