---
title: Java Object Oriented Design - Java Class Instance
nav: Java Object Oriented Desig...
description: The following is the general syntax to create an instance of a class:
section: Imported - java2s Archive
order: 50137
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0010__Java_Class_Instance.html
---
```java title=Example.java
« Previous
```

- Next »

The following is the general syntax to create an instance of a class:

```java title=Example.java
new <Class Constructor>;
```

The new operator is followed by a call to the constructor.

The new operator creates an instance of a class by allocating the memory on heap. The following statement creates an instance of the Dog class:

```java title=Example.java
new Dog();
```

Dog() is a call to the constructor of the Dog class.

When we do not add a constructor to a class, the Java compiler adds one for us.

The constructor added by the Java compiler is called a default constructor. The default constructor accepts no arguments.

The name of the constructor of a class is the same as the class name.

The new operator allocates memory for each instance field of the class. Class static variables are not allocated memory when an instance of the class is created.

To access instance variables of an instance of a class, we must have its reference.

The name of a class defines a new reference type in Java. A variable of a specific reference type can store the reference of an instance of the same reference type.

To declare a reference variable, which will store a reference of an instance of the Dog class.

```java title=Example.java

Dog anInstance;
```

Dog is the class name, which is also a reference type, and anInstance is a variable of that type.

anInstance is a reference variable of Dog type. The anInstance variable can be used to store a reference of an instance of the Dog class.

The new operator allocates the memory for a new instance of a class and returns the reference to that instance.

We need to store the reference returned by the new operator in a reference variable.

```java title=Example.java

anInstance = new Dog();
```

## null Reference Type

We can assign a null value to a variable of any reference type. A null value means that the reference variable is referring to no object.

```java title=Example.java

Dog  obj  = null;  // obj  is not  referring to any  object
obj  = new Dog();  // Now, obj  is referring to a  valid Dog  object
```

You can use a null literal with comparison operators to check for equality and inequality.

```java title=Example.java
if  (obj == null)  {
    //obj is null
}
if  (obj !=  null)  {
    //obj is not null
}
```

Java does not mix reference types and primitive types. We cannot assign null to a primitive type variable.

## Dot Notation to Access Fields of a Class

Dot notation is used to refer to instance variables.

The general form of the dot notation syntax is

```java title=Example.java

<Reference Variable Name>.<Instance Variable Name>
```

obj.name to refer to the name instance variable of the instance to which the obj reference variable is referring.

To assign a value to the name instance variable, use

```java title=Example.java

obj.name = "Rectangle";
```

The following statement assigns the value of the name instance variable to a String variable aName:

```java title=Example.java

String aName = obj.name;
```

To reference class variables, use the name of the class.

```java title=Example.java

ClassName.ClassVariableName
```

For example, we can use Dog.count to refer to the count class variable of the Dog class.

To assign a new value to the count class variable

```java title=Example.java

Dog.count  = 1;
```

To read the value of the count class variable into a variable

```java title=Example.java

long count = Dog.count;
```

The following code shows how to use class fields

```java title=Example.java
class Dog {//www.java2s.comstaticint count = 0;
  String name;
  String gender;
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Dog obj = new Dog();
    // Increase count by one
    Dog.count++;
    obj.name = "Java";
    obj.gender = "Male";
    obj.name = "XML";
    String changedName = obj.name;
  }
}
```

## Default Initialization of Fields

All fields of a class, static as well as non-static, are initialized to a default value.

The default value of a field depends on its data type.

A numeric field (byte, short, char, int, long, float, and double) is initialized to zero. A boolean field is initialized to false. A reference type field is initialized to null.

The following code demonstrates the default initialization of fields.

```java title=Example.java
publicclass Main {
  byte b;//www.java2s.comshort s;
  int i;
  long l;
  float f;
  double d;
  boolean bool;
  String str;
  publicstaticvoid main(String[] args) {
    Main obj = new Main();
    System.out.println("byte is initialized to " + obj.l);
    System.out.println("short is initialized to " + obj.s);
    System.out.println("int is initialized to " + obj.i);
    System.out.println("long is initialized to " + obj.l);
    System.out.println("float is initialized to " + obj.f);
    System.out.println("double is initialized to " + obj.d);
    System.out.println("boolean is initialized to " + obj.bool);
    System.out.println("String is initialized to " + obj.str);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
