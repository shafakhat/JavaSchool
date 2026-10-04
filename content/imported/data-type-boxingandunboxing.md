---
title: Boxing and Unboxing
nav: Boxing and Unboxing
description: Boxing refers to the conversion of a primitive to a corresponding wrapper instance, such as from an int to a java.lang.Integer. Unboxing is the conversion of a wrapper in
section: Imported - java2s Archive
order: 1317
source: https://web.archive.org/web/20140829094244/http://www.java2s.com/Tutorial/Java/0040__Data-Type/BoxingandUnboxing.htm
---
Boxing refers to the conversion of a primitive to a corresponding wrapper instance, such as from an int to a java.lang.Integer. Unboxing is the conversion of a wrapper instance to a primitive type, such as from Byte to byte.

```java title=Example.java
public class MainClass{
  public static void main(String[] args){
     Integer number = new Integer (100);
     int [] ints = new int [2];
     ints [0] = number;
  }
}
```

| 2.18.1. | Type conversion (JDK1.5 Autoboxing/Unboxing) |
|---|---|
| 2.18.2. | Boxing and Unboxing |
| 2.18.3. | Autoboxing and Auto-Unboxing |
| 2.18.4. | Manually boxes the value 100 into an Integer |
| 2.18.5. | The modern way to construct an Integer object that has the value 100 |
| 2.18.6. | To unbox an object |
| 2.18.7. | Autoboxing/unboxing: an argument passed to a method or returned from a method |
| 2.18.8. | Autoboxing/unboxing occurs inside expressions |
| 2.18.9. | Auto-unboxing: mix different types of numeric objects in an expression. |
| 2.18.10. | Using an integer object to control a switch statement |
| 2.18.11. | Autoboxing/Unboxing Boolean and Character Values |
| 2.18.12. | Autoboxing/unboxing takes place with method parameters and return values. |
| 2.18.13. | Auto-unboxing allows you to mix different types of numeric objects in an expression. |
