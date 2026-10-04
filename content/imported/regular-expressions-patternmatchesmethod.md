---
title: Pattern.matches method
nav: Pattern.matches method
description: Imported from the java2s.com archive: Pattern.matches method
section: Imported - java2s Archive
order: 2272
source: https://web.archive.org/web/20140608093447/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Patternmatchesmethod.htm
---
```java title=Example.java
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String regex = "ad*";
    String input = "add";
    boolean isMatch = Pattern.matches(regex, input);
    System.out.println(isMatch);
  }
}
```

| 8.6.1. | Pattern.matches method |
|---|---|
| 8.6.2. | Find the end point of the second 'B(ond)' |
| 8.6.3. | Match Duplicate Words |
| 8.6.4. | Validate email address |
| 8.6.5. | Matching Line Boundaries in a Regular Expression |
| 8.6.6. | Regex for IP v4 Address |
| 8.6.7. | Regex for IP v6 Address |
