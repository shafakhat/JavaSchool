---
title: Scala Tutorial - Scala Code Blocks
nav: Scala Tutorial - Scala Cod...
description: Method and variable definitions can be single lines as follows:
section: Imported - java2s Archive
order: 50077
source: https://www.java2s.com/Tutorials/Java/Scala/0080__Scala_Code_Blocks.html
---
```java title=Example.java
« Previous
```

- Next »

Method and variable definitions can be single lines as follows:

```java title=Example.java

def meth() = "Hello World"
```

Methods and variables also can be defined in code blocks that are denoted by curly braces:{ }.

Code blocks may be nested.

The result of a code block is the last line evaluated in the code block as shown in the following example.

```java title=Example.java

object Main {
    def meth1():String = {"hi"}
    def meth2():String = {
        val d = new java.util.Date()
        d.toString()
    }
  def main(args: Array[String]) {
    println(meth1 )
    println(meth2 )
  }
}
```

Variable definitions can be code blocks as well.

```java title=Example.java

val x3:String= {
    val d = new java.util.Date()
    d.toString()
}
```

- Next »
- « Previous
