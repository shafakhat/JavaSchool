---
title: Working with simple groups
nav: Working with simple groups
description: Imported from the java2s.com archive: Working with simple groups
section: Imported - java2s Archive
order: 2237
source: https://web.archive.org/web/20140829082010/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Workingwithsimplegroups.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    Pattern p = Pattern.compile("\\w\\d");
    String candidate = "A6 is my favorite";
    Matcher matcher = p.matcher(candidate);
    if (matcher.find()) {
      String tmp = matcher.group(0);
      System.out.println(tmp);
    }
  }
}
```

| 8.3.1. | A simple sub group |
|---|---|
| 8.3.2. | Working with simple groups |
| 8.3.3. | Find the end point of the first sub group (ond) |
| 8.3.4. | Finding Every Occurrence of the Letter A |
