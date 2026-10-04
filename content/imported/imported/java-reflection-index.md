---
title: Java Reflection Overview
nav: Java Reflection Overview
description: Reflection is the ability of a program to query and modify its state during the execution.
section: Imported - java2s Archive
order: 50008
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/index.html
---
## What Is Reflection?

Reflection is the ability of a program to query and modify its state during the execution.

In Java we can obtain information about the fields, methods, modifiers, and the superclass of a class at runtime.

We can also create an instance of a class whose name is not known until runtime, invoke methods on instances, and get/set its fields.

In Java we cannot change the data structure at runtime. For example, we cannot add a new field to an object at runtime.

In Java we cannot change a class's method code at runtime and we cannot add a new method to a class at runtime.

## Reflection API

The reflection facility in Java is provided through the reflection API.

Most of the reflection API classes and interfaces are in the java.lang.reflect package.

The Class class, core reflection class in Java, is in the java.lang package.

Some of the frequently used classes in reflection are listed in following table.

Class Name  Description
---  ---
java.lang.Class  Represent a single class loaded by a class loader in the JVM.
java.lang.reflect.Field  Represent a single field of a class or an interface.
java.lang.reflect.Constructor  Represent a single constructor of a class.
java.lang.reflect.Method  Represent a method of a class or an interface.
java.lang.reflect.Modifier  Decode the access modifiers for a class and its members.
java.lang.reflect.Array  Create arrays at runtime.

## Example Usage

With Java reflection we can do the following tasks.

- Get the class name of the object
- Get class package name, access modifiers, etc.
- Get the methods defined in the class, their return type, access modifiers, parameters type, parameter names(JDK 8), etc.
- Get field
- Get all constructors
- Create an object of the class using one of its constructors.
- Invoke method with the method's name and method's parameter types.
- Create an array of a type dynamically at runtime and manipulate its elements.
