---
title: Java Object Oriented Design - Java Restrictions on Annotation Types
nav: Java Object Oriented Desig...
description: An annotation type cannot inherit from another annotation type.
section: Imported - java2s Archive
order: 50192
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0710__Java_Annotations_Restrictions.html
---
```java title=Example.java
« Previous
```

- Next »

## Restrictions on Annotation Types

An annotation type cannot inherit from another annotation type.

Every annotation type implicitly inherits the java.lang.annotation.Annotation interface, which is declared as follows:

```java title=Example.java

package  java.lang.annotation;
publicinterface  Annotation  {
   boolean equals(Object  obj);
   int  hashCode();
   String toString();
   Class<? extends  Annotation> annotationType();
}
```

Method declarations in an annotation type cannot specify any parameters.

Method declarations in an annotation type cannot have a throws clause.

The return type of a method declared in an annotation type must be one of the following types:

- Any primitive type: byte, short, int, long, float, double, boolean, and char
- java.lang.String
- java.lang.Class
- An enum type
- An annotation type
- An array of any of the above mentioned type, for example, String[], int[], etc.

The return type cannot be a nested array. For example, you cannot have a return type of String[][] or int[][].

You can declare the annotation method as shown:

```java title=Example.java
public  @interface MyAnnotation {
    Class element1();  // Any Class type
    Class<Test> element2();  // Only  Test   class  type
    Class<? extends  Test>  element3(); // Test   or  its  subclass type
}
```

An annotation type cannot be generic.

- Next »
- « Previous
