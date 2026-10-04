---
title: Java Arithmetic Operator calculate leap year
nav: Java Arithmetic Operator c...
description: if ((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0)))
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/20210102113215/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-leap-year.html
---
## Question

We would like to check if a year is a leap year.

For example, year 2000 is a leap year

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int year = 2004;
    //your code
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int year = 2004;
    if ((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0)))
      System.out.println("Year " + year + " is a leap year");
    elseSystem.out.println("Year " + year + " is not a leap year");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate cylinder volume
- Java Arithmetic Operator calculate distance of two points
- Java Arithmetic Operator calculate floating point value
- Java Arithmetic Operator calculate minutes and seconds
- Java Arithmetic Operator calculate on integer
