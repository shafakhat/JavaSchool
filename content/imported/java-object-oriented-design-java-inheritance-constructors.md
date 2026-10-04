---
title: Java Object Oriented Design - Java Inheritance and Constructors
nav: Java Object Oriented Desig...
description: Constructors are not members of a class and they are not inherited by subclasses.
section: Imported - java2s Archive
order: 50167
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0320__Java_Inheritance_Constructors.html
---
```java title=Example.java
```

Constructors are not members of a class and they are not inherited by subclasses.

They are used to initialize instance variables.

```java title=Example.java
class CSuper {public CSuper() {
    System.out.println("Inside CSuper() constructor.");
  }
}
class CSub extends CSuper {
  public CSub() {
    System.out.println("Inside CSub()  constructor.");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    CSub cs = new CSub();
  }
}
```

The code above generates the following result.

## Example

The following shows how does Compiler Injection of a super() Call to Call the Immediate Ancestor's no-args Constructor

```java title=Example.java
class CSuper {public CSuper() {
    super(); // Injected by the compiler
    System.out.println("Inside CSuper() constructor.");
  }
}
class CSub extends CSuper {
  public CSub() {
    super(); // Injected by the compiler
    System.out.println("Inside CSub()  constructor.");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    CSub cs = new CSub();
  }
}
```

The code above generates the following result.

The keyword super refers to the immediate ancestor of a class.

We can call superclass constructors using the super keyword only as the first statement inside a constructor.

## no-args constructor

We can call the no-args constructor or any other constructors of the superclass explicitly as the first statement inside constructors of a class.

The compiler injects the no-args constructor call only if you have not added one explicitly.

```java title=Example.java
class Employee {private String name = "Unknown";
  public Employee(String name) {
    this.name = name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
}
class Manager extends Employee {
  public Manager(String name) {
    super(name);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Manager mgr = new Manager("Tom");
    String name = mgr.getName();
    System.out.println("Manager name:  " + name);
  }
}
```

The code above generates the following result.

Every class must call the constructor of its superclass from its constructors directly or indirectly.

If the superclass does not have a no-args constructor, we must call any other constructors of the superclass explicitly.

- « Previous
