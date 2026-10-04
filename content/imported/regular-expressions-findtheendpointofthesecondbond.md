---
title: Find the end point of the second 'B(ond)'
nav: Find the end point of the ...
description: String matchHelper[] = { " ^", " ^", " ^",
section: Imported - java2s Archive
order: 2265
source: https://web.archive.org/web/20140608093523/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/FindtheendpointofthesecondBond.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("B(on)d");
    String candidateString = "My name is Bond. James Bond.";
    String matchHelper[] = { "               ^", "              ^", "                           ^",
        "                          ^" };
    Matcher matcher = p.matcher(candidateString);
    matcher.find();
    int endIndex = matcher.end(0);
    System.out.println(candidateString);
    System.out.println(matchHelper[2] + endIndex);
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
