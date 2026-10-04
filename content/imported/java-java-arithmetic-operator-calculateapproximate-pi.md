---
title: Java Arithmetic Operator calculate/approximate PI
nav: Java Arithmetic Operator c...
description: }//ww w .ja v a 2s . co m private static double approximatePi(int index) {
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-arithmetic-operator-calculateapproximate-pi.html
---
## Question

Pi can be computed using the following formula:

```java title=Example.java
pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
```

We would like to write a program that displays the result of

```java title=Example.java
4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
```

and

```java title=Example.java
4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13)
java title=Example.java
public class Main{
  public static void main(String[] args) {
    System.out.println(4 * (1.0 - (1 / 3) + (1 / 5) -
              (1 / 7) + (1 / 9) - (1 / 11)));
    System.out.println(4 * (1.0 - (1 / 3) + (1 / 5) - (1 / 7)
               + (1 / 9) - (1 / 11) + (1 / 13)));
  }
}
```

## Note

We can also use loop:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.println(approximatePi(11));
    System.out.println(approximatePi(13));
  }private static double approximatePi(int index) {
    boolean positive = true;
    double sum = 0.0;
    for (int i = 1; i <= index; i += 2) {
      if (positive) {
        sum += (1.0 / i);
        positive = false;
      } else {
        sum -= (1.0 / i);
        positive = true;
      }
    }
    return 4.0 * sum;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate on integer
- Java Arithmetic Operator calculate pentagonal numbers
- Java Arithmetic Operator calculate tips
- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
