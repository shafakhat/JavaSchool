---
title: Find duplication
nav: Find duplication
description: Find duplication : Java examples (example source code) » Regular Expressions » Validation
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20060513094113/http://www.java2s.com/Code/Java/Regular-Expressions/Findduplication.htm
---
Find duplication : Java examples (example source code) » Regular Expressions » Validation

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
public class MatchDuplicateWords {
  public static void main(String args[]) {
    hasDuplicate("pizza pizza");
    hasDuplicate("Faster pussycat kill kill");
    hasDuplicate("The mayor of of simpleton");
    hasDuplicate("Never Never Never Never Never");
    hasDuplicate("222 2222");
    hasDuplicate("sara sarah");
    hasDuplicate("Faster pussycat kill, kill");
    hasDuplicate(". .");
  }
  public static boolean hasDuplicate(String phrase) {
    boolean retval = false;
    String duplicatePattern = "\\b(\\w+) \\1\\b";
    Pattern p = null;
    try {
      p = Pattern.compile(duplicatePattern);
    } catch (PatternSyntaxException pex) {
      pex.printStackTrace();
      System.exit(0);
    }
    int matches = 0;
    Matcher m = p.matcher(phrase);
    String val = null;
    while (m.find()) {
      retval = true;
      val = ":" + m.group() + ":";
      System.out.println(val);
      matches++;
    }
    String msg = "   NO MATCH: pattern:" + phrase
        + "\r\n             regex: " + duplicatePattern;
    if (retval) {
      msg = " MATCH     : pattern:" + phrase + "\r\n         regex: "
          + duplicatePattern;
    }
    System.out.println(msg + "\r\n");
    return retval;
  }
}
```

Related examples in the same category
---
1. Simplest validation
2. Validation with Pattern and Matcher
