---
title: Find the starting point of the second 'Bond'
nav: Find the starting point of...
description: String matchHelper[] = { " ^", " ^" };
section: Imported - java2s Archive
order: 2228
source: https://web.archive.org/web/20140829090544/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/FindthestartingpointofthesecondBond.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String candidateString = "My name is Bond. James Bond.";
    String matchHelper[] = { "          ^", "                      ^" };
    Pattern p = Pattern.compile("Bond");
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    int nextIndex = matcher.start();
    System.out.println(candidateString);
    System.out.println(matchHelper[1] + nextIndex);
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
