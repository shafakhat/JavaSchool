---
title: Finding all words that start with an 'a'
nav: Finding all words that sta...
description: Define the matching pattern as a word boundry, a lowercase a, any number of immedietly trailing letters numbers, or underscores, followed by a word boundary
section: Imported - java2s Archive
order: 2233
source: https://web.archive.org/web/20140829090533/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Findingallwordsthatstartwithana.htm
---
Define the matching pattern as a word boundry, a lowercase a, any number of immedietly trailing letters numbers, or underscores, followed by a word boundary

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) throws Exception {
    String candidate = "applying a pattern.";
    String regex = "\\ba\\w*\\b";
    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(candidate);
    String val = null;
    System.out.println("INPUT: " + candidate);
    System.out.println("REGEX: " + regex + "\r\n");
    while (m.find()) {
      val = m.group();
      System.out.println("MATCH: " + val);
    }
    if (val == null) {
      System.out.println("NO MATCHES: ");
    }
  }
}
```

| 8.1.1. | Meta-characters predefined to match specific characters. |
|---|---|
| 8.1.2. | Meta-characters to match against certain string boundaries. |
| 8.1.3. | Regular expression languages also have character classes. |
| 8.1.4. | POSIX character classes and Java character classes |
| 8.1.5. | Java Character Class |
| 8.1.6. | Match a particular character a specified number of times. |
| 8.1.7. | Read regular expression from console |
| 8.1.8. | Regex Test Harness |
| 8.1.9. | Match Java source file and file and class name |
| 8.1.10. | Finding all words that start with an 'a' |
| 8.1.11. | Simple validation using the Pattern and Matcher objects |
| 8.1.12. | A possessive qualifier |
| 8.1.13. | Find the starting point of the second 'Bond' |
| 8.1.14. | A negative look ahead |
| 8.1.15. | A negative behind ahead |
| 8.1.16. | A positive look ahead |
| 8.1.17. | Pattern helper |
| 8.1.18. | Escapes characters that have special meaning to regular expressions |
