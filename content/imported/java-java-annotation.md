---
title: Java Annotation
nav: Java Annotation
description: Imported from the java2s.com archive: Java Annotation
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20210102121619/http://www.java2s.com/ref/java/java-annotation.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

Java annotation is created via the interface.

The following code creates an annotation called MyAnno:

```java title=Example.java
// A simple annotation type.
@interface MyAnno {
  String str();
  intval();
}
```

When applying an annotation, assign values to its members.

The following code applied MyAnno to a method declaration:

```java title=Example.java
// Annotate a method.
@MyAnno(str = "Annotation Example", val = 100)
publicstaticvoid myMethod() {
```

PreviousNext

## Related

- Java ThreadGroup group threads into a group
- Java ThreadGroup catch uncaught exceptions in a group of threads
- Java ThreadLocal use local thread variables
- Java Annotation create repeating annotations
- Java Annotation retention policy
