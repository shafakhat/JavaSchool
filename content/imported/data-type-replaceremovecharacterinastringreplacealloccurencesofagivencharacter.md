---
title: Replace/remove character in a String
nav: Replace/remove character i...
description: Imported from the java2s.com archive: Replace/remove character in a String
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ReplaceremovecharacterinaStringreplacealloccurencesofagivencharacter.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    String myString = "'''";
    String tmpString = myString.replace('\'', '*');
    System.out.println("Original = " + myString);
    System.out.println("Result   = " + tmpString);
  }
}
/*
Original = '''
Result   = ***
*/
```
