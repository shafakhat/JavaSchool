---
title: Java Object Oriented Design - Java Access Level
nav: Java Object Oriented Desig...
description: When we refer to a class by its simple name, the compiler looks for that class declaration in the same package where the referring class is.
section: Imported - java2s Archive
order: 50138
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0020__Java_Class_Access_Level.html
---
```java title=Example.java
```

Class simple name is the name between class keyword and {.

When we refer to a class by its simple name, the compiler looks for that class declaration in the same package where the referring class is.

We can use full name to reference a class as follows.

```java title=Example.java
com.java2s.Dog aDog;
```

The general syntax specifying access-level for a class is

```java title=Example.java
<access level modifier>class <class name> {
    // Body of the class
}
```

There are only two valid values for <access level modifier> in a class declaration:

- no value
- public

No value is known as package-level access. A class with package-level access can be accessed only within the package in which it has been declared.

Class with public access level modifier can be accessed from any package in the application.

```java title=Example.java
package  com.java2s;
publicclass Dog  {
}
```

- « Previous
