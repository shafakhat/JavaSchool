---
title: Java Regular Expression
nav: Java Regular Expression
description: /* From http://java.sun.com/docs/books/tutorial/index.html */
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20070110035929/http://www.java2s.com:80/Code/Java/Regular-Expressions/JavaRegularExpressionsplit2.htm
---
Java Regular Expression :split 2

```java title=Example.java
/* From http://java.sun.com/docs/books/tutorial/index.html */
import java.util.regex.Pattern;
public final class SplitTest2 {
  private static String REGEX = "\\d";
  private static String INPUT = "one9two4three7four1five";
  public static void main(String[] argv) {
    Pattern p = Pattern.compile(REGEX);
    String[] items = p.split(INPUT);
    for (int i = 0; i < items.length; i++) {
      System.out.println(items[i]);
    }
  }
}
```

Related examples in the same category
---
1. Regular expression: Split Demo
2. Replacing String Tokenizer
3. String replace
4. String split
5. Simple split
6. Calculating Word Frequencies with Regular Expressions
7. Print all the strings that match a given pattern from a file
8. Quick demo of Regular Expressions substitution
9. Parse an Apache log file with StringTokenizer
10. StringConvenience -- demonstrate java.lang.String convenience routine
11. Split a String into a Java Array of Strings divided by an Regular Expressions
12. Regular Expression Replace
13. Java Regular Expression : Split text
