---
title: Scala Tutorial - Scala Numeric Types
nav: Scala Tutorial - Scala Num...
description: The numeric data types in Scala constitute Float and Double types along with Integral data types such as Byte, Short, Int, Long, and Char.
section: Imported - java2s Archive
order: 50083
source: https://www.java2s.com/Tutorials/Java/Scala/0140__Scala_Numeric_Types.html
---
```java title=Example.java
```

The numeric data types in Scala constitute Float and Double types along with Integral data types such as Byte, Short, Int, Long, and Char.

The following table displays Scala's numeric data types.

Data type  Description
---  ---
Byte  Integers in the range from -128 to 127
Short  Integers in the range from -32768 to 32767
Int  Integers in the range from -2147483648 to 2147483647
Long  Integers in the range from -9223372036854775808 to 9223372036854775807
Float  The largest positive finite float is 3.4028235*10 38 and thesmallest positive finite nonzero float is 1.40*10 -45
Double  The largest positive finite double is 1.7976931348623157*10 308 and the smallest positive finite nonzero double is 4.9*10 -324

## Example

Scala can automatically convert numbers from one type to another in the order.

```java title=Example.java
Byte . Short . Int . Long . Float . Double.
```

where the Byte type is the lowest and can be converted to any other type as illustrated in the following example:

```java title=Example.java
val x: Byte = 30
```

We can assign x to a Short type as illustrated in the following example:

```java title=Example.java
val y: Short = x
```

Likewise we can assign x to an Int, Long, Float, Double, and Scala will automatically convert the numbers for you as illustrated in the following example:

```java title=Example.java
val z: Double = y
```

Scala does not allow automatic conversion in the order reverse from mentioned earlier.

- « Previous
