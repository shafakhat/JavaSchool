---
title: Java Reflection Object Create
nav: Java Reflection Object Cre...
description: We can use reflection to create objects of a class dynamically. by invoking one of the constructors.
section: Imported - java2s Archive
order: 50407
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0070__Java_Create_Objects.html
---
```java title=Example.java
```

We can use reflection to create objects of a class dynamically. by invoking one of the constructors.

And then we can access the values of fields of objects, set their values, and invoke their methods.

There are two ways to create objects:

- Using the no-args constructor
- Using the constructor with arguments

## no-args constructor

If you have the reference of a Class object, you can create an object of the class using the newInstance() method on the Class class.

This method takes no parameter and is equivalent to using the new operator on the no-args constructor of the class.

```java title=Example.java

MyClass m  = myObject.newInstance();
```

```java title=Example.java
class MyClass {/*www.java2s.com*/public MyClass() {
     System.out.println("called");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) throws InstantiationException {
    Class<MyClass> personClass = MyClass.class;
    try {
      MyClass p = personClass.newInstance();
      System.out.println(p);
    } catch (InstantiationException | IllegalAccessException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

## Constructor with argument

You can create an object using reflection by invoking a particular constructor. It involves two steps.

- Get an instance of the constructor
- Call newInstance to invoke it

You can get the reference of this constructor as shown:

```java title=Example.java

Constructor<MyClass> cons  = myClass.getConstructor(int.class, String.class);
```

Then call the newInstance() method with the arguments to create an object.

```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
//fromwww.java2s.comclass MyClass {
  public MyClass(int i, String s) {
    System.out.println("called");
    System.out.println(i);
    System.out.println(s);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> myClass = MyClass.class;
    try {
      Constructor<MyClass> cons = myClass.getConstructor(int.class,
          String.class);
      MyClass chris = cons.newInstance(1, "abc");
      System.out.println(chris);
    } catch (NoSuchMethodException | SecurityException | InstantiationException
        | IllegalAccessException | IllegalArgumentException
        | InvocationTargetException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

## Invoking Methods

We can invoke methods using reflection through the method reference.

To invoke a method, call the invoke() method on the method's reference.

Its first parameter is the object where it is from and the second parameter is a varargs for all the arguments in the same order as the method's declaration.

In case of a static method, we just need specify null for the first argument.

```java title=Example.java
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
//www.java2s.comclass MyClass {
  public MyClass() {
  }
  publicvoid setName(String n) {
    System.out.println(n);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> myClass = MyClass.class;
    try {
      MyClass p = myClass.newInstance();
      Method setName = myClass.getMethod("setName", String.class);
      setName.invoke(p, "abc");
    } catch (InstantiationException | IllegalAccessException
        | NoSuchMethodException | SecurityException | IllegalArgumentException
        | InvocationTargetException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

- « Previous
