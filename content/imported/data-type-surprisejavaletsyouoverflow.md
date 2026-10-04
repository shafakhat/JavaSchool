---
title: Surprise! Java lets you overflow
nav: Surprise! Java lets you ov...
description: Imported from the java2s.com archive: Surprise! Java lets you overflow
section: Imported - java2s Archive
order: 1335
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/SurpriseJavaletsyouoverflow.htm
---
```java title=Example.java
public class MainClass {

  public static void main(String[] args) {
    int big = 0x7fffffff; // max int value
    System.out.println("big = " + big);
    int bigger = big * 4;
    System.out.println("bigger = " + bigger);
  }
}
```

```java title=Example.java
big = 2147483647
bigger = -4
```

| 2.1.1. | The Primitive Types |
|---|---|
| 2.1.2. | Size for Java's Primitive Types |
| 2.1.3. | Default values for primitives and references |
| 2.1.4. | Literals |
| 2.1.5. | Surprise! Java lets you overflow |
| 2.1.6. | Wrapping a Primitive Type in a Wrapper Object: boolean, byte, char, short, int, long, float, double |
| 2.1.7. | Print the limits of primitive types (e.g. byte, short, int ...) in Java |
| 2.1.8. | Get the minimum and maximum value of a primitive data types |
| 2.1.9. | Shows default initial values |
| 2.1.10. | Primitive utilities |
| 2.1.11. | Return primitive type the passed in wrapper type corresponds to |
