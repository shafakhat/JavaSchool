---
title: To replace one specific character with another throughout a string
nav: To replace one specific ch...
description: String newText = text.replace(' ', '/'); // Modify the string text
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toreplaceonespecificcharacterwithanotherthroughoutastring.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    String text = "To be or not to be, that is the question.";
    String newText = text.replace(' ', '/');     // Modify the string text
    System.out.println(newText);
  }
}
java title=Example.java
To/be/or/not/to/be,/that/is/the/question.
```
