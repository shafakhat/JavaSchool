---
title: Count letters in a String
nav: Count letters in a String
description: Imported from the java2s.com archive: Count letters in a String
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CountlettersinaString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String str = "12345";
    int counter = 0;
    for (int i = 0; i < str.length(); i++) {
      if (Character.isLetter(str.charAt(i)))
        counter++;
    }
    System.out.println(counter + " letters.");
  }
}
//0 letters.
```
