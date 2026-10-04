---
title: Java Tutorial - Java Annotations
nav: Java Tutorial - Java Annot...
description: Annotations embeds supplemental information into a source file. An annotation does not change the semantics of a program.
section: Imported - java2s Archive
order: 50454
source: https://www.java2s.com/Tutorials/Java/Java_Language/7000__Java_Annotation.html
---
```java title=Example.java
```

Annotations embeds supplemental information into a source file. An annotation does not change the semantics of a program.

An annotation is created through a mechanism based on the interface.

The following code declares an annotation called MyAnno:

```java title=Example.java
// A simple annotation type.
@interface MyAnno {
  String str();
  int val();
}
```

@ precedes the keyword interface. All annotations have method declarations only. An annotation cannot include an extends clause.

## Note

All annotation types automatically extend the Annotation interface. Annotation interface is a super-interface of all annotations. Annotation interface is declared within the java.lang.annotation package.

Any type of declaration can have an annotation associated with it. For example, classes, methods, fields, parameters, and enum constants can be annotated. An annotation can be annotated as well. In all cases, the annotation precedes the rest of the declaration.

When you apply an annotation, you give values to its members. For example, here is an example of MyAnno being applied to a class:

```java title=Example.java
// Annotate a method.
@MyAnno(str = "Annotation Example", val = 100)
publicclass Main{}
```

This annotation is linked with the class Main.

## Java Annotation retention policy

A retention policy determines at what point an annotation is discarded.

Java defines three such policies:SOURCE, CLASS, and RUNTIME.

- SOURCE is retained only in the source file and is discarded during compilation.
- CLASS is stored in the .class file during compilation. It is not available through the JVM during run time.
- RUNTIME is stored in the .class file and is available through the JVM during run time.

A retention policy is specified for an annotation by using one of Java's built-in annotations:

```java title=Example.java

@Retention
```

Its general form is shown here:

```java title=Example.java

@Retention(retention-policy)
```

retention-policy must be one of SOURCE, CLASS, and RUNTIME.

The default policy is CLASS.

The following code specifies the Retention Policy to RUNTIME.

```java title=Example.java

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  int val();
}
```

How to obtaining Annotations at Run Time by Use of Reflection.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
/*www.java2s.com*/// An annotation type declaration.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  int val();
}
publicclass Main {
  @MyAnno(str = "Annotation Example", val = 100)
  publicstaticvoid myMeth() {
    Main ob = new Main();
    try {
      Class c = ob.getClass();
      Method m = c.getMethod("myMeth");
      MyAnno anno = m.getAnnotation(MyAnno.class);
      System.out.println(anno.str() + " " + anno.val());
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```

The code above generates the following result.

## Java Annotation reflection

You can obtain all annotations that have RUNTIME retention that are associated with an item by calling getAnnotations( ) on that item.

It has this general form:

```java title=Example.java

Annotation[ ] getAnnotations( )
```

The following code shows how to get annotations from a class.

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
/*www.java2s.com*/
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  int val();
}
@Retention(RetentionPolicy.RUNTIME)
@interface What {
  String description();
}
@What(description = "An annotation")
@MyAnno(str = "Meta2", val = 99)
publicclass Main {
  @What(description = "test method")
  @MyAnno(str = "Testing", val = 100)
  publicstaticvoid myMeth() throws Exception {
    Main ob = new Main();
    Annotation annos[] = ob.getClass().getAnnotations();
    System.out.println("All annotations for Meta2:");
    for (Annotation a : annos) {
      System.out.println(a);
    }
    Method m = ob.getClass().getMethod("myMeth");
    annos = m.getAnnotations();
    for (Annotation a : annos) {
      System.out.println(a);
    }
  }
  publicstaticvoid main(String args[]) throws Exception {
    myMeth();
  }
}
```

The code above generates the following result.

## Java Annotation Default Values

You can give annotation members default values. Those default value are used if no value is specified when the annotation is applied.

A default value is specified by adding a default clause to a member's declaration.

It has this general form:

```java title=Example.java

type member( ) default value;
```

Here is @MyAnno rewritten to include default values:

```java title=Example.java

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str() default"Testing";
  int val() default 9000;
}
```

Either or both can be given values if desired. Therefore, following are the four ways that @MyAnno can be used:

```java title=Example.java

@MyAnno() // both str and val default
@MyAnno(str = "string") // val defaults
@MyAnno(val = 100) // str defaults
@MyAnno(str = "Testing", val = 100) // no defaults
```

The following program demonstrates the use of default values in an annotation.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
/*fromwww.java2s.com*/
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str() default"Testing";
  int val() default 1;
}
publicclass Main {
  @MyAnno()
  publicstaticvoid myMeth() throws Exception{
    Main ob = new Main();
      Class c = ob.getClass();
      Method m = c.getMethod("myMeth");
      MyAnno anno = m.getAnnotation(MyAnno.class);
      System.out.println(anno.str() + " " + anno.val());
  }
  publicstaticvoid main(String args[]) throws Exception{
    myMeth();
  }
}
```

The code above generates the following result.

- « Previous
