---
title: Java Object Oriented Design - Java Annotation Usage
nav: Java Object Oriented Desig...
description: The supplied value for elements of an annotation must be a compile-time constant expression and we cannot use null as the value for any type of element in an annotation.
section: Imported - java2s Archive
order: 50194
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0730__Java_Annotation_Usage.html
---
```java title=Example.java
« Previous
```

- Next »

The supplied value for elements of an annotation must be a compile-time constant expression and we cannot use null as the value for any type of element in an annotation.

## Primitive Types

The data type of an element in an annotation type could be any of the primitive data types: byte, short, int, long, float, double, boolean, and char.

The Version annotation type declares two elements, major and minor, and both are of int data type.

The following code declares an annotation type:

```java title=Example.java
public @interface MyAnnotation {
  byte a();/*www.java2s.com*/short b();
  int c();
  long d();
  float e();
  double f();
  boolean g();
  char h();
}
```

```java title=Example.java

@MyAnnotation(a=1, b=2,  c=3,  d=4,  e=12.34F, f=1.89, g=true, h='Y')
```

We can use a compile-time constant expression to specify the value for an element of an annotation.

The following two instances of the Version annotation are valid:

```java title=Example.java

@Version(major=2+1, minor=(int)13.2)
@Version(major=3, minor=13)
```

## String Types

We can use an element of the String type in an annotation type.

The following code defines an annotation type called Name. It has two elements, first and last, which are of the String type.

```java title=Example.java
public @interface Name  {
   String first(); //fromwww.java2s.com
   String last();
}
@Name(first="Tom", last="Smith")
publicclass NameTest {
    @Name(first="Jack", last="Iaan")
    publicvoid  aMethod()   {
    }
}
```

It is valid to use the string concatenation operator + in the value expression for an element of a String type.

```java title=Example.java

@Name(first="Ja" + "ck", last="Ia" + "an")
```

## Class Types

The following code shows how to use Class type as the annotation value.

```java title=Example.java
import java.io.IOException;
/*www.java2s.com*/
@interface MyAnnotation {
  Class<? extends Throwable> willThrow() default java.lang.Throwable.class;
}
publicclass Main {
  @MyAnnotation(willThrow = IOException.class)
  publicstaticvoid testCase1() {
    // Code goes here
  }
  @MyAnnotation()
  publicstaticvoid testCase2() {
  }
}
```

## Enum Type

An annotation can have elements of an enum type.

```java title=Example.java
enum Level {/*www.java2s.com*/
  PENDING, FAILED, PASSED;
}
@interface Review {
  Level status() default Level.PENDING;
  String comments() default"";
}
@Review(status = Level.PASSED)
publicclass Main {
}
```

## Annotation Type

We can use an annotation type as the type of an element inside another annotation type's declaration.

To provide a value for an element of an annotation type, use the syntax that is used to create an annotation type instance.

```java title=Example.java

@interface Name {
  String first();//www.java2s.com
  String last();
}
@interface Version {
  int major();
  int minor() default 0; // zero as default value for minor
}
@interface Description {
  Name name();
  Version version();
  String comments() default"";
}
@Description(name = @Name(first = "Tom", last = "Smith"), version = @Version(major = 1, minor = 2), comments = "Just a  test class")
publicclass Main {
}
```

## Array Type Annotation Element

An annotation can have elements of an array type. The array type could be of one of the following types:

- A primitive type
- java.lang.String type
- java.lang.Class type
- An enum type
- An annotation type

We need to specify the value for an array element inside braces.

Elements of the array are separated by a comma.

```java title=Example.java

@interface ItemList {
  String[] items();
}
@ItemList(items = { "A", "B" })
publicclass Main {
}
```

If you have only one element in the array, it is allowed to omit the braces.

```java title=Example.java

@ToDo(items={"A"})
@ToDo(items="A")
```

To pass in an empty array

```java title=Example.java

@ToDo(items={})
```

## Shorthand Annotation Syntax

Suppose we have an annotation type as follows.

```java title=Example.java
public  @interface Enabled  {
    boolean status() default true;
}
```

To annotate a program element with the Enabled annotation type with the default value, we can use the @Enabled() syntax.

We do not need to specify the values for the status element because it has a default value.

We can further omit the parentheses.

```java title=Example.java

@Enabled
publicclass Main {
}
@Enabled()
publicclass Main {
}
```

An annotation type with only one element has a shorthand syntax.

If an annotation type has only one element with named value, we can omit the name from name=value pair.

The following code declares a Company annotation type, which has only one element named value:

```java title=Example.java
public  @interface Company  {
    String value();
}
```

We can omit the name from name=value pair when using the Company annotation.

```java title=Example.java

@Company(value="Inc.")
publicclass Test   {
}
```

becomes

```java title=Example.java

@Company("Inc.")
publicclass Test   {
}
```

The following code shows how to use this shorthand if the element data type is an array.

```java title=Example.java
public  @interface Item   {
    String[] value();
}
@Item({"A", "B"})
publicclass Test   {
}
```

We can further omit the braces if we specify only one element in the array annotation type.

```java title=Example.java

@Item("A")
publicclass Test   {
}
```

If we supply only one value when using an annotation, the name of the element is assumed value.

- Next »
- « Previous
