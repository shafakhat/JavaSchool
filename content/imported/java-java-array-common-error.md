---
title: Java Array Common Error
nav: Java Array Common Error
description: Imported from the java2s.com archive: Java Array Common Error
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20210102113251/http://www.java2s.com/ref/java/java-array-common-error.html
---
## Introduction

Identify and fix the errors in the following code:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
     double[100] r;
     for (int i = 0; i < r.length(); i++);
         r(i) = Math.random * 100;
  }
}
java title=Example.java
public class Main {
  public static void main(String[] args) {
     double[100] r; //should be double[] r = new double[100];
                           //no ()
     for (int i = 0; i < r.length(); i++); // no ;
         r(i) = Math.random * 100;
       //r[i]       missing()
  }
}
java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
     double[] r = newdouble[100];
        for (int i = 0; i < r.length; i++)
         r[i] = Math.random() * 100;
  }
}
```

PreviousNext

## Related

- Java Array select random cards from deck
- Java Array shift elements
- Java Array sum all elements
- Java Array multidimensional Arrays
- Java Array multidimensional Arrays declaration
