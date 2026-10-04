---
title: Java Object Oriented Design - Java Standard Annotations
nav: Java Object Oriented Desig...
description: The following section discusses four of the most commonly used standard annotations which are defined in the java.lang package.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0750__Java_Standard_Annotations.html
---
Java API defines many standard annotation types.

The following section discusses four of the most commonly used standard annotations which are defined in the java.lang package.

- Deprecated
- Override
- SuppressWarnings
- FunctionalInterface

## Deprecated Annotation Type

The deprecated annotation type is a marker annotation type. It marks a deprecated code element.

Using a deprecated program element will cause compiler to generate a warning.

```java title=Example.java
@Deprecatedclass MyClass {
  private MyClass() {
  }
  public static MyClass getInstance() {
    MyClass dt = new MyClass();
    return dt;
  }
}
public class Main {
  public static void main(String[] args) {
    MyClass dt; // Generates a compile-time note
  }
}
```

## Override Annotation Type

The override annotation type is a marker annotation type which can only be used on methods.

It indicates that a method overrides a method declared in its supertype.

If we mean to override a method in a supertype, it is recommended to annotate the overridden method with a @Override annotation.

The compiler will make sure that the annotated method really overrides a method in the supertype.

If the annotated method does not override a method in the supertype, the compiler will generate an error.

```java title=Example.java
class A { public void m1() {
  }
}
class B extends A {
  @Override
  public void m1() {
  }
}
```

## SuppressWarnings Annotation Type

The SuppressWarnings is used to suppress named compiler warnings. It declares one element named value whose data type is an array of String.

```java title=Example.java
import java.util.ArrayList;
public class Main {
  @SuppressWarnings("unchecked")
  public void test() {
    @SuppressWarnings("rawtypes")
    ArrayList list = new ArrayList();
    list.add("Hello"); // The compiler issues an unchecked warning
  }
}
```

## FunctionalInterface Annotation Type

An interface with one abstract method declaration is known as a functional interface.

A compile-time error is generated if the interfaces annotated with this annotation are not functional interfaces.

```java title=Example.java
@FunctionalInterface
interface  MyThread{
    void  run();
}
```

An interface with only one abstract method is a functional interface no matter whether it is annotated with a @FunctionalInterface annotation or not.

## Annotating a Java Package

To annotate a Java Package, create a file named package-info.java, and place the annotated package declaration in it.

The following code shows the contents of the package-info.java file.

```java title=Example.java
// package-info.java
@Version(major=1, minor=0)
package  com.java2s.annotation;
```

- « Previous
