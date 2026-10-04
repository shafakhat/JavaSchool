---
title: Java Object Oriented Design - Java Instance/Static Methods
nav: Java Object Oriented Desig...
description: A class can have two types of methods: instance methods and class methods. Instance methods and class methods are also called non-static methods and static methods, respe
section: Imported - java2s Archive
order: 50143
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0060__Java_Instance_Static_Method.html
---
```java title=Example.java
```

A class can have two types of methods: instance methods and class methods. Instance methods and class methods are also called non-static methods and static methods, respectively.

An instance method is used to implement behavior for the instances of the class. An instance method can only be invoked in the context of an instance of the class.

A class method is used to implement the behavior for the class itself. A class method always executes in the context of a class.

The static modifier is used to define a class method. The absence of the static modifier in a method declaration makes the method an instance method.

## Example

The following are examples of declaring some static and non-static methods:

```java title=Example.java
// A  staticorclass method
static void  aClassMethod()  {
}
// A  non-staticor  instance method
void  anInstanceMethod()  {
}
```

## Note

When a static method of a class is called, an instance of that class may not exist. Therefore, it is not allowed to refer to instance variables from inside a static method.

Class variables exist as soon as the class definition is loaded into memory. The class definition is loaded into memory before the first instance of a class is created.

A class method or static method can refer to only class variables or static variables of the class. An instance method or non-static method can refer to class variables as well as instance variables of the class.

The following code demonstrate the types of class fields that are accessible inside a method.

```java title=Example.java
publicclass Main {
  staticint m = 100; // A static variable
int n = 200; // An instance variable
// Declare a static method
staticvoid printM() {
    /*
     * We can refer to only static variable m in this method because you are
     * inside a static method
     */
    System.out.println("printM() - m   = " + m);
  }
  // Declare an instance method
void printMN() {
    /* We can refer to both static and instance variables m and n in this method */
    System.out.println("printMN() - m   = " + m);
    System.out.println("printMN() - n  = " + n);
  }
}
```

## Invoking a Method

Executing the code in the body of a method is called invoking (or calling) a method.

Instance methods and class methods are invoked differently.

An instance method is invoked on an instance of the class using dot notation.

```java title=Example.java
<instance reference>.<instance method name>(<actual parameters>)
```

We must have a reference to an instance of a class before calling an instance method of that class.

The following code shows how to invoke the printMN() instance method of the Main class:

```java title=Example.java
// Create an  instance of  Main classand
// store its  reference in mt reference variable
Main mt = new Main();
// Invoke  the   printMN() instance  method  using the   mt reference variable
mt.printMN();
```

To invoke a class method, use dot notation with the class name.

The following code invokes the printM() class method of the Main class:

```java title=Example.java
// Invoke  the   printM() class  method
Main.printM();
```

Whatever belongs to a class also belongs to all instances of that class. We can also invoke a class method using a reference of an instance of that class.

```java title=Example.java
Main mt = new Main();
mt.printM(); // Call the   class method  using an  instance mt
```

Using the class name to invoke a class method is more intuitive than using an instance reference.

- « Previous
