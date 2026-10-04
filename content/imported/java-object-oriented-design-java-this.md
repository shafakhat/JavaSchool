---
title: Java Object Oriented Design - Java this
nav: Java Object Oriented Desig...
description: Java has a keyword called this. It is a reference to the current instance of a class.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0080__Java_this.html
---
## What Is this?

Java has a keyword called this. It is a reference to the current instance of a class.

It can be used only in the context of an instance.

The following code shows how to use this keyword.

```java title=Example.java
public class Main {
  int varA = 1;
  int varB = varA; // Assign value of varA to varB
  int varC = this.varA; // Assign value of varA to varC
}
```

We need to qualify an instance variable with the keyword this and a class variable with the class name when the instance variable or the class variable is hidden by another variable with the same name.

## Example

The following code shows how to use the this Keyword to Refer to an Instance Variable Whose Name Is Hidden by a Local Variable.

```java title=Example.java
public class Main {
  int num = 2014; // An instance variable
 void printNum(int num) {
    System.out.println("Parameter num: " + num);
    System.out.println("Instance variable num: " + this.num);
  }
  public static void main(String[] args) {
    Main tt6 = new Main();
    tt6.printNum(2000);
  }
}
```

The code above generates the following result.

## Note

Sometimes it is easier to keep the variable names the same, as they represent the same thing.

For example, the following code is very common:

The Student class declares an instance variable id. In its setId() method, it also names the parameter id, and uses this.id to refer to the instance variable.

It also uses this.id to refer to the instance variable id in its getId() method.

```java title=Example.java
public class Student {
  private int id; // An instance variable
public void setId(int id) {
    this.id = id;
  }
  public int getId() {
    return this.id;
  }
}
```

We can use the keyword this to qualify an instance method name. The following code shows the m1() method invoking the m2() method using the keyword this.

```java title=Example.java
public class Main {
  void m1() {
    // Invoke the m2() method
    this.m2(); // same as "m2();"
  }
  void m2() {
    // do something
  }
}
```

- « Previous
