---
title: Annotations and Annotation Types
nav: Annotations and Annotation...
description: Annotations are notes in Java programs to instruct the Java compiler to do something. Java provides three standard annotations and four standard meta-annotations.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/AnnotationsandAnnotationTypes.htm
---
Annotations are notes in Java programs to instruct the Java compiler to do something. Java provides three standard annotations and four standard meta-annotations.

- An annotation type is a special interface type.
- An annotation is an instance of an annotation type.
- An annotation type has a name and members.
- The information contained in an annotation takes the form of key/value pairs.
- There can be zero or multiple pairs and each key has a specific type.
- It can be a String, int, or other Java types.
- Annotation types with no key/value pairs are called marker annotation types.
- Those with one key/value pair are referred to single-value annotation types.

- There are three annotation types in Java 5: Deprecated, Override, and Suppress Warnings.
- There are four other annotation types that are part of the java.lang.annotation package: Documented, Inherited, Retention, and Target.
- These four annotation types are used to annotate annotations,
