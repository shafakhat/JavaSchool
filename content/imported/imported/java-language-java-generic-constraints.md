---
title: Java Tutorial - What is Java Generic Bounded Types and how to use Generic Bounded Types
nav: Java Tutorial - What is Ja...
description: When specifying a type parameter, you can create an upper bound from which all type arguments must be derived.
section: Imported - java2s Archive
order: 50461
source: https://www.java2s.com/Tutorials/Java/Java_Language/8040__Java_Generic_Constraints.html
---
```java title=Example.java
« Previous
```

- Next »

When specifying a type parameter, you can create an upper bound from which all type arguments must be derived.

## Syntax

This is accomplished through the use of an extends clause when specifying the type parameter:

```java title=Example.java

<T extends superClassName>
```

This specifies that T can only be replaced by superClassName, or subclasses of superClassName. Thus, superclass defines an inclusive, upper limit.

## Example

```java title=Example.java
class Calculator<T extends Number> {
  T[] nums;/*fromwww.java2s.com*/
  Calculator(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++){
      sum += nums[i].doubleValue();
    }
    return sum / nums.length;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Integer inums[] = { 1, 2, 3, 4, 5 };
    Calculator<Integer> iob = new Calculator<Integer>(inums);
    double v = iob.average();
    System.out.println("iob average is " + v);
    Double dnums[] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
    Calculator<Double> dob = new Calculator<Double>(dnums);
    double w = dob.average();
    System.out.println("dob average is " + w);
  }
}
```

In addition to using a class type as a bound, you can also use an interface type. You can specify multiple interfaces as bounds.

A bound can include both a class type and one or more interfaces. In this case, the class type must be specified first.

When a bound includes an interface type, only type arguments that implement that interface are legal.

When specifying a bound that has a class and an interface, or multiple interfaces, use the & operator to connect them.

For example,

```java title=Example.java
class Gen<T extends MyClass & MyInterface> {}
```

Any type argument passed to T must be a subclass of MyClass and implement MyInterface.

The code above generates the following result.

## Java Generic Parameter Wildcard

To create a generic method, you use the wildcard argument. The wildcard argument is specified by the ?, and it represents an unknown type.

Wildcard arguments can be bounded in the same way that a type parameter can be bounded. A bounded wildcard is important when creating a generic type that will operate on a class hierarchy.

A bounded wildcard specifies either an upper bound or a lower bound for the type argument.

In general, to establish an upper bound for a wildcard, use the following type of wildcard expression:

```java title=Example.java

<? extends superclass>
```

superclass is the name of the class that serves as the upper bound. This is an inclusive clause.

You can specify a lower bound for a wildcard by adding a super clause to a wildcard declaration.

```java title=Example.java

<? super subclass>
```

In this case, only classes that are superclasses of subclass are acceptable arguments. This is an exclusive clause, because it will not match the class specified by subclass.

## Example 2

An upper bound for a wildcard.

```java title=Example.java
class Calculator<T extends Number> {
  T[] nums;/*fromwww.java2s.com*/
  Calculator(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++){
      sum += nums[i].doubleValue();
    }
    return sum / nums.length;
  }
}
publicclass Main {
  boolean sameAvg(Calculator<?> ob) {
    if (1.2 == ob.average())
      return true;
    return false;
  }
  publicstaticvoid main(String args[]) {
  }
}
```

## Example 3

Calculator<?> matches any Stats object, allowing any two Stats objects to have their averages compared.

The following program demonstrates this:

```java title=Example.java
class Calculator<T extends Number> {
  T[] nums;//www.java2s.com
  Calculator(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++)
      sum += nums[i].doubleValue();
    return sum / nums.length;
  }
  boolean sameAvg(Calculator<?> ob) {
    if (average() == ob.average())
      return true;
    return false;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Integer inums[] = { 1, 2, 3, 4, 5 };
    Calculator<Integer> iob = new Calculator<Integer>(inums);
    Double dnums[] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
    Calculator<Double> dob = new Calculator<Double>(dnums);
    if (iob.sameAvg(dob))
      System.out.println("are the same.");
    else
      System.out.println("differ.");
  }
}
```

The code above generates the following result.

## Example 4

```java title=Example.java
class TwoD {//fromwww.java2s.comint x, y;
  TwoD(int a, int b) {
    x = a;
    y = b;
  }
}
// Three-dimensional coordinates.
class ThreeD extends TwoD {
  int z;
  ThreeD(int a, int b, int c) {
    super(a, b);
    z = c;
  }
}
class Map<T extends TwoD> {
  T[] coords;
  Map(T[] o) {
    coords = o;
  }
}
publicclass Main {
  staticvoid showXY(Map<?> c) {
    for (int i = 0; i < c.coords.length; i++){
      System.out.println(c.coords[i].x + " " + c.coords[i].y);
    }
  }
  staticvoid showXYZ(Map<? extends ThreeD> c) {
    for (int i = 0; i < c.coords.length; i++){
      System.out.println(c.coords[i].x + " " + c.coords[i].y + " "
          + c.coords[i].z);
    }
  }
  publicstaticvoid main(String args[]) {
    TwoD td[] = { new TwoD(0, 0), new TwoD(-1, -2) };
    Map<TwoD> map = new Map<TwoD>(td);
    System.out.println("Contents of tdlocs.");
    showXY(map);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
