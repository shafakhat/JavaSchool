---
title: Java Object Oriented Design - Java Annotation Default Value
nav: Java Object Oriented Desig...
description: We can define a default value for elements in an annotation. We are not required to provide a value for an annotation element with a default value.
section: Imported - java2s Archive
order: 50193
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0720__Java_Annotation_Default_Value.html
---
```java title=Example.java
```

We can define a default value for elements in an annotation. We are not required to provide a value for an annotation element with a default value.

The default value can be defined using the following general syntax:

```java title=Example.java
<modifiers> @interface <annotation type name> {
    <data-type> <element-name>() default <default-value>;
}
```

The keyword default specifies the default value.

The default value must be of the type compatible to the data type for the element.

The following code creates the Version annotation type by specifying a default value for its minor element as zero, as shown:

```java title=Example.java
public  @interface  Version {
    int major();
    int minor() default 0; // zero asdefault value for minor
}
```

## Example

The following code shows how to use annotation with use the default value.

```java title=Example.java
@Version(major=1) // minor is zero, which  is its  default value
@Version(major=2, minor=1)  // minor  is 1, which  is the   specified  value
```

The following code shows how to specify default values for an array and other data types:

```java title=Example.java
public @interface Version {
  double d() default 1.89;
int num() default 1;
  int[] x() default { 1, 2 };
  String s() default"Hello";
  String[] s2() default { "abc", "xyz" };
  Class c() default Exception.class;
  Class[] c2() default { Exception.class, java.io.IOException.class };
}
```

- « Previous
