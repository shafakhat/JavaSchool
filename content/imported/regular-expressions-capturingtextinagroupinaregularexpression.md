---
title: Capturing Text in a Group in a Regular Expression
nav: Capturing Text in a Group ...
description: 9. Getting the Indices of a Matching Group in a Regular Expression
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20090606185130/http://www.java2s.com:80/Code/Java/Regular-Expressions/CapturingTextinaGroupinaRegularExpression.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    CharSequence inputStr = "abbabcd";
    String patternStr = "(a(b*))+(c*)";
    // Compile and use regular expression
    Pattern pattern = Pattern.compile(patternStr);
    Matcher matcher = pattern.matcher(inputStr);
    boolean matchFound = matcher.find();
    if (matchFound) {
      // Get all groups for this match
      for (int i = 0; i <= matcher.groupCount(); i++) {
        String groupStr = matcher.group(i);
      }
    }
  }
}
```

1.  find the starting point of the first subgroup
---  ---
2.  Find the starting point of the second subgroup
3.  Matcher.group(int) Method Example
4.  Find group number 1 of the second find
5.  Matcher Group Count
6.  Using appendReplacement with Subgroup Replacements
7.  Working with Groups: characters and digits
8.  Working with Subgroups
9.  Getting the Indices of a Matching Group in a Regular Expression
10.  Using a Non-Capturing Group in a Regular Expression
11.  Using the Captured Text of a Group within a Pattern
12.  Using the Captured Text of a Group within a Replacement Pattern
