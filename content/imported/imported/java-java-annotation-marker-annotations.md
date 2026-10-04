---
title: Java Annotation marker annotations
nav: Java Annotation marker ann...
description: A marker annotation is a special kind of annotation with no members.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20210102121620/http://www.java2s.com/ref/java/java-annotation-marker-annotations.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

A marker annotation is a special kind of annotation with no members.

We use marker annotation to mark an item.

To find out if an annotation is a marker annotation, use the method isAnnotationPresent() defined by the AnnotatedElement interface.

The following code uses a marker annotation.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

// A marker annotation.
@Retention(RetentionPolicy.RUNTIME)
@interface MyMarker {
}

publicclass Main {

  // Annotate a method using a marker.// Notice that no () is needed.
  @MyMarker//www.java2s.compublicstaticvoid myMeth() {
    Main ob = new Main();

    try {
      Method m = ob.getClass().getMethod("myMeth");

      // Determine if the annotation is present.if (m.isAnnotationPresent(MyMarker.class))
        System.out.println("MyMarker is present.");

    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }

  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```

PreviousNext

## Related

- Java Annotation reflection at run time
- Java Annotation get all annotations
- Java Annotation default values
- Java Annotation with single member
- Java Annotation built-In annotations
