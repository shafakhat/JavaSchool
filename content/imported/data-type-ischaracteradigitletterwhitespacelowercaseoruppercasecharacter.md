---
title: Is character a digit, letter, white space, lower case or upper case character
nav: Is character a digit, lett...
description: Imported from the java2s.com archive: Is character a digit, letter, white space, lower case or upper case character
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Ischaracteradigitletterwhitespacelowercaseoruppercasecharacter.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    char a[] = { 'a', 'b', '5', '?', 'A', ' ' };
    for (int i = 0; i < a.length; i++) {
      if (Character.isDigit(a[i]))
        System.out.println(a[i] + "is a digit ");
      if (Character.isLetter(a[i]))
        System.out.println(a[i] + "is a letter ");
      if (Character.isWhitespace(a[i]))
        System.out.println(a[i] + "is a White Space ");
      if (Character.isLowerCase(a[i]))
        System.out.println(a[i] + "is a lower case ");
      if (Character.isLowerCase(a[i]))
        System.out.println(a[i] + "is a upper case ");
    }
  }
}
```
