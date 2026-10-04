---
title: Java Object Oriented Design - Java main Method
nav: Java Object Oriented Desig...
description: Let's discuss the main() method that we have been using to run our classes.
section: Imported - java2s Archive
order: 50144
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0070__Java_main_Method.html
---
```java title=Example.java
« Previous
```

- Next »

Let's discuss the main() method that we have been using to run our classes.

The main() method declaration is as follows:

```java title=Example.java
publicstatic  void  main(String[]  args)  {
}
```

Two modifiers, public and static, are used in the declaration of the main() method.

The public modifier makes it accessible from anywhere in the application as long as the class in which it is declared is accessible.

The static modifier makes it a class method, so it can be invoked using a class name.

Its return type is void, which means it does not return a value to its caller.

Its name is main and it accepts one parameter of type String array (String[]).

main() method is the entry method for Java application. For example, you would use the following command to run the Main class:

```java title=Example.java

java  com.java2s.Main
```

The main() method is invoked by the JVM when you run a class.

- Next »
- « Previous
