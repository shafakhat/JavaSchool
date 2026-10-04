---
title: Java annotation @SafeVarargs
nav: Java annotation @SafeVarargs
description: The @SafeVarargs annotation can designate certain methods and constructors that use a variable number of arguments as safe.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20210102121620/http://www.java2s.com/ref/java/java-annotation-safevarargs.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

The @SafeVarargs annotation can designate certain methods and constructors that use a variable number of arguments as safe.

Methods can be passed with a variable number of arguments.

These arguments may be generics.

It may be desirable to suppress harmless warnings using the @SafeVarargs annotation.

```java title=Example.java
import java.util.ArrayList;
publicclass Main {
  publicstaticvoid main(String[] args) {
    ArrayList<Integer> a1 = newArrayList<>();
    a1.add(1);
    a1.add(2);
    ArrayList<Float> a2 = newArrayList<>();
    a2.add(3.0F);
    a2.add(4.0F);
    displayElements(a1, a2, 12);
  }
  @SafeVarargspublicstatic <T> void displayElements(T... array) {
    for (T element : array) {
      System.out.println(element.getClass().getName() + ": " + element);
    }
  }
}
```

PreviousNext

## Related

- Java Annotation marker annotations
- Java Annotation with single member
- Java Annotation built-In annotations
- Java Annotation @Deprecated
- Java RuntimeMXBean class
