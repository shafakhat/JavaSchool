---
title: Demonstrates usage of the Pattern split method
nav: Demonstrates usage of the ...
description: Imported from the java2s.com archive: Demonstrates usage of the Pattern split method
section: Imported - java2s Archive
order: 2255
source: https://web.archive.org/web/20140829080728/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/DemonstratesusageofthePatternsplitmethod.htm
---
```java title=Example.java
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String args[]) {
    String statement = "a b c d e f g h i j k l";
    String splitPattern = "e|c|a|a|(a b d e)|(b c e)";
    Pattern p = Pattern.compile(splitPattern);
    String[] tokens = p.split(statement);
    for (int i = 0; i < tokens.length; i++) {
      System.out.println(tokens[i]);
    }
  }
}
```

8.7.1.  Demonstrates usage of the Pattern split method
