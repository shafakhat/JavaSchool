---
title: Java Object Oriented Design - Java Object Finalize
nav: Java Object Oriented Desig...
description: Java provides a way to perform resource release, when an object is about to be destroyed.
section: Imported - java2s Archive
order: 50157
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0210__Java_Object_Finalize.html
---
```java title=Example.java
```

Java provides a way to perform resource release, when an object is about to be destroyed.

In Java, we create objects, but we cannot destroy objects.

The JVM runs a low priority special task called garbage collector to destroy all objects that are no longer referenced.

The garbage collector gives us a chance to execute the cleanup code before an object is destroyed.

The Object class has a finalize() method, which is declared as follows:

```java title=Example.java
protected void  finalize() throws   Throwable  {  }
```

The finalize() method in the Object class does not do anything.

You need to override the method in your class.

The finalize() method of your class will be called by the garbage collector before an object of your class is destroyed.

## Example

The following code shows how to create a Finalize Class that Overrides the finalize() Method of the Object Class.

```java title=Example.java
class Finalize {//www.java2s.comprivateint x;
  public Finalize(int x) {
    this.x = x;
  }
  publicvoid finalize() {
    System.out.println("Finalizing " + this.x);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    for (int i = 0; i < 20000; i++) {
      new Finalize(i);
    }
  }
}
```

The code above generates the following result.

- « Previous
