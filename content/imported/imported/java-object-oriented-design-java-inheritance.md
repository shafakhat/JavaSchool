---
title: Java Object Oriented Design - Java Inheritance
nav: Java Object Oriented Desig...
description: A subclass can inherit from the superclass. A superclass is also known as a base class or a parent class. A subclass is also known as a derived class or a child class.
section: Imported - java2s Archive
order: 50165
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0300__Java_Inheritance.html
---
```java title=Example.java
« Previous
```

- Next »

A subclass can inherit from the superclass. A superclass is also known as a base class or a parent class. A subclass is also known as a derived class or a child class.

It is very simple to inherit a class from another class. We use the keyword extends followed by the superclass name in the class declaration of your subclass.

Java does not support multiple inheritance of implementation.

A class in Java cannot have more than one superclass.

## Syntax

The general syntax is

```java title=Example.java

<class modifiers>class <SubclassName> extends <SuperclassName> {
    // Code for the   Subclass
}
```

## Example

The following code shows how to use create a Manager class from Employee class.

```java title=Example.java
class Employee {/*www.java2s.com*/private String name = "Unknown";
  publicvoid setName(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
}
class Manager extends Employee {
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create an object of the Manager class
    Manager mgr = new Manager();
    // Set the name of the manager
    mgr.setName("Tom");
    // Get the name of the manager
    String mgrName = mgr.getName();
    // Display the manager name
    System.out.println("Manager Name: " + mgrName);
  }
}
```

The code above generates the following result.

## Note

We did not write any code for the Manager class, it works the same as the Employee class, because it inherits from the Employee class.

You create a manager object by using the Manager class's constructor.

```java title=Example.java

Manager mgr = new Manager();
```

After the manager object is created, Manager object works the same way with Employee object.

We used the setName() and getName() methods with the manager object.

```java title=Example.java

mgr.setName("Tom");
String mgrName  = mgr.getName();
```

The Manager class does not declare the setName() and getName() methods. Manager class "extends Employee".

When a class inherits from another class, it inherits its superclass members, instance variables, methods, etc.

## Object Parent class

Object Class is the Default Superclass

If a class does not specify a superclass using the keyword extends in its class declaration, it inherits from the java.lang.Object class.

```java title=Example.java
publicclass P {
}
```

class P is extending from Object, even though we didn't specify the parent class.

All classes were implicitly inherited from the Object class. Therefore objects of all classes can use the methods of the Object class.

```java title=Example.java

Employee emp = new Employee();
int hc  = emp.hashCode();
String str = emp.toString();
```

Employee class does not specify its superclass using an extends clause. This means that it inherits from the Object class.

The Object class declares the hashCode() and toString() methods. Because Employee class is a subclass of the Object class, it can use these methods.

## Upcasting and Downcasting

An "is-a" relationship in the real world translates into inheritance class hierarchy in software.

For example, a Manager is a specific type of Employee. An Employee is a specific type of Object.

As you move up in the inheritance hierarchy, you move from a specific type to a more general type.

An assignment from subclass to superclass is called upcasting and it is always allowed in Java.

```java title=Example.java
class Employee {//fromwww.java2s.comprivate String name = "Unknown";
  publicvoid setName(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
}
class Manager extends Employee {
}
publicclass Main {
  publicstaticvoid printName(Employee emp) {
    String name = emp.getName();
    System.out.println(name);
  }
  publicstaticvoid main(String[] args) {
    Employee emp = new Employee();
    emp.setName("Tom");
    Manager mgr = new Manager();
    mgr.setName("Jack"); // Inheritance of setName() at work
// Print names
    printName(emp);
    printName(mgr); // Upcasting at work
  }
}
```

Assigning a superclass reference to a subclass variable is called downcasting.

Downcasting is the opposite of upcasting.

In upcasting, the assignment moves up the class hierarchy whereas in downcasting the assignment moves down the class hierarchy.

We have to use a typecast in downcasting.

```java title=Example.java

Manager mgr = (Manager)emp;  // OK. Downcast  at work
```

The code above generates the following result.

## instanceof Operator

Java instanceof operator helps us determine whether a reference variable has a reference to a class or a subclass.

It takes two operands and evaluates to a boolean value true or false.

Its syntax is

```java title=Example.java

<Class Reference Variable> instanceof <Class Name or Interface>
```

If <Class Reference Variable> refers to an object of class <Class Name> or any of its descendants, instanceof returns true.

Otherwise, it returns false.

If reference variable is null, instanceof always returns false.

We should use the instanceof operator before downcasting.

```java title=Example.java

Manager mgr = new Manager();
Employee emp = mgr;
if (emp instanceof Manager)  {
    // downcast  will succeed
    mgr = (Manager)emp;
}else  {
    // emp is not  a  Manager type
}
```

## Disabling Inheritance

We can disable subclassing by declaring the class final.

A final class cannot be subclassed.

The following code declares a final class named MyClass:

```java title=Example.java
publicfinalclass  MyClass{
}
```

We can also declare a method as final. A final method cannot be overridden or hidden by a subclass.

```java title=Example.java
publicclass A  {
    publicfinal  void  m1()  {
    }
    public void  m2()  {
    }
}
```

- Next »
- « Previous
