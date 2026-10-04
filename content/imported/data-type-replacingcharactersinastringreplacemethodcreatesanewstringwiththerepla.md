---
title: Replacing Characters in a String
nav: Replacing Characters in a ...
description: Imported from the java2s.com archive: Replacing Characters in a String
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ReplacingCharactersinaStringreplacemethodcreatesanewstringwiththereplacedcharacters.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    String string = "this is a string";
    // Replace all occurrences of 'a' with 'o'
    String newString = string.replace('a', 'o');
    System.out.println(newString);
  }
}
```
