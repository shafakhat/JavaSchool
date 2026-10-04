---
title: Java Reflection - java.lang.Class Class
nav: Java Reflection - java.lan...
description: The java.lang.Class class is the center of reflection in Java.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Reflection/0020__Java_java.lang.Class.html
---
The java.lang.Class class is the center of reflection in Java.

An object of the Class class represents a class in a program at runtime.

The Class class is a generic class.

It takes a type parameter, which is the type of the class represented by the Class object.

For example, Class<Boolean> represents the class object for the Boolean class.

Class<?> represents a class type whose class is unknown.

We can use Class class to find information about a class at runtime.

We can get the reference to the Class object of a class in the followings ways:

- Using class literal
- Using the getClass() method of the Object class
- Using the forName() method of the Class class

## Class Literal

A class literal is the class name followed by a dot and the word "class."

For example, if you have a class Test, its class literal is Test.class and you can write

```java title=Example.java
Class<Test> testClass = Test.class;
```

You can also get the class object for primitive data types and the keyword void using class literals as boolean.class, byte.class, char.class, short.class, int.class, long.class, float.class, double.class, and void.class.

Each wrapper primitive data type class has a static field named TYPE, which has the reference to the class object of the primitive data type it represents.

int.class and Integer.TYPE refer to the same class object.

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Class c = boolean.class;
    c = Boolean.TYPE;
    c = byte.class;
    c = Byte.TYPE;
    c = char.class;
    c = Character.TYPE;
    c = short.class;
    c = Short.TYPE ;
    c = int.class;
    c = Integer.TYPE;
    c = long.class;
    c = Long.TYPE;
    c = float.class;
    c = Float.TYPE;
    c = double.class;
    c = Double.TYPE;
    c = void.class;
    c = Void.TYPE;
  }
}
```

## getClass() method

The Object class has a getClass() method, which returns the reference to the Class object of the class of the object.

The following code shows how to get the reference to the Class object of the Test class:

```java title=Example.java
class Test{
}
public class Main {
  public static void main(String[] args) {
    Test   testRef = new Test();
    Class testClass = testRef.getClass();
  }
}
```

## forName() method

The Class class forName() static method returns a reference to a Class object.

Its overloaded methods are

```java title=Example.java
Class<?>   forName(String  className)
Class<?>   forName(String name,  boolean initialize, ClassLoader loader)
```

The first version of the forName() method takes the fully qualified name of the class as parameter and loads the class, and returns its object reference.

If the class is already loaded, it returns the reference to the Class object.

The second version method can control if to initialize or not to initialize the class when it is loaded. We can also passin class loader.

To load a class named com.java2s..Test:

```java title=Example.java
Class testClass  = Class.forName("com.java2s..Test");
```

The following code shows how to load a class and gets the reference to its Class object.

```java title=Example.java
class MyClass {static {
    System.out.println("Loading class MyClass...");
  }
}
public class Main {
  public static void main(String[] args) {
    try {
      String className = "MyClass";
      boolean initialize = false;
      ClassLoader cLoader = Main.class.getClassLoader();
      Class c = Class.forName(className, initialize, cLoader);
      className = "MyClass";
      System.out.println("about to load");
      // Will load and initialize the class
      c = Class.forName(className);
    } catch (ClassNotFoundException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

- « Previous
