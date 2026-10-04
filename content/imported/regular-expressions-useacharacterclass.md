---
title: Use a character class.
nav: Use a character class.
description: Imported from the java2s.com archive: Use a character class.
section: Imported - java2s Archive
order: 2249
source: https://web.archive.org/web/20140829075110/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Useacharacterclass.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class RegExpr7 {
  public static void main(String args[]) {
    Pattern pat = Pattern.compile("[a-z]+");
    Matcher mat = pat.matcher("this is a test.");
    while (mat.find())
      System.out.println("Match: " + mat.group());
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
