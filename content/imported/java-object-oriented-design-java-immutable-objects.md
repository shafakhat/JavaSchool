---
title: Java Object Oriented Design - Java Immutable Objects
nav: Java Object Oriented Desig...
description: An object whose state cannot be changed after it is created is called an immutable object.
section: Imported - java2s Archive
order: 50158
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0220__Java_Immutable_Objects.html
---
An object whose state cannot be changed after it is created is called an immutable object.

A class whose objects are immutable is called an immutable class.

An immutable object can be shared by different areas of a program without worrying about its state changes.

An immutable object is inherently thread-safe.

## Example

The following code creates an Example of an Immutable Class.

```java title=Example.java
publicclass  IntWrapper {
    privatefinalint  value;
public IntWrapper(int value) {
        this.value = value;
    }
    publicint  getValue() {
        return value;
    }
}
```

## Note

This is how you create an object of the IntWrapper class:

```java title=Example.java
IntWrapper wrapper  = new IntWrapper(101);
```

At this point, the wrapper object holds 101 and there is no way to change it.

Therefore, the IntWrapper class is an immutable class and its objects are immutable objects.

It is good practice to declare all instance variables final so the Java compiler will enforce the immutability during compile time.

- « Previous
