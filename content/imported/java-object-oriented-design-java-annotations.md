---
title: Java Object Oriented Design - Java Annotations
nav: Java Object Oriented Desig...
description: An annotation in Java lets us associate metadata to the program elements.
section: Imported - java2s Archive
order: 50191
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0700__Java_Annotations.html
---
## What Are Annotations?

An annotation in Java lets us associate metadata to the program elements.

The program elements may be a package, a class, an interface, a field of a class, a local variable, a method, a parameter of a method, an enum, an annotation, a type parameter in a generic type/method declaration, etc.

We can annotate any declaration or type in a Java program. An annotation is used as a modifier in a declaration of a program element like any other modifiers (public, private, final, static, etc.).

Unlike a modifier, an annotation does not modify the meaning of the program elements. It is a note for the program element.

## Declaring an Annotation Type

Declaring an annotation type is similar to declaring an interface type.

An annotation type is a special kind of interface type.

We use the interface keyword preceded by the @ sign to declare an annotation type.

The following is the general syntax for declaring an annotation type:

```java title=Example.java
<modifiers> @interface <annotation-type-name>  {
    // Annotation type body
}
```

The <modifiers> for an annotation declaration is the same as for an interface declaration.

We can declare an annotation type as public or package level.

The @ sign and the interface keyword may be separated by whitespaces or they can be placed together.

By convention, they are placed together as @interface.

The interface keyword is followed by an annotation type name. It should be a valid Java identifier.

The annotation type body is placed within braces.

The following code creates an annotation to annotate program elements with the version information.

```java title=Example.java
public  @interface  Version {
    int  major();
    int  minor();
}
```

We have declared two abstract methods in the Version annotation type: major() and minor().

Abstract methods in an annotation type are called elements.

An annotation can declare zero or more elements and they are declared as abstract methods. The abstract method names are the names of the elements of the annotation type.

In the code above we declared two elements, major and minor, for the Version annotation type. The data types of both elements are int.

We need to import an annotation type the same way we import any other types.

## Annotation Instance

To create an instance of an annotation type and use it to annotate a program element, we use the following syntax:

```java title=Example.java
@annotationType(name1=value1,  name2=value2, names3=values3...)
```

The annotation type is preceded by an @ sign followed by a list of comma-separated name=value pairs enclosed in parentheses.

The name in a name=value pair is the name of the element declared in the annotation type and the value is supplied by the user.

The name=value pairs do not have to appear in the same order as they are declared in the annotation type.

The following code uses an annotation of the Version type, with the major element value set to 1 and the minor element value set to 0.

```java title=Example.java
@Version(major=1, minor=0)
```

We can use the annotation type's fully qualified name as

```java title=Example.java
@com.java2s.annotation.Version(major=0,  minor=1)
```

We can annotate the class declaration as

```java title=Example.java
@Version(major=1, minor=0)
publicclass  VersionTest {
}
```

We can mix the annotation for a program element with its other modifiers.

```java title=Example.java
@Version(major=1, minor=0)  publicclass  VersionTest {
}
public  @Version(major=1, minor=0)  class  VersionTest {
}
```

Full source code

```java title=Example.java
@interface Version {
  int major();int minor();
}
@Version(major = 1, minor = 0)
publicclass Main {
  @Version(major = 1, minor = 1)
  privateint xyz = 110;
  @Version(major = 1, minor = 0)
  public Main() {
  }
  @Version(major = 1, minor = 1)
  public Main(int xyz) {
    this.xyz = xyz;
  }
  @Version(major = 1, minor = 0)
  publicvoid printData() {
  }
  @Version(major = 1, minor = 1)
  publicvoid setXyz(int xyz) {
    @Version(major = 1, minor = 2)
    int newValue = xyz;
    this.xyz = xyz;
  }
}
```

- « Previous
