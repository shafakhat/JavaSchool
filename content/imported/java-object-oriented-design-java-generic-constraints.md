---
title: Java Object Oriented Design - Java Generic Constraints
nav: Java Object Oriented Desig...
description: For a generic type, a wildcard type is what an Object type is for a raw type.
section: Imported - java2s Archive
order: 50171
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0360__Java_Generic_Constraints.html
---
## Unbounded Wildcards

A wildcard type is denoted by a question mark, as in <?>.

For a generic type, a wildcard type is what an Object type is for a raw type.

We can assign any generic of known type to a generic of wildcard type.

Here is the sample code:

```java title=Example.java
// MyBag  of  String type
MyBag<String> stringMyBag  = new MyBag<String>("Hi");
// You can  assign a  MyBag<String> to  MyBag<?> type
MyBag<?> wildCardMyBag  = stringMyBag;
```

The question mark in a wildcard generic type (e.g., <?>) denotes an unknown type.

When you declare a parameterized type using a wildcard as a parameter type, it means that it does not know about its type.

```java title=Example.java
MyBag<?> unknownMyBag = new MyBag<String>("Hello");
```

## Upper-Bounded Wildcards

We express the upper bound of a wildcard as

```java title=Example.java
<? extends T>
```

Here, T is a type. <? extends T> means anything that is of type T or its subclass is acceptable.

For example, the upper bound can be the Number type.

If we pass any other type, which is a subclass of the Number type, it is fine. However, anything that is not a Number type or its subclass type should be rejected at compile time.

Using the upper bound as Number, we can define the method as

```java title=Example.java
class MyBag<T> {
  private T ref;public MyBag(T ref) {
    this.ref = ref;
  }
  public T get() {
    return ref;
  }
  publicvoid set(T a) {
    this.ref = a;
  }
}
publicclass Main {
  publicstaticdouble sum(MyBag<? extends Number> n1,
      MyBag<? extends Number> n2) {
    Number num1 = n1.get();
    Number num2 = n2.get();
    double sum = num1.doubleValue() + num2.doubleValue();
    return sum;
  }
}
```

No matter what you pass for n1 and n2, they will always be assignment-compatible with Number since the compiler ensure that the parameters passed to the sum() method follow the rules specified in its declaration of <? extends Number>.

## Lower-Bounded Wildcards

Specifying a lower-bound wildcard is the opposite of specifying an upper-bound wildcard.

The syntax for using a lower-bound wildcard is <? super T>, which means "anything that is a supertype of T."

```java title=Example.java
class MyBag<T> {
  private T ref;public MyBag(T ref) {
    this.ref = ref;
  }
  public T get() {
    return ref;
  }
  publicvoid set(T a) {
    this.ref = a;
  }
}
publicclass Main {
  publicstatic <T> void copy(MyBag<T> source, MyBag<? super T> dest) {
    T value = source.get();
    dest.set(value);
  }
}
```

- « Previous
