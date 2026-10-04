---
title: Split a String
nav: Split a String
description: Imported from the java2s.com archive: Split a String
section: Imported - java2s Archive
order: 1316
source: https://web.archive.org/web/20140216121412/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SplitaString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String str = "one,two,three,four,five";
    String[] elements = str.split(",");
    for (int i = 0; i < elements.length; i++)
      System.out.println(elements[i]);
  }
}
/*
one
two
three
four
five
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
