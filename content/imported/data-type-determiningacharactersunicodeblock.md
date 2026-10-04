---
title: Determining a Character's Unicode Block
nav: Determining a Character's ...
description: Character.UnicodeBlock block = Character.UnicodeBlock.of(ch);
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminingaCharactersUnicodeBlock.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    char ch = '\u5639';
    Character.UnicodeBlock block = Character.UnicodeBlock.of(ch);
  }
}
```
