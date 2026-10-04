---
title: Using the boolean type
nav: Using the boolean type
description: Imported from the java2s.com archive: Using the boolean type
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usingthebooleantype.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    boolean b;
    b = false;
    System.out.println("b is " + b);
    b = true;
    System.out.println("b is " + b);
    // a boolean value can control the if statement
if(b) System.out.println("This is executed.");
    b = false;
    if(b) System.out.println("This is not executed.");
    // outcome of a relational operator is a boolean value
    System.out.println("10 > 9 is " + (10 > 9));
  }
}
```

```java title=Example.java
b is false
b is true
This is executed.
10 > 9 is true
```
