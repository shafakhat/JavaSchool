---
title: String Characters
nav: String Characters
description: if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringCharacters.htm
---
```java title=Example.java
public class StringCharacters {
  public static void main(String[] args) {
    String text = "To be or not to be?";
    int spaces = 0,
    vowels = 0,
    letters = 0;
    for (int i = 0; i < text.length(); i++) {
      char ch = Character.toLowerCase(text.charAt(i));
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
        ++vowels;
      if (Character.isLetter(ch))
        ++letters;
      if (Character.isWhitespace(ch))
        ++spaces;
    }
  }
}
```
