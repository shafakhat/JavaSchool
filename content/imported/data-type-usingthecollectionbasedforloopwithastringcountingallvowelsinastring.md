---
title: Using the Collection-Based for Loop with a String
nav: Using the Collection-Based...
description: String phrase = "The quick brown fox jumped over the lazy dog.";
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UsingtheCollectionBasedforLoopwithaStringCountingallvowelsinastring.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    String phrase = "The quick brown fox jumped over the lazy dog.";
    int vowels = 0;
    for(char ch : phrase.toCharArray()) {
      ch = Character.toLowerCase(ch);
      if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        ++vowels;
      }
    }
    System.out.println("The phrase contains " + vowels + " vowels.");
  }
}
java title=Example.java
The phrase contains 12 vowels.
```
