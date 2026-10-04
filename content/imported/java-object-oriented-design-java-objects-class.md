---
title: Java Object Oriented Design - Java Objects Class
nav: Java Object Oriented Desig...
description: Java has a utility class Objects in the java.util package for working with objects.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0230__Java_Objects_Class.html
---
Java has a utility class Objects in the java.util package for working with objects.

It consists of all static methods. Most of the methods of the Objects class deal with null values gracefully.

The following is the list of methods in the class. Their descriptions follow the list.

- int compare(T a, T b, Comparator c) Returns 0 if the arguments are identical and c.compare(a, b) otherwise. Consequently, if both arguments are null 0 is returned.
- boolean deepEquals(Object a, Object b) check if two objects are deeply equal. It returns true if both arguments are deeply equal. Otherwise, it returns false. It returns true if both arguments are null.
- boolean equals(Object a, Object b) compares two objects for equality. It returns true if both arguments are equal. Otherwise, it returns false. It returns true if both arguments are null.
- int hash(Object... values) generates a hash code for all specified objects. It can be used to compute the hash code for an object, which is based on the multiple instance fields.
- int hashCode(Object o) returns the hash code value of the specified object. If the argument is null, it returns 0.
- boolean isNull(Object obj) The isNull() method returns true if the specified object is null. Otherwise, it returns false. You can also check whether an object is null using the comparison operator ==, for example, obj == null returns true of obj is null.
- boolean nonNull(Object obj) performs the check opposite of what the isNull() method does.
- T requireNonNull(T obj) T requireNonNull(T obj, String message) T requireNonNull(T obj, Supplier messageSupplier) checks if the argument is not null. If the argument is null, it throws a NullPointerException. This method is designed for validating parameters of methods and constructors. The second version can specify the message for the NullPointerException that is thrown when the argument is null. The third version of the method takes a Supplier as the second argument.
- String toString(Object o) String toString(Object o, String nullDefault) The toString() method returns a "null" string if the argument is null. For a non-null argument, it returns the value returned by calling the toString() method on the argument.

## hash code

The following code demonstrates how to use the method from the Objects class to calculate the hash code.

```java title=Example.java
import java.util.Objects;
public class Main {
  public static void main(String[] args) {
    // Compute hash code for two integers, a char, and a string
 int hash = Objects.hash(10, 800, '\u20b9', "Hello");
    System.out.println("Hash Code is " + hash);
  }
}
```

The code above generates the following result.

## equals

The following code shows how to use equals method from Objects class to compare two objects.

```java title=Example.java
import java.util.Objects;
public class Main {
  public static void main(String[] args) {
    // Test for equality
 boolean isEqual = Objects.equals(null, null);
    System.out.println("null is  equal to null:  " + isEqual);
    isEqual = Objects.equals(null, "XYZ");
    System.out.println("null is  equal to XYZ: " + isEqual);
  }
}
```

The code above generates the following result.

## toString

The following code shows how to use toString method from Objects to convert object to a String.

```java title=Example.java
import java.util.Objects;
public class Main {
  public static void main(String[] args) {
    // toString() method test
    System.out.println("toString(null) is  " + Objects.toString(null));
    System.out.println("toString(null, \"XXX\")  is "
        + Objects.toString(null, "XXX"));
  }
}
```

The code above generates the following result.

## requireNonNull

The following code shows how to use requireNonNull from Objects class.

```java title=Example.java
import java.time.Instant;
import java.util.Objects;
import java.util.function.Supplier;
public class Main {
  public static void main(String[] args) {
    try {
      printName("A");
      printName(null);
    } catch (NullPointerException e) {
      System.out.println(e.getMessage());
    }
    try {
      Supplier<String> messageSupplier = () -> "Name is  required. Error generated on  "
          + Instant.now();
      printNameWithSuplier("asdf", messageSupplier);
      printNameWithSuplier(null, messageSupplier);
    } catch (NullPointerException e) {
      System.out.println(e.getMessage());
    }
  }
  public static void printName(String name) {
    Objects.requireNonNull(name, "Name is required.");
    System.out.println("Name is " + name);
  }
  public static void printNameWithSuplier(String name,
      Supplier<String> messageSupplier) {
    Objects.requireNonNull(name, messageSupplier);
  }
}
```

The code above generates the following result.

- « Previous
