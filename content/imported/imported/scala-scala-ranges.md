---
title: Scala Tutorial - Scala Ranges
nav: Scala Tutorial - Scala Ran...
description: Some code need to create a sequence of numbers from some start to finish. A Range literal is what we need.
section: Imported - java2s Archive
order: 50087
source: https://www.java2s.com/Tutorials/Java/Scala/0180__Scala_Ranges.html
---
```java title=Example.java
« Previous
```

- Next »

Some code need to create a sequence of numbers from some start to finish. A Range literal is what we need.

Ranges can be defined by their start, their end, and the stepping value.

To create a range in Scala, use the predefined the method to as illustrated in the following code:

```java title=Example.java

object Main {
  def main(args: Array[String]) {
    println(1 to 5  )
  }
}
```

We can also create a range with the upper limit exclusive of its upper limit using the predefined method until as shown in the following code.

```java title=Example.java

object Main {
  def main(args: Array[String]) {
    println(1 until 5 )
  }
}
```

For 1 to 5, a Range(1,2,3,4,5) is created, but for 1 until 5 a Range with upper limit exclusive Range(1,2,3,4) is created.

We can also create a Range with stepping values using the predefined method by as shown in the following code.

```java title=Example.java

object Main {
  def main(args: Array[String]) {
    println(1 to 20 by 4  )
  }
}
```

## Example

The following examples show how to create ranges for the types that support them, Int, Long, Float, Double, Char, BigInt, and BigDecimal.

```java title=Example.java

object Main {
  def main(args: Array[String]) {
     var v = 1 to 10        // Int range inclusive, interval of 1, (1 to  10)
     println(v)
     v = 1 until 10        // Int range exclusive, interval of 1, (1 to 9)
     println(v)
     val v1 = 1 to 10 by 3           // Int range inclusive, every third.
     println(v1)
     val v2 = 10 to 1 by -3          // Int range inclusive, every third, counting down.
     println(v2)
     val v3 = 1L to 10L by 3         // Long
     println(v3)
     val v4 = 1.1f to 10.3f by 3.1f  // Float with an interval != 1
     println(v4)
     val v5 = 1.1f to 10.3f by 0.5f  // Float with an interval < 1
     println(v5)
     val v6 = 1.1 to 10.3 by 3.1     // Double
     println(v6)
     val v7 = 'a' to 'g ' by 3         // Char
     println(v7)
     val v8 = BigInt(1) to BigInt(10) by 3
     println(v8)
     val v9 = BigDecimal(1.1) to BigDecimal(10.3) by 3.1
     println(v9)
  }
}
```

## Note

You can create ranges with an inclusive or exclusive upper bound, and you can specify an interval not equal to one:

- Next »
- « Previous
