---
title: Match Java source file and file and class name
nav: Match Java source file and...
description: System.out.println("The class [" + classMatcher.group(1) + "] is not public");
section: Imported - java2s Archive
order: 2225
source: https://web.archive.org/web/20140829090557/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/MatchJavasourcefileandfileandclassname.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class RegExpExample {
  public static void main(String args[]) {
    String unadornedClassRE = "^\\s*class (\\w+)";
    String doubleIdentifierRE = "\\b(\\w+)\\s+\\1\\b";
    Pattern classPattern = Pattern.compile(unadornedClassRE);
    Pattern doublePattern = Pattern.compile(doubleIdentifierRE);
    Matcher classMatcher, doubleMatcher;
    String line = " class MainClass";
    classMatcher = classPattern.matcher(line);
    doubleMatcher = doublePattern.matcher(line);
    if (classMatcher.find()) {
      System.out.println("The class [" + classMatcher.group(1) + "] is not public");
    }
    while (doubleMatcher.find()) {
      System.out.println("The word \"" + doubleMatcher.group(1) + "\" occurs twice at position "
          + doubleMatcher.start());
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
