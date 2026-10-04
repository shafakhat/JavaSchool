---
title: Scala Tutorial - Scala Type Hierarchy
nav: Scala Tutorial - Scala Typ...
description: All data types in Scala are objects that have methods to operate on their data.
section: Imported - java2s Archive
order: 50079
source: https://www.java2s.com/Tutorials/Java/Scala/0100__Scala_Type_Hierarchy.html
---
Unlike Java, there are no primitive types in Scala.

All data types in Scala are objects that have methods to operate on their data.

All Scala's types exist as part of a type hierarchy.

Every class that you define in Scala will also belong to this hierarchy automatically.

```java title=Example.java
Any
 +---AnyVAl
 |     +---Numberic Types
 |     +---Char
 |     +---Boolean
 +---AnyRef
       +---Collections
       +---Classes
       |     +---Null
       +---String
```

## Any, AnyVal and AnyRef Types

Class Any is the root of the Scala class hierarchy and is an abstract class.

Every class in a Scala inherits directly or indirectly from this class.

AnyVal and AnyRef extend Any type. The Any, AnyVal,and AnyRef types are the root of Scala's type hierarchy.

All other types descend from AnyVal and AnyRef.

The types that extend AnyVal are known as value types.

- « Previous
