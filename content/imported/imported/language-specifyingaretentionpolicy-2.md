---
title: Specifying a Retention Policy
nav: Specifying a Retention Pol...
description: A retention policy determines at what point an annotation is discarded.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/SpecifyingaRetentionPolicy.htm
---
A retention policy determines at what point an annotation is discarded.

- SOURCE: annotation retained only in the source file and is discarded during compilation.
- CLASS: annotation stored in the .class file during compilation, not available in the run time.
- RUNTIME: annotation stored in the .class file and available in the run time.
- They are defined java.lang.annotation.RetentionPolicy enumeration.

A retention policy is specified using Java's built-in annotations: @Retention.

```java title=Example.java
@Retention(retention-policy)
```

the default policy is CLASS.

MyAnnotation uses @Retention to specify the RUNTIME retention policy.

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// A simple annotation type.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  String stringValue();

  int intValue();
}

publicclass MainClass {
  // Annotate a method.
  @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
  publicstaticvoid myMethod() {
  }

}
```
