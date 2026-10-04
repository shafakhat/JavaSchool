---
title: Java Tutorial - How to extend Java generic classes
nav: Java Tutorial - How to ext...
description: A generic class can act as a superclass or be a subclass. In a generic hierarchy, any type arguments needed by a generic superclass must be passed up the hierarchy by all
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Language/8030__Java_generic_hierarchy.html
---
A generic class can act as a superclass or be a subclass. In a generic hierarchy, any type arguments needed by a generic superclass must be passed up the hierarchy by all subclasses.

## Example

Using a Generic Superclass

```java title=Example.java
class MyClass<T> {
  T ob;
  MyClass(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
class MySubclass<T, V> extends MyClass<T> {
  V ob2;
  MySubclass(T o, V o2) {
    super(o);
    ob2 = o2;
  }
  V getob2() {
    return ob2;
  }
}
public class Main {
  public static void main(String args[]) {
    MySubclass<String, Integer> x = new MySubclass<String, Integer>("Value is: ", 99);
    System.out.print(x.getob());
    System.out.println(x.getob2());
  }
}
```

The code above generates the following result.

## Example 2

It is perfectly acceptable for a non-generic class to be the superclass of a generic subclass.

```java title=Example.java
class MyClass {int num;
  MyClass(int i) {
    num = i;
  }
  int getnum() {
    return num;
  }
}
class MySubclass<T> extends MyClass {
  T ob;
  MySubclass(T o, int i) {
    super(i);
    ob = o;
  }
  T getob() {
    return ob;
  }
}
public class Main {
  public static void main(String args[]) {
     MySubclass<String> w = new MySubclass<String>("Hello", 4);
    System.out.print(w.getob() + " ");
    System.out.println(w.getnum());
  }
}
```

The code above generates the following result.

## Example 3

The instanceof operator can be applied to objects of generic classes.

```java title=Example.java
class Gen<T> {
  T ob;
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
}
public class Main {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    Gen2<Integer> iOb2 = new Gen2<Integer>(99);
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    System.out.println("iOb2 is instance of Gen2"+(iOb2 instanceof Gen2<?>));
    System.out.println("iOb2 is instance of Gen"+(iOb2 instanceof Gen<?>));
    System.out.println("strOb2 is instance of Gen2"+(strOb2 instanceof Gen2<?>));
    System.out.println("strOb2 is instance of Gen"+(strOb2 instanceof Gen<?>));
    System.out.println("iOb is instance of Gen2"+(iOb instanceof Gen2<?>));
    System.out.println("iOb is instance of Gen"+(iOb instanceof Gen<?>));
  }
}
```

The output:

## Example 4

A method in a generic class can be overridden like any other method.

```java title=Example.java
class Gen<T> {
  T obj;
  Gen(T o) {
    obj = o;
  }
  T getob() {
    System.out.print("Gen's getob(): ");
    return obj;
  }
}
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
  T getob() {
    System.out.print("Gen2's getob(): ");
    return obj;
  }
}
public class Main {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    System.out.println(iOb.getob());
    System.out.println(strOb2.getob());
  }
}
```

The code above generates the following result.

## Java generic types cast

You can cast one instance of a generic class into another only if the two are compatible and their type arguments are the same.

For example, assuming the following program, this cast is legal:

```java title=Example.java
class Gen<T> {
  T ob;
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
}
public class Main {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    Gen2<Integer> iOb2 = new Gen2<Integer>(99);
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    iOb = (Gen<Integer>) iOb2;
  }
}
```

because iOb2 is an instance of Gen<Integer>. But, this cast:

```java title=Example.java
class Gen<T> {
  T ob;
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
}
public class Main {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    Gen2<Integer> iOb2 = new Gen2<Integer>(99);
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    //iOb = (Gen<Long>) iOb2;//wrong
  }
}
```

is not legal because iOb2 is not an instance of Gen<Long>.

- « Previous
