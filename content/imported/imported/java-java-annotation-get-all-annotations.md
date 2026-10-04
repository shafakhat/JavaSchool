---
title: Java Annotation get all annotations
nav: Java Annotation get all an...
description: To get all annotations with RUNTIME retention, call getAnnotations() on that item.
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20210102121619/http://www.java2s.com/ref/java/java-annotation-get-all-annotations.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

To get all annotations with RUNTIME retention, call getAnnotations() on that item.

It has this general form:

```java title=Example.java
Annotation[ ] getAnnotations()
```

It returns an array of the annotations.

getAnnotations() can be called on objects of type Class, Method, Constructor, and Field.

The following code shows how to obtain all annotations associated with a class and with a method.

It declares two annotations. It then uses those annotations to annotate a class and a method.

```java title=Example.java
// Show all annotations for a class and a method. import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();/*fromwww.java2s.com*/intval();
}

@Retention(RetentionPolicy.RUNTIME)
@interface What {
  String description();
}

@What(description = "An annotation test class")
@MyAnno(str = "Meta2", val = 99)
publicclass Main {

  @What(description = "An annotation test method")
  @MyAnno(str = "Testing", val = 100)
  publicstaticvoid myMethod() {
    Main ob = new Main();

    try {
      Annotation annos[] = ob.getClass().getAnnotations();
      // Display all annotations for Meta2.System.out.println("All annotations for Meta2:");
      for (Annotation a : annos)
        System.out.println(a);

      System.out.println();

      // Display all annotations for myMethod.Method m = ob.getClass().getMethod("myMethod");
      annos = m.getAnnotations();

      System.out.println("All annotations for myMethod:");
      for (Annotation a : annos)
        System.out.println(a);

    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }

  publicstaticvoid main(String args[]) {
    myMethod();
  }
}
```

PreviousNext

## Related

- Java Annotation create repeating annotations
- Java Annotation retention policy
- Java Annotation reflection at run time
- Java Annotation default values
- Java Annotation marker annotations
