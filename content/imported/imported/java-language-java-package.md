---
title: Java Tutorial - Java Package
nav: Java Tutorial - Java Package
description: Packages are containers for classes. Packages are used to keep the class name space compartmentalized. In Java, package is mapped to a folder on your hard drive.
section: Imported - java2s Archive
order: 50450
source: https://www.java2s.com/Tutorials/Java/Java_Language/5120__Java_Package.html
---
```java title=Example.java
« Previous
```

- Next »

Packages are containers for classes. Packages are used to keep the class name space compartmentalized. In Java, package is mapped to a folder on your hard drive.

## Syntax

To define a package, include a package command as the first statement in a Java source file. Any classes declared within that file will belong to the specified package.

If you omit the package statement, the class names are put into the default package, which has no name.This is the general form of the package statement:

```java title=Example.java
package packageName;
```

## Create a hierarchy of packages

To create a hierarchy of packages, separate each package name from the one above it by use of a period. The general form of a multileveled package statement:

```java title=Example.java
package pkg1[.pkg2[.pkg3]];
```

A package hierarchy must be reflected in the file system of your Java development system.

## Java package maps to directory

Java package maps to physical directory on your hard drive. As what is defined in the following example, you have to save the following file to a file named Main.java and create a folder named MyPack to actually store Main.java file.

```java title=Example.java
package MyPack;
publicclass Main {
  publicstaticvoid main(String args[]) {
    System.out.println("hi");
  }
}
```

Then try executing the class, using the following command line:

## Java Packages Import

In a Java source file, import statements occur immediately following the package statement and before class definitions.

This is the general form of the import statement:

```java title=Example.java

import pkg1[.pkg2].(classname|*);
```

* means including all classes under that package. For example,

```java title=Example.java

import java.lang.*;
```

Any place you use a class name, you can use its fully qualified name, which includes its full package hierarchy.

For example, this fragment uses an import statement:

```java title=Example.java

import java.util.*;
class MyDate extends Date {
}
```

The same example without the import statement looks like this:

```java title=Example.java
class MyDate extends java.util.Date {
}
```

## static import

In order to access static members, it is necessary to qualify references. For example, one must say:

```java title=Example.java

double r = Math.cos(Math.PI * theta);
```

The static import construct allows unqualified access to static members.

```java title=Example.java

import static java.lang.Math.PI;
```

or:

```java title=Example.java

import static java.lang.Math.*;
```

Once the static members have been imported, they may be used without qualification:

```java title=Example.java

double r = cos(PI * theta);
```

The static import declaration imports static members from classes, allowing them to be used without class qualification.

## Java Source File

All Java source files must end with the .java extension. A source file should contain, at most, one top-level public class definition. If a public class is present, the class name should match the unextended filename.

Three top-level elements known as compilation units may appear in a file. None of these elements is required.

If they are present, then they must appear in the following order:

- Package declaration
- Import statements
- Class, interface, and enum definitions

```java title=Example.java
package MyPack;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String args[]) {
    System.out.println(new Date());
  }
}
```

- Next »
- « Previous
