---
title: Java Object Oriented Design - Java Object Class
nav: Java Object Oriented Desig...
description: All Java classes extend the Object class directly or indirectly.
section: Imported - java2s Archive
order: 50152
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0160__Java_Object_Class.html
---
Java has an Object class in the java.lang package.

All Java classes extend the Object class directly or indirectly.

All Java classes are a subclass of the Object class and the Object class is the superclass of all classes.

The Object class itself does not have a superclass.

A reference variable of the Object class can hold a reference of an object of any class.

The following code declares a reference variable obj of the Object type:

```java title=Example.java
Object obj;
```

## Methods

The Object class has nine methods, which are available to be used in all classes in Java.

- public String toString() It is Implemented in Object class and we can customize it. It returns a string representation of an object. Typically, it is used for debugging purpose.
- public boolean equals(Object obj) It is implemented in Object class and we can customize it. It is used to compare two objects for equality.
- public int hashCode() It is implemented in Object class and we can customize it. It returns a hash code (an integer) value of an object.
- protected Object clone() throws CloneNotSupportedException It is not implemented in Object class and we can customize it by overriding the clone method. It is used to make a copy of an object.
- protected void finalize() throws Throwable It is not implemeneted in Object class and we can customize it. It is called by the garbage collector before an object is destroyed.
- public final Class getClass() It is implemented in Object class and we cannot customize it. It returns a reference to the Class object of the object.
- public final void notify() It is implemeneted in Object class and we cannot customize it. This method notifies one thread in the wait queue of the object.
- public final void notifyAll() It is implemeneted in Object class and we cannot customize it. This method notifies all threads in the wait queue of the object.
- public final void wait() throws InterruptedException public final void wait(long timeout) throws InterruptedException public final void wait (long timeout, int nanos) throws InterruptedException It is implemeneted in Object class and we cannot customize it. Makes a thread wait in the wait queue of the object with or without a timeout.

## Example

The following code shows how to reimplement the toString() method of the Object class.

```java title=Example.java
publicclass Test   {
    public String toString()  {
        return "Here  is a  string";
    }
}
```

## What Is the Class of an Object?

Every object in Java belongs to a class.

The getClass() method of the Object class returns the reference of the Class object.

The following code shows how to get the reference of the Class object for a Cat object:

```java title=Example.java
Cat  c  = new Cat();
Class catClass  = c.getClass();
```

The Class class is generic and its formal type parameter is the name of the class that is represented by its object.

We can rewrite the above statement using generics.

```java title=Example.java
Class<Cat>   catClass = c.getClass();
```

- « Previous
