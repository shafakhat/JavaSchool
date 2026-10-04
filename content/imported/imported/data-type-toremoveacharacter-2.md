---
title: To remove a character
nav: To remove a character
description: Imported from the java2s.com archive: To remove a character
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20100714192003/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Toremoveacharacter.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    String str = "this is a test";
    System.out.println(removeChar(str,'s'));
  }
  public static String removeChar(String s, char c) {
    String r = "";
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) != c)
        r += s.charAt(i);
    }
    return r;
  }
}
//thi i a tet
```
