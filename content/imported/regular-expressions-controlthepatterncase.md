---
title: Control the pattern case
nav: Control the pattern case
description: Pattern p = Pattern.compile("java", Pattern.CASE_INSENSITIVE);
section: Imported - java2s Archive
order: 2245
source: https://web.archive.org/web/20140829074636/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Controlthepatterncase.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("java", Pattern.CASE_INSENSITIVE);
    String candidateString = "Java. java JAVA jAVA";
    Matcher matcher = p.matcher(candidateString);
    // display the latter match
    System.out.println(candidateString);
    matcher.find(11);
    System.out.println(matcher.group());
    // display the earlier match
    System.out.println(candidateString);
    matcher.find(0);
    System.out.println(matcher.group());
  }
}
/*
*/
java title=Example.java
Java. java JAVA jAVA
JAVA
Java. java JAVA jAVA
Java
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
