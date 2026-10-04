---
title: Java Annotation default values
nav: Java Annotation default va...
description: The default value is used when no value is set when using the annotation.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-annotation-default-values.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

We can set annotation members with default values.

The default value is used when no value is set when using the annotation.

A default value is set by adding a default clause to a member's declaration.

It has this general form:

```java title=Example.java
type member() default value ;
```

Here, value must be of a type compatible with type.

Here is @MyAnno rewritten to include default values:

```java title=Example.java
// An annotation type declaration that includes defaults.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str() default "DefaultStringValue";
  int val() default 99999;
}
```

The following are the four ways that we can use @MyAnno:

```java title=Example.java
@MyAnno() // both str and val default
@MyAnno(str = "some string") // val defaults
@MyAnno(val = 100) // str defaults
@MyAnno(str = "Testing", val = 100) // no defaults
```

The following code demonstrates the use of default values in an annotation.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
// An annotation type declaration that includes defaults.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str() default "Testing";
  int val() default 9000;
}
public class Main {
  // Annotate a method using the default values.
  @MyAnno()public static void myMethod() {
    Main ob = new Main();
    // Obtain the annotation for this method // and display the values of the members. try {
      Class<?> c = ob.getClass();
      Method m = c.getMethod("myMethod");
      MyAnno anno = m.getAnnotation(MyAnno.class);
      System.out.println(anno.str() + " " + anno.val());
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  public static void main(String args[]) {
    myMethod();
  }
}
```

PreviousNext

## Related

- Java Annotation retention policy
- Java Annotation reflection at run time
- Java Annotation get all annotations
- Java Annotation marker annotations
- Java Annotation with single member
