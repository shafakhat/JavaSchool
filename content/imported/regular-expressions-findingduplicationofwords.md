---
title: Finding duplication of words
nav: Finding duplication of words
description: Imported from the java2s.com archive: Finding duplication of words
section: Imported - java2s Archive
order: 2258
source: https://web.archive.org/web/20140828212251/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Findingduplicationofwords.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
public class MainClass {
  public static void main(String args[]) {
    String phrase = "a word word";
    String duplicatePattern = "\\b(\\w+) \\1\\b";
    Pattern p = null;
    try {
      p = Pattern.compile(duplicatePattern);
    } catch (PatternSyntaxException pex) {
      pex.printStackTrace();
      System.exit(0);
    }
    // count the number of matches.
    int matches = 0;
    // get the matcher
    Matcher m = p.matcher(phrase);
    String val = null;
    // find all matching Strings
    while (m.find()) {
      val = ":" + m.group() + ":";
      System.out.println(val);
      matches++;
    }
  }
}
```

| 8.10.1. | Primitive address validation |
|---|---|
| 8.10.2. | Date format consists of one or two digits followed by a hyphen, followed by one or two digits, followed by a hypen, followed by four digits |
| 8.10.3. | Finding duplication of words |
| 8.10.4. | Name validation |
| 8.10.5. | Phone number validation |
| 8.10.6. | Zip code validation |
| 8.10.7. | String manipulation using English synonyms |
| 8.10.8. | Match a digit |
