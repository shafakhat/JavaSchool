---
title: Reuse Pattern Method
nav: Reuse Pattern Method
description: Imported from the java2s.com archive: Reuse Pattern Method
section: Imported - java2s Archive
order: 2244
source: https://web.archive.org/web/20140829074731/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/ReusePatternMethod.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("\\d");
    Matcher matcher = p.matcher("5");
    boolean isOk = matcher.matches();
    System.out.println("original pattern matches " + isOk);
    // recycle the pattern
    String tmp = p.pattern();
    Pattern p2 = Pattern.compile(tmp);
    matcher = p.matcher("5");
    isOk = matcher.matches();
    System.out.println("second pattern matches " + isOk);
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
