---
title: Autoboxing/Unboxing Boolean and Character Values
nav: Autoboxing/Unboxing Boolea...
description: Imported from the java2s.com archive: Autoboxing/Unboxing Boolean and Character Values
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AutoboxingUnboxingBooleanandCharacterValues.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Boolean booleanObject = true;
    if (booleanObject){
      System.out.println("b is true");
    }
    Character ch = 'x'; // box a char
char ch2 = ch; // unbox a char
    System.out.println("ch2 is " + ch2);
  }
}
```

```java title=Example.java
b is true
ch2 is x
```
