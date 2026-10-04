---
title: Scala Tutorial - Scala try expressions
nav: Scala Tutorial - Scala try...
description: Exception handling in Scala is implemented differently, but it behaves exactly like Java and works seamlessly with existing Java libraries.
section: Imported - java2s Archive
order: 50094
source: https://www.java2s.com/Tutorials/Java/Scala/0250__Scala_try_expressions.html
---
```java title=Example.java
« Previous
```

- Next »

Exception handling in Scala is implemented differently, but it behaves exactly like Java and works seamlessly with existing Java libraries.

All exceptions in Scala are unchecked; there is no concept of checked exception.

Throwing exceptions is the same in Scala and Java.

```java title=Example.java

throw new Exception("some exception...")
```

The try/finally construct is also the same in Scala and Java as shown in the following code.

```java title=Example.java

try {
    throw newException("some exception...")
} finally{
    println("This will always be printed")
}
```

try/catch in Scala is an expression that results in a value.

The exception in Scala can be pattern matched in the catch block instead of providing a separate catch clause for each different exception.

Because try/catch in Scala is an expression, it becomes possible to wrap a call in a try/catch and assign a default value if the call fails.

The following code shows a basic try/catch expression with pattern matched catch block.

```java title=Example.java

try {
    file.write(stuff)
} catch{
    case e:java.io.IOException => // handle IO Exception
    case n:NullPointerException => // handle null pointer
}
```

## Example

The following code shows an example of wrapping a call in try/catch by calling Integer.parseIntand assigning a default if the call fails.

```java title=Example.java

try{
   Integer.parseInt("dog")
}catch{
   case_ => 0
}
```

- Next »
- « Previous
