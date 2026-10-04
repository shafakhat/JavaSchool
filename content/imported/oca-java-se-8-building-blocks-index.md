---
title: OCA Java SE 8 Building Blocks - Java Class Structure
nav: OCA Java SE 8 Building Blo...
description: Variables hold the state of the program, and methods operate on that state.
section: Imported - java2s Archive
order: 50000
source: https://www.java2s.com/Tutorials/Java/OCA_Java_SE_8_Building_Blocks/index.html
---
In Java programs, classes are the basic building blocks.

To use most classes, you have to create objects.

An object is a runtime instance of a class in memory.

## Fields and Methods

Java classes have two primary elements: methods and fields.

Together these are called the members of the class.

Variables hold the state of the program, and methods operate on that state.

## Example

The simplest Java class you can write looks like this:

```java title=Example.java
publicclass Animal {
}
```

Java defines special words in code as keyword.

The public keyword means the class can be used by other classes.

The class keyword indicates you're defining a class.

Animal gives the name of the class.

The following code adds field to the class:

```java title=Example.java
publicclass Animal {
    String name;
}
```

In the code above we defined a variable named name.

We also define the type of that variable to be a String.

A String is a value to store characters, such as "this is a string".

String is a class from Java language.

The following code adds methods to the class:

```java title=Example.java
publicclass Animal {
     String name;
     public String getName() {
           return name;
     }
     public void setName(String newName) {
           name = newName;
     }
}
```

## Note

public before the method name signify that this method may be called from other classes.

The method public String getName() returns a String.

public void setName(String newName) has a special return type called void.

void means that no value is returned.

setName has one parameter named newName, and it is of type String.

The caller should pass in one String parameter and expect nothing to be returned.

The full declaration of a method is called a method signature.

In the following code the return type is int, which is a numeric type.

There's one parameter named month, which is of type int as well.

```java title=Example.java
public int numberVisitors(int month)
```

## Comments

Comments aren't executable code and can be placed anywhere.

Comments make your code easier to read.

There are three types of comments in Java.

The first is called a single-line comment:

```java title=Example.java
// comment until end of line
```

A single-line comment begins with two slashes.

Anything after that on the same line is ignored by the compiler.

Next comes the multiple-line comment:

```java title=Example.java
/* Multiple
 * line comment
 */
```

A multiple-line comment includes anything starting from the symbol /* until the symbol */.

The third one is a Javadoc comment:

```java title=Example.java
 /**
 * Javadoc multiple-line comment
 * @author JavaSchool
 */
```

Javadoc comment is similar to a multiline comment except it starts with /**.

Javadoc comments have a special structure for the Javadoc tool.

## Classes vs. Files

Each Java class is normally defined in its own *.java file. And the file name is the public class name.

The class is usually public, which means any code can call it.

Java does not require that the class be public. Java class can be non-public.

For example, this class is just fine:

```java title=Example.java
class Animal {
    String name;
}
```

You can put two classes in the same file.

When putting two classes in one file, at most one of the classes in the file can be public.

That means a file containing the following is also fine:

```java title=Example.java
publicclass Animal {
   private String name;
}
class Animal2 {
}
```

The public class needs to match the filename.

public class Animal2 would not compile in a file named Animal.java.

## main() Method

A Java program begins execution with its main() method.

The following code defines a class with a main() method:

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] args) {
  }
}
```

To compile and execute this code, type it into a file called Main.java and execute the following:

```java title=Example.java
$ javac Main.java
$ java Main
```

To compile Java code, the file must have the extension .java.

The name of the file must match the name of the class.

The result is a file of bytecode by the same name, but with a .class filename extension.

Bytecode consists of instructions that the JVM knows how to execute.

We must omit the .class extension to run Main.java because the period has a reserved meaning in the JVM.

The following code shows how to use the args parameter.

First we modify the Main program to print out the first two arguments passed in:

```java title=Example.java
publicclass Main {
  publicstatic void main(String[] args) {
     System.out.println(args[0]);
     System.out.println(args[1]);
  }
}
```

args[0] accesses the first element of the array. That's right: array indexes begin with 0 in Java. To run it, type this:

```java title=Example.java
$ javac Main.java
$ java Main First Second
```

The output is what you might expect:

```java title=Example.java
First
Second
```

The program correctly identifies the first two "words" as the arguments. Spaces are used to separate the arguments.

If you want spaces inside an argument, you need to use quotes as in this example:

```java title=Example.java
$ javac Main.java
$ java Main "One Two" Second
```

Now we have a space in the output:

```java title=Example.java
One Two
Second
```

All command-line arguments are treated as String objects, even if they represent another data type:

```java title=Example.java
$ javac Main.java
$ java Main Second 2
```

No matter. You still get the values output as Strings. In Chapter 2, you'll learn how to convert Strings to numbers.

```java title=Example.java
Second
2
```

What happens if you don't pass in enough arguments?

```java title=Example.java
$ javac Main.java
$ java Main First
```

Reading args[0] goes fine and First is printed out.

There's no second argument!

Java prints out an exception telling you it has no idea what to do with this argument at position 1.

```java title=Example.java
First
Exception in thread "main"
java.lang.ArrayIndexOutOfBoundsException: 1
       at mainmethod.Main.main(Main.java:4)
```
