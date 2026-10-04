---
title: Java Annotation create repeating annotations
nav: Java Annotation create rep...
description: To be a repeatable annotation, annotated with the @Repeatable annotation in java.lang.annotation.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20210102121619/http://www.java2s.com/ref/java/java-annotation-create-repeating-annotations.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

Java annotation can be repeated on the same element.

To be a repeatable annotation, annotated with the @Repeatable annotation in java.lang.annotation.

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Repeatable;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

// Make MyAnno repeatable
@Retention(RetentionPolicy.RUNTIME)
@Repeatable(MyRepeatedAnnos.class)
@interface MyAnno {
  String str() default"Testing";

  intval() default 999;
}

// This is the container annotation.
@Retention(RetentionPolicy.RUNTIME)
@interface MyRepeatedAnnos {
  MyAnno[] value();//www.java2s.com
}

publicclass Main {

  // Repeat MyAnno on myMethod().
  @MyAnno(str = "First annotation", val = -1)
  @MyAnno(str = "Second annotation", val = 100)
  publicstaticvoid myMethod(String str, int i) {
    Main ob = new Main();

    try {
      Class<?> c = ob.getClass();

      // Obtain the annotations for myMethod().Method m = c.getMethod("myMethod", String.class, int.class);

      // Display the repeated MyAnno annotations.Annotation anno = m.getAnnotation(MyRepeatedAnnos.class);
      System.out.println(anno);

      Annotation[] annos = m.getAnnotationsByType(MyAnno.class);
      for(Annotation a : annos)  {
        System.out.println(a);
      }
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }

  publicstaticvoid main(String args[]) {
    myMethod("test", 10);
  }
}
```

PreviousNext

## Related

- Java ThreadGroup catch uncaught exceptions in a group of threads
- Java ThreadLocal use local thread variables
- Java Annotation
- Java Annotation retention policy
- Java Annotation reflection at run time
