---
title: Java Object Oriented Design - Java Exception Usage
nav: Java Object Oriented Desig...
description: The following code shows how to get to the stack frames of a thread.
section: Imported - java2s Archive
order: 50178
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0430__Java_Exception_Usage.html
---
```java title=Example.java
« Previous
```

- Next »

## Accessing the Stack of a Thread

The following code shows how to get to the stack frames of a thread.

A Throwable object captures the stack of the thread at the point it is created.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    m1();//fromwww.java2s.com
  }
  publicstaticvoid m1() {
    m2();
  }
  publicstaticvoid m2() {
    m3();
  }
  publicstaticvoid m3() {
    Throwable t = new Throwable();
    StackTraceElement[] frames = t.getStackTrace();
    printStackDetails(frames);
  }
  publicstaticvoid printStackDetails(StackTraceElement[] frames) {
    System.out.println("Frame count: " + frames.length);
    for (int i = 0; i < frames.length; i++) {
      int frameIndex = i; // i = 0 means top frame
      System.out.println("Frame Index: " + frameIndex);
      System.out.println("File Name: " + frames[i].getFileName());
      System.out.println("Class Name: " + frames[i].getClassName());
      System.out.println("Method Name: " + frames[i].getMethodName());
      System.out.println("Line Number: " + frames[i].getLineNumber());
    }
  }
}
```

The code above generates the following result.

## try-with-resources Block

Java 7 added a new construct called try-with-resources.

With the new try-with-resources construct in Java 7, the above code can be written as

```java title=Example.java
try (AnyResource aRes = create the resource...) {
    // Work with the resource here.
    // The resource will be  closed automatically.
}
```

The try-with-resources construct automatically closes the resources when the program exits the construct.

A try-with-resource construct may have one or more catch blocks and/or a finally block.

We can specify multiple resources in a try-with-resources block. Two resources must be separated by a semicolon.

The last resource must not be followed by a semicolon.

The following code shows some usage of try-with-resources to use one and multiple resources:

```java title=Example.java
try (AnyResource  aRes1  = getResource1())  {
    // Use aRes1  here
}
try (AnyResource  aRes1  = getResource1(); AnyResource  aRes2  = getResource2())  {
    // Use aRes1  and  aRes2  here
}
```

The resources that we specify in a try-with-resources are implicitly final.

A resource that in a try-with-resources must be of the type java.lang.AutoCloseable.

Java 7 added the AutoCloseable interface, which has a close() method.

When the program exits the try-with-resources block, the close() method of all the resources is called automatically.

In the case of multiple resources, the close() method is called in the reverse order in which the resources are specified.

```java title=Example.java
class MyResource implements AutoCloseable {
/*fromwww.java2s.com*/public MyResource() {
    System.out.println("Creating MyResource.");
  }
  @Override
  publicvoid close() {
    System.out.println("Closing  MyResource...");
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    try (MyResource mr = new MyResource();
        MyResource mr2 = new MyResource()) {
    }
  }
}
```

The code above generates the following result.

## Multi-Catch Block

Java 7 added support for a multi-catch block to handle multiple types of exceptions in a catch block.

We can specify multiple exceptions types in a multi-catch block. Multiple exceptions are separated by a vertical bar (|).

To catch three exceptions: Exception1, Exception2, and Exception3.

```java title=Example.java
try  {
    // May  throw  Exception1, Exception2, or  Exception3
}
catch (Exception1 | Exception2 | Exception3  e)  {
    // Handle  Exception1, Exception2, and  Exception3
}
```

In a multi-catch block, it is not allowed to have alternative exceptions that are related by subclassing.

For example, the following multi-catch block is not allowed, because Exception1 and Exception2 are subclasses of Throwable:

```java title=Example.java
try  {
    // May  throw  Exception1, Exception2, or  Exception3
}
catch (Exception1 | Exception2 | Throwable    e)  {
    // Handle  Exceptions here
}
```

- Next »
- « Previous
