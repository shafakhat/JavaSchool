---
title: Java Annotation with single member
nav: Java Annotation with singl...
description: When only one member is present, we don't need to specify its name.
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20210102121620/http://www.java2s.com/ref/java/java-annotation-with-single-member.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

A single-member annotation contains only one member.

It allows a shorthand form of setting the member value.

When only one member is present, we don't need to specify its name.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
// A single-member annotation.
@Retention(RetentionPolicy.RUNTIME)
@interface MySingle {
  int value(); // this variable name must be value
}
publicclass Main {
  // Annotate a method using a marker.
  @MySingle(100)publicstaticvoid myMeth() {
    Main ob = new Main();
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

PreviousNext

## Related

- Java Annotation get all annotations
- Java Annotation default values
- Java Annotation marker annotations
- Java Annotation built-In annotations
- Java annotation @SafeVarargs
