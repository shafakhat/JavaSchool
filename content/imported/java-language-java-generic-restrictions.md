---
title: Java Tutorial - What are restrictions for Java generic types
nav: Java Tutorial - What are r...
description: It is not possible to create an instance of a type parameter. For example, consider this class:
section: Imported - java2s Archive
order: 50462
source: https://www.java2s.com/Tutorials/Java/Java_Language/8050__Java_generic_restrictions.html
---
```java title=Example.java
```

## Type Parameters Can't Be Instantiated

It is not possible to create an instance of a type parameter. For example, consider this class:

```java title=Example.java
// Can't create an instance of T.
class Gen<T> {
  T ob;
  Gen() {
    ob = new T(); // Illegal!!!
  }
}
```

## Restrictions on Static Members

No static member can use a type parameter declared by the enclosing class. For example, all of the static members of this class are illegal:

```java title=Example.java
class Wrong<T> {
  // Wrong, no static variables of type T.
static T ob;
// Wrong, no static method can use T.
static T getob() {
    return ob;
  }
  // Wrong, no static method can access object of type T.
staticvoid showob() {
    System.out.println(ob);
  }
}
```

You can declare static generic methods with their own type parameters.

## Generic Array Restrictions

You cannot instantiate an array whose base type is a type parameter. You cannot create an array of type specific generic references.

The following short program shows both situations:

```java title=Example.java
class MyClass<T extends Number> {
  T ob;
  T vals[];
  MyClass(T o, T[] nums) {
    ob = o;
    vals = nums;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Integer n[] = { 1 };
    MyClass<Integer> iOb = new MyClass<Integer>(50, n);
    // Can't create an array of type-specific generic references.
// Gen<Integer> gens[] = new Gen<Integer>[10];
    MyClass<?> gens[] = new MyClass<?>[10]; // OK
  }
}
```

- « Previous
