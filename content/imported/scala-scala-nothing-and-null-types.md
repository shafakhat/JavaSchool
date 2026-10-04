---
title: Scala Tutorial - Scala Nothing and Null Types
nav: Scala Tutorial - Scala Not...
description: Null is a subtype of all reference types. It is a subtype of all AnyRef types to provide a type for the keyword null.
section: Imported - java2s Archive
order: 50085
source: https://www.java2s.com/Tutorials/Java/Scala/0160__Scala_Nothing_and_Null_Types.html
---
Null is a subtype of all reference types. It is a subtype of all AnyRef types to provide a type for the keyword null.

Scala does not have a null keyword.

For instance, it is not possible to assign null to a variable of type scala.Int.

Nothing provides a compatible return type for operations that affect a program's flow.

One of the usages of Nothing is that it signals abnormal termination.

Any time you feel like using a null, use an Option instead.

- « Previous
