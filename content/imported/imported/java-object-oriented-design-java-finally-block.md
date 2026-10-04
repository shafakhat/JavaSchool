---
title: Java Object Oriented Design - Java finally block
nav: Java Object Oriented Desig...
description: A try block can also have zero or one finally block. A finally block is always used with a try block.
section: Imported - java2s Archive
order: 50177
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0420__Java_finally_block.html
---
```java title=Example.java
```

A try block can also have zero or one finally block. A finally block is always used with a try block.

## Syntax

The syntax for using a finally block is

```java title=Example.java

finally  {
    // Code for finally block
}
```

A finally block starts with the keyword finally, which is followed by an opening brace and a closing brace.

The code for a finally block is placed inside the braces.

There are two possible combinations of try, catch, and finally blocks: try-catch-finally or try-finally.

A try block may be followed by zero or more catch blocks.

A try block can have a maximum of one finally block.

A try block must have either a catch block, a finally block, or both.

The syntax for a try-catch-finally block is

```java title=Example.java
try  {
    // Code fortry block
}
catch(Exception1 e1)  {
    // Code forcatch block
}
finally  {
    // Code for finally block
}
```

The syntax for a try-finally block is

```java title=Example.java
try  {
    // Code fortry block
}
finally  {
    // Code for finally block
}
```

A finally block is guaranteed to be executed no matter what happens in the associated try and/or catch block.

Typically, we use a finally block to write cleanup code.

For example, we may obtain some resources that must be released when we are done with them.

A try-finally block lets you implement this logic.

Your code structure would look as follows:

```java title=Example.java
try  {
    // Obtain   anduse  some resources here
}
finally  {
    // Release the   resources that were  obtained in the   try  block
}
```

## Example

The following code demonstrates the use of a finally block.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int x = 10, y = 0, z = 0;
    try {/*fromwww.java2s.com*/
      System.out.println("Before dividing x  by  y.");
      z = x / y;
      System.out.println("After dividing x  by  y.");
    } catch (ArithmeticException e) {
      System.out.println("Inside  catch block a.");
    } finally {
      System.out.println("Inside finally  block a.");
    }
    try {
      System.out.println("Before setting  z  to 2.");
      z = 2;
      System.out.println("After setting  z  to 2.");
    }
    catch (Exception e) {
      System.out.println("Inside  catch block b.");
    } finally {
      System.out.println("Inside finally  block b.");
    }
    try {
      System.out.println("Inside try block c.");
    }
    finally {
      System.out.println("Inside finally  block c.");
    }
    try {
      System.out.println("Before  executing System.exit().");
      System.exit(0);
      System.out.println("After  executing System.exit().");
    } finally {
      // This finally block will not be executed
// because application exits in try block
      System.out.println("Inside finally  block d.");
    }
  }
}
```

The code above generates the following result.

## Rethrowing an Exception

An exception that is caught can be rethrown.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    try {/*www.java2s.com*/
      m1();
    } catch (MyException e) {
      // Print the stack trace
      e.printStackTrace();
    }
  }
  publicstaticvoid m1() throws MyException {
    try {
      m2();
    } catch (MyException e) {
      e.fillInStackTrace();
      throw e;
    }
  }
  publicstaticvoid m2() throws MyException {
    thrownew MyException("An  error has  occurred.");
  }
}
class MyException extends Exception {
  public MyException() {
    super();
  }
  public MyException(String message) {
    super(message);
  }
  public MyException(String message, Throwable cause) {
    super(message, cause);
  }
  public MyException(Throwable cause) {
    super(cause);
  }
}
```

The code above generates the following result.

- « Previous
