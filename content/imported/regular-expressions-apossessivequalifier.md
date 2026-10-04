---
title: A possessive qualifier
nav: A possessive qualifier
description: Imported from the java2s.com archive: A possessive qualifier
section: Imported - java2s Archive
order: 2227
source: https://web.archive.org/web/20140829092704/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Apossessivequalifier.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String regex = "(\\w++)(\\d\\d)(\\w+)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "X99SuperJava";
    Matcher matcher = pattern.matcher(candidate);
    if (matcher.find()) {
      System.out.println("GROUP 0:" + matcher.group(0));
      System.out.println("GROUP 1:" + matcher.group(1));
      System.out.println("GROUP 2:" + matcher.group(2));
      System.out.println("GROUP 3:" + matcher.group(3));
    } else {
      System.out.println("NO MATCHES");
    }
    System.out.println("Done");
  }
}
/*
 */
java title=Example.java
NO MATCHES
Done
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
