---
title: Autoboxing/unboxing a Boolean and Character.
nav: Autoboxing/unboxing a Bool...
description: Imported from the java2s.com archive: Autoboxing/unboxing a Boolean and Character.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AutoboxingunboxingaBooleanandCharacter.htm
---
```java title=Example.java
class AutoBox5 {
  publicstaticvoid main(String args[]) {

    Boolean b = true;

    if (b)
      System.out.println("b is true");

    Character ch = 'x'; // box a char
char ch2 = ch; // unbox a char

    System.out.println("ch2 is " + ch2);
  }
}
```
