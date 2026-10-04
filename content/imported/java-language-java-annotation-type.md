---
title: Java Tutorial - Java Annotation Type
nav: Java Tutorial - Java Annot...
description: A marker annotation contains no members. It is used to mark a declaration.
section: Imported - java2s Archive
order: 50455
source: https://www.java2s.com/Tutorials/Java/Java_Language/7010__Java_Annotation_Type.html
---
```java title=Example.java
```

## Java Marker annotation

A marker annotation contains no members. It is used to mark a declaration.

To determine if a marker annotation is present, use the method isAnnotationPresent( ). isAnnotationPresent( ) is a defined by the AnnotatedElement interface.

Here is an example that uses a marker annotation.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyMarker {
}
publicclass Main {
  @MyMarker
  publicstaticvoid myMethod() throws Exception{
    Main ob = new Main();
      Method m = ob.getClass().getMethod("myMethod");
      if (m.isAnnotationPresent(MyMarker.class)){
        System.out.println("MyMarker is present.");
      }
  }
  publicstaticvoid main(String args[]) throws Exception{
    myMethod();
  }
}
```

The code above generates the following result.

## Java Single-Member Annotations

A single-member annotation contains only one member. It allows a shorthand form of specifying the value of the member.

When only one member is present, you don't need to specify the name of the member.

In order to use this shorthand, the name of the member must be value. Here is an example that creates and uses a single-member annotation:

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MySingle {
  int value(); // this variable name must be value
}
publicclass Main {
  @MySingle(100)
  publicstaticvoid myMeth() {
    Main ob = new Main ();
    try {
      Method m = ob.getClass().getMethod("myMeth");
      MySingle anno = m.getAnnotation(MySingle.class);
      System.out.println(anno.value()); // displays 100
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

## Example

You can use the single-value syntax when applying an annotation that has other members, but those other members must all have default values.

For example, here the value xyz is added, with a default value of zero:

```java title=Example.java
@interface SomeAnno {
    int value();
    int xyz() default 0;
}
```

You can apply @SomeAnno as ,

```java title=Example.java
@SomeAnno(1)
```

by specifying the value using the single-member syntax.

In this case, xyz defaults to zero, and value gets the value 1.

- « Previous
