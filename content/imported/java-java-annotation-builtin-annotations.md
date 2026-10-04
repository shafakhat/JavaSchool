---
title: Java Annotation built-In annotations
nav: Java Annotation built-In a...
description: @Documented annotation tells that an annotation is to be documented.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20210102121620/http://www.java2s.com/ref/java/java-annotation-builtin-annotations.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

Java defines has built-in annotations.

We will take a look of the following built-in annotations.

- @Retention
- @Documented
- @Target
- @Inherited
- @Override
- @Deprecated
- @FunctionalInterface
- @SafeVarargs
- @SuppressWarnings

## @Retention

@Retention is used to annotate another annotation.

It specifies the retention policy.

## @Documented

@Documented annotation tells that an annotation is to be documented.

It is used only as an annotation to an annotation declaration.

## @Target

@Target annotation specifies the types of items that an annotation can be applied.

It is used as an annotation to another annotation.

The target constants are shown here:

Target Constant  Annotation Can Be Applied To
---  ---
ANNOTATION_TYPE  Another annotation
CONSTRUCTOR  Constructor
FIELD  Field
LOCAL_VARIABLE  Local variable
METHOD  Method
PACKAGE  Package
PARAMETER  Parameter
TYPE  Class, interface, or enumeration
TYPE_PARAMETER  Type parameter
TYPE_USE  Type use

We can specify one or more of these values in a @Target annotation.

To specify multiple values, specify them within a braces-delimited list.

```java title=Example.java
@Target( { ElementType.FIELD, ElementType.LOCAL_VARIABLE } )
```

## @Inherited

@Inherited is a marker annotation used only on another annotation declaration.

@Inherited causes the annotation for a superclass to be inherited by a subclass.

## @Override

@Override is a marker annotation for on methods.

A method with @Override must override a method from a superclass.

## @Deprecated

@Deprecated is a marker annotation that indicates that a declaration is obsolete and has been replaced by a newer form.

## @FunctionalInterface

@FunctionalInterface is a marker annotation for interfaces.

It marks that the annotated interface is a functional interface.

## @SafeVarargs

@SafeVarargs is a marker annotation for methods and constructors.

It indicates that no unsafe actions related to a varargs parameter occur.

## @SuppressWarnings

@SuppressWarnings can suppress warnings by compiler.

PreviousNext

## Related

- Java Annotation default values
- Java Annotation marker annotations
- Java Annotation with single member
- Java annotation @SafeVarargs
- Java Annotation @Deprecated
