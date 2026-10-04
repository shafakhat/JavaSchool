---
title: Java Regular Expression
nav: Java Regular Expression
description: Java Regular Expression : find 2 : Java examples (example source code) » Regular Expressions » Lookup
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20060506131235/http://www.java2s.com:80/Code/Java/Regular-Expressions/JavaRegularExpressionfind2.htm
---
Java Regular Expression : find 2 : Java examples (example source code) » Regular Expressions » Lookup

Java Regular Expression : find 2

```java title=Example.java
/* From http://java.sun.com/docs/books/tutorial/index.html */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
public final class RegexTestHarness2 {
  private static String REGEX;
  private static String INPUT;
  private static BufferedReader br;
  private static Pattern pattern;
  private static Matcher matcher;
  private static boolean found;
  public static void main(String[] argv) {
    initResources();
    processTest();
    closeResources();
  }
  private static void initResources() {
    try {
      br = new BufferedReader(new FileReader("regex.txt"));
    } catch (FileNotFoundException fnfe) {
      System.out
          .println("Cannot locate input file! " + fnfe.getMessage());
      System.exit(0);
    }
    try {
      REGEX = br.readLine();
      INPUT = br.readLine();
    } catch (IOException ioe) {
    }
    try {
      pattern = Pattern.compile(REGEX);
      matcher = pattern.matcher(INPUT);
    } catch (PatternSyntaxException pse) {
      System.out
          .println("There is a problem with the regular expression!");
      System.out.println("The pattern in question is: "
          + pse.getPattern());
      System.out.println("The description is: " + pse.getDescription());
      System.out.println("The message is: " + pse.getMessage());
      System.out.println("The index is: " + pse.getIndex());
      System.exit(0);
    }
    System.out.println("Current REGEX is: " + REGEX);
    System.out.println("Current INPUT is: " + INPUT);
  }
  private static void processTest() {
    while (matcher.find()) {
      System.out.println("I found the text \"" + matcher.group()
          + "\" starting at index " + matcher.start()
          + " and ending at index " + matcher.end() + ".");
      found = true;
    }
    if (!found) {
      System.out.println("No match found.");
    }
  }
  private static void closeResources() {
    try {
      br.close();
    } catch (IOException ioe) {
    }
  }
}
```

Related examples in the same category
---
1. Positive Look behind 1
2. Positive Look ahead
3. Positive Look Behind 2
4. Positive Look Behind 3
5. Negative Look ahead
6. Regular Expression: find
7. Java Regular Expression : File and Find
