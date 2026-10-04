---
title: Scala Tutorial - Scala Import
nav: Scala Tutorial - Scala Imp...
description: To use declarations in packages, we have to import them, just as we do in Java.
section: Imported - java2s Archive
order: 50109
source: https://www.java2s.com/Tutorials/Java/Scala/3090__Scala_Import.html
---
```java title=Example.java
« Previous
```

- Next »

## Importing Types and Their Members

To use declarations in packages, we have to import them, just as we do in Java.

Scala offers additional options, as shown in the following examples that import Java types:

A package is a named module of code.

Java and Scala convention dictates that package names are the reversed domain name of the code owner.

The first non-comment line in the source file:

```java title=Example.java

package com.java2s.stuff
```

Scala packages can be imported so that they can be referenced in the current compilation scope.

The following statement imports the contents of the scala.xml package:

```java title=Example.java

import scala.xml._
```

Import statements are made in the scope of prior imports. The following statement imports the scala.xml.transform package:

```java title=Example.java

import transform._
```

We can import a single class and object, for example, HashMap from the scala.collection.mutable package:

```java title=Example.java

import scala.collection.mutable.HashMap
```

We can import more than one class or object from a single package, for example, TreeMap and TreeSet from the scala.collection.immutable package:

```java title=Example.java

import scala.collection.immutable.{TreeMap, TreeSet}
```

## Example

```java title=Example.java

     import java.awt._
     import java.io.File
     import java.io.File._
     import java.util.{Map, HashMap}
```

We can import all types in a package, using the underscore _ as a wildcard.

We can also import individual Scala or Java types, as shown on the second line.

Java uses the "star" character * as the wildcard for imports.

In Scala, this character is allowed as a method name, so _ is used instead to avoid ambiguity.

The third line imports all the static methods and fields in java.io.File.

The equivalent Java import statement would be import static java.io.File.*;

Finally, we can import a class or object and rename it. For example, you can import the JSON class/object from the scala.util.parsing.json package and rename it to JsonParser:

```java title=Example.java

import scala.util.parsing.json.{JSON=> JsonParser}
```

import can be used inside any codeblock, and the import will be active only in the scope of that code block.

For example, we can import something inside a class body as shown in the following code:

```java title=Example.java

class Frog {
    import scala.xml._
    //
}
```

We can import the methods of an object so that those methods can be used without explicit reference to its object.

This is much like Java's static import.

Combining local scope import and importing objects allows us to fine-tune where the objects and their associated methods are imported.

## Note

Scala doesn't have an import static construct because it treats object types uniformly like other types.

We can put import statements almost anywhere to scope their visibility to just where they are needed.

We can rename types as you import them, and we can suppress the visibility of unwanted types:

```java title=Example.java

     def stuffWithBigInteger() = {
       import java.math.BigInteger.{
         ONE => _,
         TEN,
         ZERO => JAVAZERO }
       println( "TEN: "+TEN )
       println( "ZERO: "+JAVAZERO )
     }
```

## Imports Are Relative

Scala imports are relative.

Note the comments for the following imports:

```java title=Example.java

     import scala.collection.mutable._
     import collection.immutable._              // Since "scala" is already imported
     import _root_.scala.collection.parallel._  // full path from real "root"
```

- Next »
- « Previous
