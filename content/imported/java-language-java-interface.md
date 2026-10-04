---
title: Java Tutorial - Java Interface
nav: Java Tutorial - Java Inter...
description: interface specifies what a class must do, but not how it does it.
section: Imported - java2s Archive
order: 50446
source: https://www.java2s.com/Tutorials/Java/Java_Language/5080__Java_Interface.html
---
interface specifies what a class must do, but not how it does it.

An interface in Java is like a contract. It defines certain rules through Java methods and the class which implements that interface must follow the rules by implementing the methods.

To implement an interface, a class must create the complete set of methods defined by the interface.

## Syntax

An interface is defined much like a class. This is the general form of an interface:

```java title=Example.java
access interface name {
   return-type method-name1(parameter-list);
   return-type method-name2(parameter-list);
   type final-varname1 = value;
   type final-varname2 = value;
   // ...
   return-type method-nameN(parameter-list);
   type final-varnameN = value;
}
```

Variables can be declared inside of interface declarations. They are implicitly final and static. Variables must also be initialized with a constant value. All methods and variables are implicitly public if the interface, itself, is declared as public.

Here is an example of an interface definition.

```java title=Example.java
interface MyInterface{
   void callback(int param);
}
```

## Implementing Interfaces

To implement an interface, include the implements clause in a class definition, and then create the methods defined by the interface.

The general form of a class that includes the implements clause looks like this:

```java title=Example.java
access-level class classname [extends superclass] [implementsinterface [,interface...]] {
   // class-body
}
```

Here is a small example class that implements the interface shown earlier.

```java title=Example.java
interface MyInterface {
  void callback(int param);
}class Client implements MyInterface{
  // Implement Callback's interface
publicvoid callback(int p) {
    System.out.println("callback called with " + p);
  }
}
```

callback() is declared using the public access specifier. When you implement an interface method, it must be declared as public.

## Java Interface as data type

Once we define an interface we can use it as a type for object instance we create through its implementation class.

The following example calls the callback( ) method via an interface reference variable:

```java title=Example.java
interface MyInterface {
  void callback(int param);
}class Client implements MyInterface{
  // Implement Callback's interface
publicvoid callback(int p) {
    System.out.println("callback called with " + p);
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    MyInterface c = new Client();
    c.callback(42);
  }
}
```

The output of this program is shown here:

## Polymorphism and interface

interface is designed for polymorphism. interface defines a list of methods acting as the contract between the interface and its implementation. One interface can be implements by more than once and each different implementation of the same interface would follow the same list of methods. Therefore if we know several classes implement the same interface we can use that interface to reference all of its implementer classes. The compiler will determine dynamically which implementation to use.

```java title=Example.java
interface MyInterface {
  void callback(int param);
}class Client implements MyInterface{
  // Implement Callback's interface
publicvoid callback(int p) {
    System.out.println("Client");
    System.out.println("p squared is " + (p * 2));
  }
}
class AnotherClient implements MyInterface{
  // Implement Callback's interface
publicvoid callback(int p) {
    System.out.println("Another version of callback");
    System.out.println("p squared is " + (p * p));
  }
}
class TestIface2 {
  publicstaticvoid main(String args[]) {
    MyInterface c = new Client();
    AnotherClient ob = new AnotherClient();
    c.callback(42);
    c = ob; // c now refers to AnotherClient object
    c.callback(42);
  }
}
```

The output from this program is shown here:

## Java interface as build block

If a class implements an interface but does not fully implement its methods, then that class must be declared as abstract. For example:

```java title=Example.java
interface MyInterface {
  void callback(int param);
void show();
}
abstractclass Incomplete implements MyInterface {
  int a, b;
  publicvoid show() {
    System.out.println(a + " " + b);
  }
}
```

## Variables in Interfaces

We can use interface to organize constants.

```java title=Example.java
interface MyConstants {
  int NO = 0;int YES = 1;
}
class Question implements MyConstants {
  int ask() {
      return YES;
  }
}
publicclass Main implements MyConstants {
  staticvoid answer(int result) {
    switch (result) {
      case NO:
        System.out.println("No");
        break;
      case YES:
        System.out.println("Yes");
        break;
    }
  }
  publicstaticvoid main(String args[]) {
    Question q = new Question();
    answer(q.ask());
  }
}
```

The output:

## Extend Interface

One interface can inherit another interface with the keyword extends.

```java title=Example.java
interface IntefaceA {
  void meth1();void meth2();
}
interface IntefaceB extends IntefaceA {
  void meth3();
}
class MyClass implements IntefaceB {
  publicvoid meth1() {
    System.out.println("Implement meth1().");
  }
  publicvoid meth2() {
    System.out.println("Implement meth2().");
  }
  publicvoid meth3() {
    System.out.println("Implement meth3().");
  }
}
publicclass Main {
  publicstaticvoid main(String arg[]) {
    MyClass ob = new MyClass();
    ob.meth1();
    ob.meth2();
    ob.meth3();
  }
}
```

The output:

- « Previous
