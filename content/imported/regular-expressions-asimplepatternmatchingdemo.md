---
title: A simple pattern matching demo.
nav: A simple pattern matching ...
description: Imported from the java2s.com archive: A simple pattern matching demo.
section: Imported - java2s Archive
order: 2264
source: https://web.archive.org/web/20140829074736/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Asimplepatternmatchingdemo.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class RegExpr {
  public static void main(String args[]) {
    Pattern pat;
    Matcher mat;
    boolean found;
    pat = Pattern.compile("Java");
    mat = pat.matcher("Java");
    found = mat.matches();
    if (found)
      System.out.println("Matches");
    else
      System.out.println("No Match");
    mat = pat.matcher("Java 2");
    found = mat.matches();
    if (found)
      System.out.println("Matches");
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
