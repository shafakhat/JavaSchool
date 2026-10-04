---
title: Using Constructors
nav: Using Constructors
description: Imported from the java2s.com archive: Using Constructors
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20070314221356/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/UsingConstructors.htm
---
- Every class must have at least one constructor.
- If there is no constructors for your class, the compiler will supply a default constructor(no-arg constructor).
- A constructor is used to construct an object.
- A constructor looks like a method and is sometimes called a constructor method.
- A constructor never returns a value
- A constructor always has the same name as the class.
- A constructor may have zero argument, in which case it is called a no-argument (or no-arg, for short) constructor.
- Constructor arguments can be used to initialize the fields in the object.

The syntax for a constructor is as follows.

```java title=Example.java
constructorName (listOfArguments) {
    [constructor body]
}
```

```java title=Example.java
public class MainClass {
  double radius;
  // Class constructor
  MainClass(double theRadius) {
    radius = theRadius;
  }
}
```
