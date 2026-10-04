---
title: Split by dot
nav: Split by dot
description: Imported from the java2s.com archive: Split by dot
section: Imported - java2s Archive
order: 1337
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Splitbydot.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) throws Exception {
    String s = "A.BB.CCC";

    String[] words = s.split("\\.");
    for (String str : words) {
      System.out.println(str);
    }
  }
}
/*
A
BB
CCC
*/
```

| 2.32.1. | Split string |
|---|---|
| 2.32.2. | Split a String |
| 2.32.3. | Using split() with a space can be a problem |
| 2.32.4. | " ".split(" ") generates a NullPointerException |
| 2.32.5. | String.split() is based on regular expression |
| 2.32.6. | String split on multicharacter delimiter |
| 2.32.7. | Split by dot |
| 2.32.8. | Split up a string into multiple strings based on a delimiter |
| 2.32.9. | Splits a string around matches of the given delimiter character. |
| 2.32.10. | Splits the provided text into an array, separator string specified. Returns a maximum of max substrings. |
| 2.32.11. | Splits the provided text into an array, using whitespace as the separator, preserving all tokens, including empty tokens created by adjacent separators. |
