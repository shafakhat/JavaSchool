---
title: Find the end point of the first sub group (ond)
nav: Find the end point of the ...
description: String matchHelper[] = { " ^", " ^", " ^",
section: Imported - java2s Archive
order: 2238
source: https://web.archive.org/web/20140829082002/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Findtheendpointofthefirstsubgroupond.htm
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
    int nextIndex = matcher.end(1);
    System.out.println(candidateString);
    System.out.println(matchHelper[1] + nextIndex);
  }
}
```

| 8.3.1. | A simple sub group |
|---|---|
| 8.3.2. | Working with simple groups |
| 8.3.3. | Find the end point of the first sub group (ond) |
| 8.3.4. | Finding Every Occurrence of the Letter A |
