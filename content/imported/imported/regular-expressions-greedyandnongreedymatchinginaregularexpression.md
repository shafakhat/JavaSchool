---
title: Greedy and Nongreedy Matching in a Regular Expression
nav: Greedy and Nongreedy Match...
description: public static String find(String patternStr, CharSequence input) {
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20100206192702/http://java2s.com/Code/Java/Regular-Expressions/GreedyandNongreedyMatchinginaRegularExpression.htm
---
Greedy and Nongreedy Matching in a Regular Expression

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Greedy quantifiers
    String match = find("A.*c", "AbcAbc");
    match = find("A.+", "AbcAbc");
  }
  public static String find(String patternStr, CharSequence input) {
    Pattern pattern = Pattern.compile(patternStr);
    Matcher matcher = pattern.matcher(input);
    if (matcher.find()) {
      return matcher.group();
    }
    return null;
  }
}
```

1.  Greedy Qualifier
---  ---
2.  Reluctant Qualifier Example
3.  Nongreedy quantifiers
