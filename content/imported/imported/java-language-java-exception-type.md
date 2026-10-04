---
title: Java Tutorial - Java Exception Type
nav: Java Tutorial - Java Excep...
description: The following diagram shows the Java exception type hierarchy:
section: Imported - java2s Archive
order: 50453
source: https://www.java2s.com/Tutorials/Java/Java_Language/6020__Java_Exception_Type.html
---
```java title=Example.java
```

The following diagram shows the Java exception type hierarchy:

```java title=Example.java

Throwable
 +---Exception.
 |    +--- RuntimeException
 +---Error
```

Exception and its subclasses are used for exceptional conditions that user programs should catch. You can subclass Exception to create your own custom exception types.

Error defines exceptions that are not expected to be caught under normal circumstances. Java run-time system use Error to indicate errors in the run-time environment. Stack overflow is an example of such an error.

## Uncaught Exceptions

This small program includes an expression that intentionally causes a divide-by-zero error:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int d = 0;
    int a = 42 / d;
  }
}
```

Here is the exception generated when this example is executed:

## Example

Here is another version of the preceding program that introduces the same error but in a method separate from main( ):

```java title=Example.java
publicclass Main {
  staticvoid subroutine() {
    int d = 0;/*fromwww.java2s.com*/int a = 10 / d;
  }
  publicstaticvoid main(String args[]) {
    subroutine();
  }
}
```

The resulting stack trace from the default exception handler shows how the entire call stack is displayed:

## Example 2

You can display exception description message in a println( ) statement.

For example, the catch block can be written like this:

```java title=Example.java
import java.util.Random;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String args[]) {
    int a = 0, b = 0, c = 0;
    Random r = new Random();
    for (int i = 0; i < 32000; i++) {
      try {
        b = r.nextInt();
        c = r.nextInt();
        a = 12345 / (b / c);
      } catch (ArithmeticException e) {
        System.out.println("Exception: " + e);
        a = 0; // set a to zero and continue
      }
      System.out.println("a: " + a);
    }
  }
}
```

The code above generates the following result.

## What are Java's Built-in Exceptions

Exceptions subclassing RuntimeException need not be included in any method's throws list. These are called unchecked exceptions.

The unchecked exceptions defined in java.lang are listed in the following table.

Exception  Meaning
---  ---
ArithmeticException  Arithmetic error, such as divide-by-zero.
ArrayIndexOutOfBoundsException  Array index is out-of-bounds.
ArrayStoreException  Assignment to an array element of an incompatible type.
ClassCastException  Invalid cast.
EnumConstantNotPresentException  An attempt is made to use an undefined enumeration value.
IllegalArgumentException  Illegal argument used to invoke a method.
IllegalMonitorStateException  Illegal monitor operation, such as waiting on an unlocked thread.
IllegalStateException  Environment or application is in incorrect state.
IllegalThreadStateException  Requested operation not compatible with current thread state.
IndexOutOfBoundsException  Some type of index is out-of-bounds.
NegativeArraySizeException  Array created with a negative size.
NullPointerException  Invalid use of a null reference.
NumberFormatException  Invalid conversion of a string to a numeric format.
SecurityException  Attempt to violate security.
StringIndexOutOfBounds  Attempt to index outside the bounds of a string.
TypeNotPresentException  Type not found.
UnsupportedOperationException  An unsupported operation was encountered.

The checked exceptions are listed in the following table.

Exception  Meaning
---  ---
ClassNotFoundException  Class not found.
CloneNotSupportedException  Attempt to clone an object that does not implement the Cloneable interface.
IllegalAccessException  Access to a class is denied.
InstantiationException  Attempt to create an object of an abstract class or interface.
InterruptedException  One thread has been interrupted by another thread.
NoSuchFieldException  A requested field does not exist.
NoSuchMethodException  A requested method does not exist.

## Java custom exception class

You can create your own exception class by defining a subclass of Exception.

The Exception class does not define any methods of its own. It inherits methods provided by Throwable.

The following program creates a custom exception type.

```java title=Example.java
class MyException extends Exception {
  privateint detail;
/*www.java2s.com*/
  MyException(int a) {
    detail = a;
  }
  public String toString() {
    return"MyException[" + detail + "]";
  }
}
publicclass Main {
  staticvoid compute(int a) throws MyException {
    System.out.println("Called compute(" + a + ")");
    if (a > 10)
      thrownew MyException(a);
    System.out.println("Normal exit");
  }
  publicstaticvoid main(String args[]) {
    try {
      compute(1);
      compute(20);
    } catch (MyException e) {
      System.out.println("Caught " + e);
    }
  }
}
```

The code above generates the following result.

## Java chained exceptions

The chained exception allows you to associate another exception with an exception. This second exception describes the cause of the first exception.

To allow chained exceptions, two constructors and two methods were added to Throwable.

```java title=Example.java

Throwable(Throwable causeExc)
Throwable(String msg, Throwable causeExc)
```

Here is an example that illustrates the mechanics of handling chained exceptions:

```java title=Example.java
publicclass Main {
  staticvoid demoproc() {
    NullPointerException e = new NullPointerException("top layer");
    e.initCause(new ArithmeticException("cause"));
    throw e;//www.java2s.com
  }
  publicstaticvoid main(String args[]) {
    try {
      demoproc();
    } catch (NullPointerException e) {
      System.out.println("Caught: " + e);
      System.out.println("Original cause: " + e.getCause());
    }
  }
}
```

The code above generates the following result.

- « Previous
