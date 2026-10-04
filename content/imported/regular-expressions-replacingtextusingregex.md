---
title: Replacing text using regex
nav: Replacing text using regex
description: Imported from the java2s.com archive: Replacing text using regex
section: Imported - java2s Archive
order: 2254
source: https://web.archive.org/web/20140829080455/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Replacingtextusingregex.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String regex = "(\\w)(\\d)(\\w+)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "W3C";
    Matcher matcher = pattern.matcher(candidate);
    String tmp = matcher.replaceAll("$33");
    System.out.println("REPLACEMENT: " + tmp);
    System.out.println("ORIGINAL: " + candidate);
  }
}
```

8.9.1.  Replacing text using regex
