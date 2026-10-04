---
title: The Annotation Interface
nav: The Annotation Interface
description: In addition, any implementation of Annotation will override the equals, hashCode, and
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/TheAnnotationInterface.htm
---
- An annotation type is a Java interface.
- All annotation types are subinterfaces of the java.lang.annotation.Annotation interface.
- It has one method, annotation Type, that returns an java.lang.Class object.

```java title=Example.java
java.lang.Class<? extends Annotation> annotationType()
```

```java title=Example.java
In addition, any implementation of Annotation will override the equals, hashCode, and
toString methods from the java.lang.Object class.
```
