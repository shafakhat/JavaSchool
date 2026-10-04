---
title: Scala Tutorial - Scala while Loops
nav: Scala Tutorial - Scala whi...
description: The while loop executes a block of code as long as a condition is true.
section: Imported - java2s Archive
order: 50093
source: https://www.java2s.com/Tutorials/Java/Scala/0240__Scala_while_Loops.html
---
The while loop executes a block of code as long as a condition is true.

The following code prints out a complaint once a day until the next Friday the 13th has arrived:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     import java.util.Calendar
     def isFridayThirteen(cal: Calendar): Boolean = {
       val dayOfWeek = cal.get(Calendar.DAY_OF_WEEK)
       val dayOfMonth = cal.get(Calendar.DAY_OF_MONTH)
       (dayOfWeek == Calendar.FRIDAY) && (dayOfMonth == 13)
     }
     while (!isFridayThirteen(Calendar.getInstance())) {
       println("Today isn't Friday the 13th. Lame.")
       Thread.sleep(86400000)
     }
  }
}
```

## Scala do-while Loops

A do-while loop executes some code while a conditional expression is true.

That is, the do-while checks to see if the condition is true after running the block.

To count up to 10, we could write this:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     var count = 0
     do {
       count += 1
       println(count)
     } while (count < 10)
  }
}
```

- « Previous
