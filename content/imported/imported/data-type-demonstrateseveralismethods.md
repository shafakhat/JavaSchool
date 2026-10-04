---
title: Demonstrate several Is... methods.
nav: Demonstrate several Is... ...
description: Imported from the java2s.com archive: Demonstrate several Is... methods.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DemonstrateseveralIsmethods.htm
---
```java title=Example.java
class IsDemo {
  publicstaticvoid main(String args[]) {
    char a[] = { 'a', 'b', '5', '?', 'A', ' ' };

    for (int i = 0; i < a.length; i++) {
      if (Character.isDigit(a[i]))
        System.out.println(a[i] + " is a digit.");
      if (Character.isLetter(a[i]))
        System.out.println(a[i] + " is a letter.");
      if (Character.isWhitespace(a[i]))
        System.out.println(a[i] + " is whitespace.");
      if (Character.isUpperCase(a[i]))
        System.out.println(a[i] + " is uppercase.");
      if (Character.isLowerCase(a[i]))
        System.out.println(a[i] + " is lowercase.");
    }
  }
}
```
