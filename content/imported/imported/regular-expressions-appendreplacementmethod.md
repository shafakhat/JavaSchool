---
title: Append Replacement Method
nav: Append Replacement Method
description: Imported from the java2s.com archive: Append Replacement Method
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20100211073150/http://java2s.com/Code/Java/Regular-Expressions/AppendReplacementMethod.htm
---
Append Replacement Method

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("test");
    StringBuffer sb = new StringBuffer();
    String candidateString = "This is a test.";
    String replacement = "Test";
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    matcher.appendReplacement(sb, replacement);
  }
}
```

1.  REGEX = "a*b"
---  ---
2.  Escaping Special Characters in a Pattern
3.  Removing Line Termination Characters from a String
4.  ReplaceAll Method from Matcher
5.  replaceFirst Method from Matcher
6.  Working with Back References
7.  Regular Expression search and replace program
