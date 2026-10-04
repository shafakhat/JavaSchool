---
title: Java Object Oriented Design - Java Initialization Block
nav: Java Object Oriented Desig...
description: An instance initialization block is used to initialize objects of a class.
section: Imported - java2s Archive
order: 50151
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0120__Java_Initialization_Block.html
---
```java title=Example.java
```

## Instance Initialization Block

An instance initialization block is used to initialize objects of a class.

An instance initializer is simply a block of code inside the body of a class, but outside any methods or constructors.

An instance initializer does not have a name. Its code is simply placed inside an opening brace and a closing brace.

## Example

The following code shows how to declare an instance initializer for the Test class.

Note that an instance initializer is executed in instance context and the keyword this is available inside the instance initializer.

```java title=Example.java
class Test {//fromwww.java2s.comprivateint num;
  // An instance initializer
  {
    this.num = 101;
    /* Other code for the instance initializer*/
  }
  /* Other code for Test class*/
}
```

## Multiple instance initializers

We can have multiple instance initializers for a class. All of them are executed automatically in textual order for every object we create.

Code for all instance initializers are executed before any constructor.

The following code demonstrates the sequence in which the constructor and instance initializers are executed.

```java title=Example.java
publicclass Main {
  {//fromwww.java2s.com
    System.out.println("Inside instance initializer 1.");
  }
  {
    System.out.println("Inside instance initializer 2.");
  }
  public Main() {
    System.out.println("Inside  no-args constructor.");
  }
  publicstaticvoid main(String[] args) {
    Main m = new Main();
  }
}
```

The code above generates the following result.

An instance initializer cannot have a return statement.

## static Initialization Block

A static initialization block is also known as a static initializer. It is similar to an instance initialization block.

It is used to initialize a class. An instance initializer is executed once per object whereas a static initializer is executed only once for a class when the class definition is loaded into JVM.

We need to use the static keyword in the beginning of its declaration.

We can have multiple static initializers in a class. All static initializers are executed in textual order in which they appear, and execute before any instance initializers.

The following code demonstrates when a static initializer is executed.

```java title=Example.java
publicclass Main {
  privatestaticint num;
  {// An instance initializer
    System.out.println("Inside instance initializer.");
  }//www.java2s.com// A static initializer. Note the use of the keyword static below.
static {
    num = 2014;
    System.out.println("Inside static initializer.");
  }
  // Constructor
public Main() {
    System.out.println("Inside constructor.");
  }
  publicstaticvoid main(String[] args) {
    System.out.println("Inside  main() #1.   num: " + num);
    // Declare a reference variable of the class
    Main si;
    System.out.println("Inside  main() #2.   num: " + num);
    new Main();    // Create an object

    System.out.println("Inside  main() #3.   num: " + num);
    new Main();// Create another object
  }
}
```

The code above generates the following result.

static initializer cannot throw checked exceptions and it cannot have a return statement.

- « Previous
