---
title: A negative behind ahead
nav: A negative behind ahead
description: System.out.println("candidate.length() = " + candidate.length() + "\n");
section: Imported - java2s Archive
order: 2230
source: https://web.archive.org/web/20140829090940/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Anegativebehindahead.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class NegativeLookBehindExample {
  public static void main(String args[]) throws Exception {
    String regex = "(and)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "candidate";
    Matcher matcher = pattern.matcher(candidate);
    String msg = "";
    int counter = 0;
    String tmp = null;
    while (matcher.find()) {
      int start = matcher.start();
      int end = matcher.end();
      tmp = ":" + matcher.group() + ":";
      msg += tmp;
      System.out.println("counter = " + counter);
      counter++;
      System.out.println("start = " + start);
      System.out.println("end = " + end);
      System.out.println("tmp = " + tmp);
      System.out.println("candidate.length() = " + candidate.length() + "\n");
    }
  }
}
/**/
java title=Example.java
counter = 0
start = 1
end = 4
tmp = :and:
candidate.length() = 9
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
