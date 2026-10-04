---
title: Java Array Variables
nav: Java Array Variables
description: A Java array variable has two parts: array type and array object.
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20131220111545/http://www.java2s.com:80/Tutorials/Java/Array/Java_Array_Variables.htm
---
In this chapter you will learn:

- What is Java array variable
- Syntax for Java array variable definition
- Note for Java array variable definition
- Alternative Syntax for Java array variable definition
- Create an array
- Single statement for declare and create an array

### Description

A Java array variable has two parts: array type and array object.

The array type is the type of the array variable. The array object is the memory allocated for an array variable.

When defining an array we can first define the array type and allocate the memory later.

### Syntax

You could declare the integer array variable myIntArray with the following statement:

```java title=Example.java
int[] myIntArray;                // Declare an integer array variable
```

### Note

The variable myIntArray is now a type for an integer array. No memory has been allocated to hold an array itself.

Later we will create the array by allocating memory and specify how many elements it can contain.

The square brackets following the type indicates that the variable is for an array of int values, and not for storing a single value of type int.

The type of the array variable is int[].

### Alternative Syntax

We can use an alternative notation for declaring an array variable:

```java title=Example.java
int myIntArray[];                // Declare an integer array variable
```

Here the square brackets appear after the variable name, rather than after the type name.

This is exactly equivalent to the previous statement. int[] form is preferred since it indicates more clearly that the type is an array of values of type int.

The following two declarations are equivalent:

```java title=Example.java
int a1[] = newint[3];
int[] a2 = newint[3];
```

### Array create

After you have declared an array variable, you can define an array that it references:

```java title=Example.java

myIntArray = newint[10];        // Define an array of 10 integers
```

This statement creates an array that stores 10 values of type int and stores a reference to the array in the variable myIntArray.

The reference is simply where the array is in memory.

### Single Statement

You could also declare the array variable and define the array of type int to hold 10 integers with a single statement.

```java title=Example.java
int[] myIntArray = newint[10];            //An array of 10 integers
```

The first part of the definition specifies the type of the array. The element type name, int in this case, is followed by an empty pair of square brackets.

The part of the statement that follows the equal sign defines the array.

The keyword new indicates that you are allocating new memory for the array, and int[10] specifies that the capacity is 10 variables of type int in the array.

#### Next chapter...

What you will learn in the next chapter:

- What are the Java Array Initial Values
- Initial value for Java array
