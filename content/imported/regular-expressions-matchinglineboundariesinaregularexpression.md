---
title: Matching Line Boundaries in a Regular Expression
nav: Matching Line Boundaries i...
description: Pattern pattern = Pattern.compile(patternStr, Pattern.MULTILINE);
section: Imported - java2s Archive
order: 2267
source: https://web.archive.org/web/20140829094557/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/MatchingLineBoundariesinaRegularExpression.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    CharSequence inputStr = "abc\ndef";
    String patternStr = "abc$";
    // Compile with multiline enabled
    Pattern pattern = Pattern.compile(patternStr, Pattern.MULTILINE);
    Matcher matcher = pattern.matcher(inputStr);
    boolean matchFound = matcher.find(); // true
    // Use an inline modifier to enable multiline mode
    matchFound = pattern.matches(".*abc$.*", "abc\r\ndef"); // false
    matchFound = pattern.matches("(?m).*abc$.*", "abc\r\ndef"); // true
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
