---
title: Java Object Oriented Design - Java Annotation Type
nav: Java Object Oriented Desig...
description: A marker annotation type is an annotation type with no elements, not even one with a default value.
section: Imported - java2s Archive
order: 50195
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0740__Java_Annotation_Type.html
---
```java title=Example.java
```

## Marker Annotation Types

A marker annotation type is an annotation type with no elements, not even one with a default value.

A marker annotation is used by the annotation processing tools.

```java title=Example.java
public  @interface Marker  {
}
@Marker
publicclass Main{
}
```

## Meta-Annotation Types

Meta-annotations types are annotation types, which are used to annotate other annotation types.

Meta-annotation types are part of the Java class library. They are declared in the package java.lang.annotation.

The following annotation types are meta-annotation types:

- Target
- Retention
- Inherited
- Documented
- Repeatable
- Native

## Target Annotation Type

Target annotation type annotates an annotation type to set the context to use the annotation type.

It has only one element named value. Its value element is an array of java.lang.annotation.ElementType enum type.

The following table lists all constants in the ElementType enum.

Constant Name  Description
---  ---
ANNOTATION_TYPE  annotate another annotation type declaration. This makes the annotation type a meta-annotation.
CONSTRUCTOR  annotate constructors.
FIELD  annotate fields and enum constants.
LOCAL_VARIABLE  annotate local variables.
METHOD  annotate methods.
PACKAGE  annotate package declarations.
PARAMETER  annotate parameters.
TYPE  annotate class, interface (including annotation type), or enum declarations.
TYPE_PARAMETER  annotate type parameters in generic classes, interfaces, methods, etc.
TYPE_USE  annotate all uses of types.

The following Version annotation type has Target meta-annotation, which specifies that the Version annotation type can be used with program elements of only three types: any type (class, interface, enum, and annotation types), a constructors, and methods.

```java title=Example.java
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;
@Target({ ElementType.TYPE, ElementType.CONSTRUCTOR, ElementType.METHOD })
public @interface Version {
  int major();
  int minor();
}
```

The Version annotation cannot be used on any program elements other than the three types specified in its Target annotation.

```java title=Example.java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;
@Target({ ElementType.TYPE_USE })
@interface MyAnno {
}
@Target({ ElementType.TYPE_USE })
@interface MyAnno2 {
}
publicclass Main {
  publicvoid processData() throws @MyAnno Exception {
    int roundedValue = (@MyAnno2 int) .02;
    Main t = new @MyAnno Main();
  }
}
```

If we do not annotate an annotation type with the Target annotation type, the annotation type can be used as a modifier for any declaration, except a type parameter declaration.

## The Retention Annotation

Retention Annotation sets the retention policy of an annotation type.

An annotation can be retained at three levels.

- Source code only
- Class file only. The default behaviour.
- Class file and the runtime

The Retention meta-annotation type specifies how an annotation should be retained by Java.

If an annotation type has a "source code only" retention policy, its instances are removed when compiled into a class file.

If the retention policy is "class file only", its instances are retained in the class file, but they cannot be read at runtime.

If the retention policy is "class file and runtime", the annotation instances are retained in the class file and they are available for reading at runtime.

The Retention meta-annotation type declares one element, named value, which is of the java.lang. annotation.RetentionPolicy enum type.

The RetentionPolicy enum has three constants, SOURCE, CLASS, and RUNTIME, which are used to specify the retention policy of source only, class only, and class-and-runtime, respectively.

The following code uses the Retention meta-annotation on the Version annotation type. It specifies that the Version annotations should be available at runtime.

```java title=Example.java
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
@Target({ ElementType.TYPE, ElementType.CONSTRUCTOR, ElementType.METHOD })
@Retention(RetentionPolicy.RUNTIME)
@interface Version {
  int major();
  int minor();
}
```

If we do not use the Retention meta-annotation on an annotation type, its retention policy defaults to class file only. And we will not be able to read those annotations at runtime.

An annotation on a local variable declaration is never available in the class file or at runtime irrespective of the retention policy of the annotation type.

## Inherited Annotation Type

Inherited annotation type is a marker meta-annotation type.

If an annotation type is annotated with an Inherited meta-annotation, its instances are inherited by a subclass declaration.

It has no effect if an annotation type is used to annotate any elements other than a class declaration.

The following code shows the effect of @Inherited meta-annotation type.

```java title=Example.java
import java.lang.annotation.Inherited;
@interface Ann2 {
  int id();
}
@Inherited
@interface Ann3 {
  int id();
}
@Ann2(id = 1)
@Ann3(id = 2)
class A {
}
// Class B inherits Ann3(id=2) annotation from the class A
class B extends A {
}
```

## Documented Annotation

Documented annotation type is a marker meta-annotation type.

If an annotation type is annotated with a Documented annotation, the Javadoc tool will generate documentation for all of its instances.

```java title=Example.java
import java.lang.annotation.Documented;
@Documented
@interface Version {
  int major();
  int minor();
}
@Version(major = 1, minor = 0)
publicclass Main {
}
```

When generating documentation for the Main class with the Javadoc tool, the Version annotation on the Main class declaration is also generated as part of the documentation.

## Repeatable Annotation

Java 8 added a Repeatable meta-annotation type.

An annotation type declaration must be annotated with a @Repeatable annotation if we would use it repeatly on one single code element.

The Repeatable annotation type has only one element named value whose type is a class type of another annotation type.

```java title=Example.java
import java.lang.annotation.Repeatable;
@interface LogHistory {
  Log[] value();
}
@Repeatable(LogHistory.class)
@interface Log {
  String date();
  String comments();
}
@Log(date = "01/01/2014", comments = "B")
@Log(date = "01/21/2014", comments = "A")
publicclass Main {
  publicstaticvoid process() {
  }
}
```

## The Native Annotation

The Native annotation type is a meta-annotation that is used to annotate fields which may be referenced from native code. It is a marker annotation.

- « Previous
