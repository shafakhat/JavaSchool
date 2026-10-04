---
title: Escaping Special Characters in a Pattern
nav: Escaping Special Character...
description: matchFound = Pattern.matches("\\Q" + patternStr + "\\E", "i.e.");
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20100211073412/http://java2s.com/Code/Java/Regular-Expressions/EscapingSpecialCharactersinaPattern.htm
---
```java title=Example.java
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    String patternStr = "i.e.";
    boolean matchFound = Pattern.matches(patternStr, "i.e.");
    matchFound = Pattern.matches(patternStr, "ibex");
    // Quote the pattern; i.e. surround with \Q and \E
    matchFound = Pattern.matches("\\Q" + patternStr + "\\E", "i.e.");
    matchFound = Pattern.matches("\\Q" + patternStr + "\\E", "ibex");
    // Escape the pattern
    patternStr = escapeRE(patternStr);
    matchFound = Pattern.matches(patternStr, "i.e.");
    matchFound = Pattern.matches(patternStr, "ibex");
    // Returns a pattern where all punctuation characters are escaped.
  }
  public static String escapeRE(String str) {
    Pattern escaper = Pattern.compile("([^a-zA-z0-9])");
    return escaper.matcher(str).replaceAll("\\\\$1");
  }
}
```

1.  REGEX = "a*b"
---  ---
2.  Removing Line Termination Characters from a String
3.  Append Replacement Method
4.  ReplaceAll Method from Matcher
5.  replaceFirst Method from Matcher
6.  Working with Back References
7.  Regular Expression search and replace program
