---
title: Java Tutorial - Java Exception Statements
nav: Java Tutorial - Java Excep...
description: To guard against and handle a run-time error, enclose the code to monitor inside a try block.
section: Imported - java2s Archive
order: 50452
source: https://www.java2s.com/Tutorials/Java/Java_Language/6010__Java_Exception_Statements.html
---
To guard against and handle a run-time error, enclose the code to monitor inside a try block.

Immediately following the try block, include a catch clause that specifies the exception type that you wish to catch.

## Java try catch statement

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    try { // monitor a block of code.
int d = 0;
      int a = 42 / d;
      System.out.println("This will not be printed.");
    } catch (ArithmeticException e) { // catch divide-by-zero error
      System.out.println("Division by zero.");
    }
    System.out.println("After catch statement.");
  }
}
```

The code above generates the following result.

## Multiple catch Clauses

You can specify two or more catch clauses, each catching a different type of exception.

When an exception is thrown, each catch statement is inspected in order, and the first one whose type matches that of the exception is executed.

After one catch statement executes, the others are bypassed, and execution continues after the try/catch block.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    try {int a = args.length;
      System.out.println("a = " + a);
      int b = 42 / a;
      int c[] = { 1 };
      c[42] = 99;
    } catch (ArithmeticException e) {
      System.out.println("Divide by 0: " + e);
    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Array index oob: " + e);
    }
    System.out.println("After try/catch blocks.");
  }
}
```

When you use multiple catch statements, exception subclasses must come before any of their superclasses.

The code above generates the following result.

## Nested try Statements

The try statement can be nested.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    try {int a = args.length;
      int b = 42 / a;
      System.out.println("a = " + a);
      try { // nested try block
if (a == 1)
          a = a / (a - a); // division by zero exception
if (a == 2) {
          int c[] = { 1 };
          c[4] = 9; // an out-of-bounds exception
        }
      } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Array index out-of-bounds: " + e);
      }
    } catch (ArithmeticException e) {
      System.out.println("Divide by 0: " + e);
    }
  }
}
```

The code above generates the following result.

## Java throw statement

We can throw an exception in case of an exception.

## Syntax

The general form of throw is shown here:

```java title=Example.java
throw ThrowableInstance;
```

Here, ThrowableInstance must be an object of type Throwable or a subclass of Throwable.

There are two ways to obtain a Throwable object: using a parameter in a catch clause, or creating one with the new operator.

The flow of execution stops immediately after the throw statement; any subsequent statements are not executed.

How to use Java throws statement?

```java title=Example.java
publicclass Main {
  staticvoid aMethod() {
    try {thrownew NullPointerException("demo");
    } catch (NullPointerException e) {
      System.out.println("Caught inside demoproc.");
      throw e; // rethrow the exception
    }
  }
  publicstaticvoid main(String args[]) {
    try {
      aMethod();
    } catch (NullPointerException e) {
      System.out.println("Recaught: " + e);
    }
  }
}
```

The code above generates the following result.

## Java throws statement

If a method wants to throw an exception, it must specify this behavior.

This is the general form of a method declaration that includes a throws clause:

```java title=Example.java
type method-name(parameter-list) throws exception-list
{
// body of method
}
```

exception-list is a comma-separated list of the exceptions that a method can throw.

```java title=Example.java
publicclass Main {
  staticvoid throwOne() throws IllegalAccessException {
    System.out.println("Inside throwOne.");
    thrownew IllegalAccessException("demo");
  }publicstaticvoid main(String args[]) {
    try {
      throwOne();
    } catch (IllegalAccessException e) {
      System.out.println("Caught " + e);
    }
  }
}
```

The code above generates the following result.

## Java finally statement

Any code that would be executed regardless after a try block is put in a finally block.

This is the general form of an exception-handling block:

```java title=Example.java
try {
// block of code to monitor for errors
}
catch (ExceptionType1 exOb) {
// exception handler for ExceptionType1
}
catch (ExceptionType2 exOb) {
// exception handler for ExceptionType2
}
// ...
finally {
// block of code to be executed after try block ends
}
```

finally creates a block of code that will be executed after a try/catch block has completed.

The finally block will execute even if no catch statement matches the exception.

finally block can be useful for closing file handles and freeing up any other resources. The finally clause is optional.

```java title=Example.java
publicclass Main {
  // Through an exception out of the method.
staticvoid methodC() {
    try {
      System.out.println("inside methodC");
      thrownew RuntimeException("demo");
    } finally {
      System.out.println("methodC finally");
    }
  }
  // Return from within a try block.
staticvoid methodB() {
    try {
      System.out.println("inside methodB");
      return;
    } finally {
      System.out.println("methodB finally");
    }
  }
  // Execute a try block normally.
staticvoid methodA() {
    try {
      System.out.println("inside methodA");
    } finally {
      System.out.println("methodA finally");
    }
  }
  publicstaticvoid main(String args[]) {
    try {
      methodC();
    } catch (Exception e) {
      System.out.println("Exception caught");
    }
    methodB();
    methodA();
  }
}
```

The code above generates the following result.

- « Previous
