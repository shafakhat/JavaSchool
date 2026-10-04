---
title: Java Annotation retention policy
nav: Java Annotation retention ...
description: They are captured in the java.lang.annotation.RetentionPolicy enumeration.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20210102121619/http://www.java2s.com/ref/java/java-annotation-retention-policy.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

A retention policy determines when to keep the annotation.

Java defines three policies:

- SOURCE - retained only in the source file, discarded during compilation
- CLASS - stored in the .class file during compilation, not available during run time
- RUNTIME - stored in the .class file during compilation and available during run time

They are captured in the java.lang.annotation.RetentionPolicy enumeration.

An annotation on a local variable declaration is not retained in the .class file.

A retention policy is set for an annotation by Java's built-in annotations: @Retention.

The general form is shown here:

```java title=Example.java
@Retention(retention-policy)
```

Here, retention-policy must be one of the discussed enumeration constants.

If no retention policy is specified for an annotation, the default policy of CLASS is used.

The following version of MyAnno uses @Retention to specify the RUNTIME retention policy.

Thus, MyAnno will be available during the program execution.

```java title=Example.java
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  intval();
}
```

PreviousNext

## Related

- Java ThreadLocal use local thread variables
- Java Annotation
- Java Annotation create repeating annotations
- Java Annotation reflection at run time
- Java Annotation get all annotations
