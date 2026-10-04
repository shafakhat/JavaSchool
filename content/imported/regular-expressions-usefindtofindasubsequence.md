---
title: Use find() to find a subsequence.
nav: Use find() to find a subse...
description: Imported from the java2s.com archive: Use find() to find a subsequence.
section: Imported - java2s Archive
order: 2250
source: https://web.archive.org/web/20140829075054/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Usefindtofindasubsequence.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class RegExpr2 {
  public static void main(String args[]) {
    Pattern pat = Pattern.compile("Java");
    Matcher mat = pat.matcher("Java 2");
    System.out.println("Looking for Java in Java 2.");
    if (mat.find())
      System.out.println("subsequence found");
    else
      System.out.println("No Match");
  }
}
```

| 8.5.1. | Use Pattern class to match |
|---|---|
| 8.5.2. | Pattern.compile method |
| 8.5.3. | Reuse Pattern Method |
| 8.5.4. | Control the pattern case |
| 8.5.5. | A simple pattern matching demo. |
| 8.5.6. | Use find() to find a subsequence. |
| 8.5.7. | Use find() to find multiple subsequences. |
| 8.5.8. | Use a quantifier. |
| 8.5.9. | Use wildcard and quantifier. |
| 8.5.10. | Use the ? quantifier. |
| 8.5.11. | Use a character class. |
| 8.5.12. | Split by number |
| 8.5.13. | Split by : |
