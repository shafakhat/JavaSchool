---
title: Java Object Oriented Design - Java Custom Exception
nav: Java Object Oriented Desig...
description: <Class Modifiers> class <Class Name> extends <Exception Class Name> {
section: Imported - java2s Archive
order: 50176
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0410__Java_Custom_Exception.html
---
```java title=Example.java
« Previous
```

- Next »

We can create our own exception classes.

They must extend an existing exception class.

```java title=Example.java

<Class Modifiers> class <Class Name> extends <Exception Class Name> {
}
```

```java title=Example.java

<Class Name> is the exception class name.
```

To create a MyException class, which extends the java.lang.Exception class.

## Syntax

The syntax would be as follows:

```java title=Example.java
publicclass MyException  extends  Exception  {
}
```

An exception class is like any other classes in Java. Typically, we do not add any methods to our exception class.

Many useful methods that can be used to query an exception object's state are declared in the Throwable class.

## Custom Exception Class Constructors

Typically, we include four constructors to our exception class.

All constructors will call the corresponding constructor of its superclass using the super keyword.

```java title=Example.java
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

The first constructor creates an exception with null as its detailed message.

The second constructor creates an exception with a detailed message.

The third and fourth constructors let you create an exception by wrapping another exception with/without a detailed message.

You can throw an exception of type MyException.

```java title=Example.java
thrownew MyException("Your  message  goes  here");
```

We can use the MyException class in a throws clause in a method/constructor declaration or as a parameter type in a catch block.

```java title=Example.java
public void  m1()  throws   MyException  {
}
```

or catch MyException class

```java title=Example.java
try  {
}catch(MyException e)  {
}
```

## Throwable

The following list shows some of the commonly used methods of the Throwable class.

Throwable class is the superclass of all exception classes in Java. All of the methods shown in this table are available in all exception classes.

- Throwable getCause() returns the cause of the exception. If the cause of the exception is not set, it returns null.
- String getMessage() returns the detailed message of the exception.
- StackTraceElement[] getStackTrace() returns an array of stack trace elements.
- Throwable initCause(Throwable cause) sets the cause of an exception. There are two ways to set an exception as the cause of an exception. Other way is to use the constructor, which accepts the cause as a parameter.
- void printStackTrace() prints the stack trace on the standard error stream.
- void printStackTrace(PrintStream s) prints the stack trace to the specified PrintStream object.
- void printStackTrace(PrintWriter s) prints the stack trace to the specified PrintWriter object.
- String toString() returns a short description of the exception object.

## Exception

The following code demonstrates the use of the printStackTrace() method for an exception class.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    try {//www.java2s.com
      m1();
    } catch (MyException e) {
      e.printStackTrace(); // Print the stack trace
    }
  }
  publicstaticvoid m1() throws MyException {
    m2();
  }
  publicstaticvoid m2() throws MyException {
    thrownew MyException("Some  error has  occurred.");
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

## Example 2

The following code shows how to write Stack Trace of an Exception to a String

```java title=Example.java
import java.io.PrintWriter;
import java.io.StringWriter;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    try {
      m1();
    } catch (MyException e) {
      String str = getStackTrace(e);
      System.out.println(str);
    }
  }
  publicstaticvoid m1() throws MyException {
    m2();
  }
  publicstaticvoid m2() throws MyException {
    thrownew MyException("Some  error has  occurred.");
  }
  publicstatic String getStackTrace(Throwable e) {
    StringWriter strWriter = new StringWriter();
    PrintWriter printWriter = new PrintWriter(strWriter);
    e.printStackTrace(printWriter);
    // Get the stack trace as a string
    String str = strWriter.toString();
    return str;
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

- Next »
- « Previous
