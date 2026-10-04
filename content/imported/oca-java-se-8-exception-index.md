---
title: OCA Java SE 8 Exception - Java Exception
nav: OCA Java SE 8 Exception - ...
description: Java has a Throwable superclass for all objects that represent these events.
section: Imported - java2s Archive
order: 50005
source: https://www.java2s.com/Tutorials/Java/OCA_Java_SE_8_Exception/index.html
---
## Understanding Exception Types

An exception is an event that alters program flow.

Java has a Throwable superclass for all objects that represent these events.

Not all of them have the word exception in their classname.

Error means something went so horribly wrong that your program should not attempt to recover from it.

A runtime exception is defined as the RuntimeException class and its subclasses.

Runtime exceptions tend to be unexpected but not necessarily fatal.

For example, accessing an invalid array index is unexpected.

Runtime exceptions are also known as unchecked exceptions.

A runtime (unchecked) exception is a specific type of exception. All exceptions occur at the time that the program is run.

A checked exception includes Exception and all subclasses that do not extend RuntimeException.

Checked exceptions tend to be more anticipated-for example, trying to read a file that doesn't exist.

Java has a rule called the handle or declare rule.

For checked exceptions, Java requires the code to either handle them or declare them in the method signature.

For example, this method declares that it might throw an exception:

```java title=Example.java
void fall() throws Exception {
    thrownew Exception();
}
```

throw tells Java that you want to throw an Exception.

throws declares that the method might throw an Exception. It might not.

An example of a runtime exception is a NullPointerException, which happens when you try to call a member on a null reference.

## Throwing an Exception

The exception can be thrown from wrong code. For example:

```java title=Example.java
String[] animals = new String[0];
System.out.println(animals[0]);
```

This code throws an ArrayIndexOutOfBoundsException.

The code can use throw keyword to throw an exception. Java can write statements like these:

```java title=Example.java
thrownew Exception();
thrownew Exception("Hi");
thrownew RuntimeException();
thrownew RuntimeException("Runtime.");
```

The throw keyword tells Java to throw exception and the exception would be handled by the code somewhere.

When creating an exception, pass a String parameter with a message or you can pass no parameters and use the default message.

Here is the summary of three types of exceptions in the Java code.

The first type is Runtime exception which is the subclass of RuntimeException. For Runtime Exception we can catch them in the code but we are not required to do so.

The second type is the Checked exception which is Subclass of Exception but not subclass of RuntimeException. For the checked exception we are required to catch them.

The last type is the Error which is the Subclass of Error. We cannot catch them and are not required to catch them.
