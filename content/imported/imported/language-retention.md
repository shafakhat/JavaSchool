---
title: Retention
nav: Retention
description: Imported from the java2s.com archive: Retention
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Retention.htm
---
- @Retention indicates how long annotations whose annotated types are annotated @Retention are to be retained.
- The value of @Retention can be one of the members of the java.lang.annotation.RetentionPolicy enum:

- SOURCE. Annotations are to be discarded by the Java compiler.
- CLASS. Annotations are to be recorded in the class file but not be retained by the JVM. This is the default value.
- RUNTIME. Annotations are to be retained by the JVM so you can query them using reflection.

```java title=Example.java
@Retention(value=SOURCE)
public @interface SuppressWarnings
```
