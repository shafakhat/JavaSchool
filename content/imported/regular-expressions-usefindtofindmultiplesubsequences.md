---
title: Use find() to find multiple subsequences.
nav: Use find() to find multipl...
description: Imported from the java2s.com archive: Use find() to find multiple subsequences.
section: Imported - java2s Archive
order: 2246
source: https://web.archive.org/web/20140829074944/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Usefindtofindmultiplesubsequences.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class RegExpr3 {
  public static void main(String args[]) {
    Pattern pat = Pattern.compile("test");
    Matcher mat = pat.matcher("test 1 2 3 test");
    while (mat.find()) {
      System.out.println("test found at index " + mat.start());
    }
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
