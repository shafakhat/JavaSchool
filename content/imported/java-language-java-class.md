---
title: Java Tutorial - Java Class
nav: Java Tutorial - Java Class
description: A class is a template for an object, and an object is an instance of a class.
section: Imported - java2s Archive
order: 50439
source: https://www.java2s.com/Tutorials/Java/Java_Language/5010__Java_Class.html
---
```java title=Example.java
```

A class defines a new data type.

This new type can be used to create objects of that type.

A class is a template for an object, and an object is an instance of a class.

## Syntax

The general form of a class definition is shown here:

```java title=Example.java
class classname {
  type instance-variable1;
  type instance-variable2;
  // ...
  type instance-variableN;
  type methodname1(parameter-list) {
    // body of method
  }
  type methodname2(parameter-list) {
    // body of method
  }
  // ...
  type methodnameN(parameter-list) {
   // body of method
  }
}
```

A class is declared by using the class keyword.

The methods and variables defined within a class are called class members.

Variables defined within a class are called instance variables because each instance of the class contains its own copy of these variables.

The data for one object is separate and unique from the data for another.

## Example

Here is a class called Box that defines three member variables: width, height, and depth.

```java title=Example.java
class Box {
    int width;
    int height;
    int depth;
}
```

## Java Object

When you create a class, you are creating a new data type. You can use this type to declare objects of that type.

Creating objects of a class is a two-step process.

- Declare a variable of the class type.
- Use the new operator to dynamically allocates memory for an object.

The following line is used to declare an object of type Box:

```java title=Example.java
Box mybox = new Box();
```

This statement combines the two steps. It can be rewritten like this to show each step more clearly:

```java title=Example.java
Box mybox; // declare reference to object
mybox = new Box(); // allocate a Box object
```

The first line declares mybox as a reference to an object of type Box. After this line executes, mybox contains the value null. null indicates that mybox does not yet point to an actual object.

Any attempt to use mybox at this point will result in an error.

The next line allocates an actual object and assigns a reference to mybox. After the second line executes, you can use mybox as a Box object.

mybox holds the memory address of the actual Box object.

A class defines a new type of data. In this case, the new type is called Box. To create a Box object, you will use a statement like the following:

```java title=Example.java
class Box {int width;
  int height;
  int depth;
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Box myBox = new Box();
    myBox.width = 10;
    System.out.println("myBox.width:"+myBox.width);
  }
}
```

The output:

myBox is an instance of Box. mybox contains its own copy of each instance variable, width, height, and depth, defined by the class. To access these variables, you will use the dot (.) operator.

```java title=Example.java
mybox.width = 10;
```

This statement assigns the width from mybox object to 10. Here is a complete program that uses the Box class:

Any attempt to use a null mybox will result in a compile-time error.

```java title=Example.java
class Box {
  int width;
  int height;
  int depth;
}
publicclass Main {
  publicstatic void main(String args[]) {
    Box myBox;
    myBox.width = 10;
  }
}
```

If you try to compile the code above, you will get the following error message from the Java compiler.

## Java instanceof operator

Java provides the run-time operator instanceof to check class type for an object.

The instanceof operator has this general form:

```java title=Example.java
object instanceof type
```

The following program demonstrates instanceof:

```java title=Example.java
class A {
}
class B {
}
class C extends A {
}
class D extends A {
}
publicclass Main{
  publicstaticvoid main(String args[]) {
    A a = new A();
    B b = new B();
    C c = new C();
    D d = new D();
    if (a instanceof A)
      System.out.println("a is instance of A");
    if (b instanceof B)
      System.out.println("b is instance of B");
    if (c instanceof C)
      System.out.println("c is instance of C");
    if (c instanceof A)
      System.out.println("c can be cast to A");
    if (a instanceof C)
      System.out.println("a can be cast to C");
    A ob;
    ob = d; // A reference to d
    System.out.println("ob now refers to d");
    if (ob instanceof D)
      System.out.println("ob is instance of D");
    ob = c; // A reference to c
    System.out.println("ob now refers to c");
    if (ob instanceof D)
      System.out.println("ob can be cast to D");
    else
      System.out.println("ob cannot be cast to D");
    if (ob instanceof A)
      System.out.println("ob can be cast to A");
    // all objects can be cast to Object
if (a instanceof Object)
      System.out.println("a may be cast to Object");
    if (b instanceof Object)
      System.out.println("b may be cast to Object");
    if (c instanceof Object)
      System.out.println("c may be cast to Object");
    if (d instanceof Object)
      System.out.println("d may be cast to Object");
  }
}
```

The output from this program is shown here:

- « Previous
