---
title: Java Object Oriented Design - Java interface Fields
nav: Java Object Oriented Desig...
description: An interface cannot have mutable instance and class variables. Unlike a class, an interface cannot be instantiated. All members of an interface are implicitly public.
section: Imported - java2s Archive
order: 50180
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0510__Java_interface_fields.html
---
```java title=Example.java
```

An interface can have three types of members:

- Constant fields
- Abstract, static, and default methods
- Static types as nested interfaces and classes

An interface cannot have mutable instance and class variables. Unlike a class, an interface cannot be instantiated. All members of an interface are implicitly public.

## Constant Fields Declarations

We can declare constant fields in an interface as follows. It declares an interface named Choices, which has declarations of two fields: YES and NO. Both are of int data type.

```java title=Example.java
publicinterface  Choices   {
    publicstaticfinal int YES  = 1;
    publicstaticfinal int NO  = 2;
}
```

All fields in an interface are implicitly public, static, and final.

The Choices interface can be declared as follows without changing its meaning:

```java title=Example.java
publicinterface  Choices   {
    int YES  = 1;
    int NO  = 2;
}
```

You can access the fields in an interface using the dot notation in the form of

```java title=Example.java

<interface-name>.<field-name>
```

You can use Choices.YES and Choices.NO to access the values of YES and NO fields in the Choices interface.

The following code demonstrates how to use the dot notation to access fields of an interface.

```java title=Example.java
publicclass ChoicesTest {
  publicstatic void main(String[] args) {
    System.out.println("Choices.YES = " + Choices.YES);
    System.out.println("Choices.NO = " + Choices.NO);
  }
}
```

Fields in an interface are always final whether the keyword final is used in its declaration or not. We must initialize a field at the time of declaration.

We can initialize a field with a compile-time or runtime constant expression. Since a final field is assigned a value only once, we cannot set the value of the field of an interface, except in its declaration.

The following code shows some valid and invalid field declarations for an interface:

```java title=Example.java
publicinterface ValidFields {
  int X = 10;
  int Y = X;
  double N = X + 10.5;
  boolean YES = true;
  boolean NO = false;
  Test TEST = new Test();
}
```

It is a convention to use all uppercase letters in the name of a field in an interface to indicate that they are constants.

The fields of an interface are always public.

- « Previous
