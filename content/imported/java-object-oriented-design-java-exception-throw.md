---
title: Java Object Oriented Design - Java Exception Throw
nav: Java Object Oriented Desig...
description: If a piece of code may throw a checked exception, we have two options:
section: Imported - java2s Archive
order: 50175
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0400__Java_Exception_Throw.html
---
```java title=Example.java
```

If a piece of code may throw a checked exception, we have two options:

- Handle the checked exception with a try-catch block.
- Specify in your method/constructor declaration with throws clause.

## Syntax

The general syntax for a throws clause is

```java title=Example.java
<modifiers> <return type> <method name>(<params>) throws<List of Exceptions>{
}
```

The keyword throws is used to specify a throws clause.

The throws clause is placed after the closing parenthesis of the method's parameters list.

The throws keyword is followed by a comma-separated list of exception types.

## Example

The following code shows how to use a throws Clause in a Method's Declaration

```java title=Example.java
import java.io.IOException;
publicclass Main {
  publicstatic void readChar() throws IOException {
    int input = System.in.read();
  }
}
```

Here is the code showing how to use it.

## Example 2

```java title=Example.java
import java.io.IOException;
publicclass Main {
  publicstaticvoid readChar() throws IOException {
    int input = System.in.read();
    System.out.println(input);
  }
  publicstaticvoid main(String[] args) {
    try {
      readChar();
    } catch (IOException e) {
      System.out.println("Error occurred.");
    }
  }
}
```

The code above generates the following result.

## Example 3

We can continue to throw exception.

```java title=Example.java
import java.io.IOException;
publicclass Main {
  publicstaticvoid readChar() throws IOException {
    int input = System.in.read();
    System.out.println(input);
  }
  publicstaticvoid main(String[] args) throws IOException {
    readChar();
  }
}
```

The code above generates the following result.

## Throwing an Exception

We can throw an exception in our code using a throw statement.

The syntax for a throw statement is

```java title=Example.java
throw <A throwable object reference>;
```

throw is a keyword, which is followed by a reference to a throwable object.

A throwable object is an instance of a class, which is a subclass of the Throwable class, or the Throwable class itself.

The following is an example of a throw statement, which throws an IOException:

```java title=Example.java
// Create an  object of  IOException
IOException e1  = new IOException("File not  found");
// Throw the   IOException
throw  e1;
```

We can create a throwable object and throw it in one statement.

```java title=Example.java
// Throw an  IOException
thrownew IOException("File not  found");
```

If we throw a checked exception, we must handle it with a try-catch block, or using a throws clause in the method or constructor declaration.

These rules do not apply if you throw an unchecked exception.

- « Previous
