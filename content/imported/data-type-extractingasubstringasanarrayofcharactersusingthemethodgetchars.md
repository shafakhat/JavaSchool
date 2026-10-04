---
title: Extracting a substring as an array of characters using the method getChars()
nav: Extracting a substring as ...
description: Imported from the java2s.com archive: Extracting a substring as an array of characters using the method getChars()
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ExtractingasubstringasanarrayofcharactersusingthemethodgetChars.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    String text = "To be or not to be";
    char[] textArray = newchar[3];
    text.getChars(9, 12, textArray, 0);
    for(char ch: textArray){
      System.out.println(ch);
    }
  }
}
java title=Example.java
n
o
t
```
