---
title: Java Tutorial - What are Java built-in annotations
nav: Java Tutorial - What are J...
description: Java defines many built-in annotations. Most are specialized, but seven are general purpose.
section: Imported - java2s Archive
order: 50456
source: https://www.java2s.com/Tutorials/Java/Java_Language/7030__Java_Buildin_annotations.html
---
## Built-In Annotations

Java defines many built-in annotations. Most are specialized, but seven are general purpose.

- @Retention
- @Documented
- @Target
- @Inherited
- @Override
- @Deprecated
- @SuppressWarnings

## @Retention

@Retention is designed to be used only as an annotation to another annotation. It specifies the retention policy.

## @Documented

The @Documented annotation is a marker interface that tells a tool that an annotation is to be documented.

## @Target

The @Target annotation specifies the types of declarations to which an annotation can be applied.

It is designed to be used only as an annotation to another annotation. @Target takes one argument, which must be a constant from the ElementType enumeration.

Target constant annotation can be applied to

- ANNOTATION_TYPE Another annotation
- CONSTRUCTOR Constructor
- FIELD Field
- LOCAL_VARIABLE Local variable
- METHOD Method
- PACKAGE Package
- PARAMETER Parameter
- TYPE Class, interface, or enumeration

You can specify one or more of these values in a @Target annotation. To specify multiple values, you must specify them within a braces-delimited list. For example:

```java title=Example.java
@Target( { ElementType.FIELD, ElementType.LOCAL_VARIABLE } )
```

## @Inherited

@Inherited is a marker annotation that can be used only on another annotation declaration. It affects only annotations that will be used on class declarations. @Inherited causes the annotation for a superclass to be inherited by a subclass.

## @Override

@Override is a marker annotation that can be used only on methods. A method annotated with @Override must override a method from a superclass.

## @Deprecated

@Deprecated is a marker annotation. It indicates that a declaration is obsolete and has been replaced by a newer form.

## @SuppressWarnings

@SuppressWarnings specifies that one or more warnings that might be issued by the compiler are to be suppressed. The warnings to suppress are specified by name, in string form. This annotation can be applied to any type of declaration.

- « Previous
