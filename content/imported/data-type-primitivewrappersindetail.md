---
title: Primitive Wrappers in detail
nav: Primitive Wrappers in detail
description: For the sake of performance, not everything in Java is an object. There are also primitives, such as int, long, float, double, etc.
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20140814011034/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PrimitiveWrappersindetail.htm
---
For the sake of performance, not everything in Java is an object. There are also primitives, such as int, long, float, double, etc.
---
java.lang.Integer
The java.lang.Integer class wraps an int. The Integer class has two static final fields of type int: MIN_VALUE and MAX_VALUE. MIN_VALUE contains the minimum possible value for an int (-2^31) and MAX_VALUE the maximum possible value for an int (2^31 - 1).
Integer class has two constructors:

```java title=Example.java
public Integer (int value)
     public Integer (String value)
```

For example, this code constructs two Integer objects.

```java title=Example.java
Integer i1 = new Integer (12);
     Integer i2 = new Integer ("123");
```

Integer has the no-arg byteValue, doubleValue, floatValue, intValue, longValue, and shortValue methods that convert the wrapped value to a byte, double, float, int, long, and short, respectively. In addition, the toString method converts the value to a String.
static methods parse a String to an int (parseInt) and convert an int to a String (toString).

```java title=Example.java
public static int parsetInt (String string)
     public static String toString (int i)
```
