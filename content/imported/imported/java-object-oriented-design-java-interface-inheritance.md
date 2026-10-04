---
title: Java Object Oriented Design - Java Interface Inheritance
nav: Java Object Oriented Desig...
description: An interface can inherit from another interface. Unlike a class, an interface can inherit from multiple interfaces.
section: Imported - java2s Archive
order: 50184
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0550__Java_Interface_Inheritance.html
---
```java title=Example.java
« Previous
```

- Next »

An interface can inherit from another interface. Unlike a class, an interface can inherit from multiple interfaces.

```java title=Example.java
interface Singer {
  void sing();
  void setRate(double rate);
  double getRate();
}
interface Writer {
  void write();
  void setRate(double rate);
  double getRate();
}
interface Player {
  void play();
  void setRate(double rate);
  default double getRate() {
    return 300.0;
  }
}
```

An interface uses the keyword extends to inherit from other interfaces. The keyword extends is followed by a comma-separated list of inherited interface names.

The inherited interfaces are known as superinterfaces and the interface inheriting them is known as subinterface.

An interface inherits the following members of its superinterfaces:

- Abstract and default methods
- Constant fields
- Nested types

An interface does not inherit static methods from its superinterfaces.

An interface may override the inherited abstract and default methods that it inherits from its superinterfaces.

If the super interface and child interface have the fields and nested types with the same names, the child interface wins.

```java title=Example.java
interface A {//fromwww.java2s.com
  String s = "A";
}
interface B extends A {
  String s = "B";
}
publicclass Main {
  publicstaticvoid main(String[] argv){
    System.out.println(B.s);
  }
}
```

The following code shows how to override the default method.

```java title=Example.java
interface A {
  default String getValue(){
    return "A";
  }
}
interface B extends A {
  default String getValue(){
    return "B";
  }
}
class MyClass implements B{
}
publicclass Main {
  publicstatic void main(String[] argv){
    System.out.println(new MyClass().getValue());
  }
}
```

The code above generates the following result.

## Inheriting Conflicting Implementations

Introduction of default methods made it possible for a class to inherit conflicting implementations from its superclass and superinterfaces.

Java uses the three simple rules in order to resolve the conflict.

- superclass always wins
- most specific superinterface wins
- class must override the conflicting method

## instanceof Operator

We can use the instanceof operator to evaluate if a reference type variable refers to an object of a specific class or its class implements a specific interface.

The general syntax of the instanceof operator is

```java title=Example.java

referenceVariable instanceof  ReferenceType
```

```java title=Example.java
interface A {//www.java2s.comdefault String getValue(){
    return"A";
  }
}
interface B {
  default String getValue(){
    return"B";
  }
}
class MyClass implements B,A{
  public String getValue(){
    return"B";
  }
}
publicclass Main {
  publicstaticvoid main(String[] argv){
    MyClass myClass = new MyClass();
    System.out.println(myClass instanceof MyClass);
    System.out.println(myClass instanceof A);
    System.out.println(myClass instanceof B);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
