---
title: Using Default Values
nav: Using Default Values
description: This declaration gives a default value of "Testing" to str and 9000 to val.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/UsingDefaultValues.htm
---
- Annotation default values is used if no value is specified.
- A default value is specified by adding a default clause.
- Default value must be of a type compatible with type.

Here is @MyAnnotation rewritten to include default values:

```java title=Example.java
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  String stringValue() default "defaultString";
  int intValue() default 101;
}
```

This declaration gives a default value of "Testing" to str and 9000 to val.

This means that neither value needs to be specified when @MyAnno is used.

However, either or both can be given values if desired.

Therefore, following are the four ways that @MyAnnotation can be used:

```java title=Example.java
@MyAnnotation()                           // both str and val default
@MyAnnotation(stringValue = "some string")        // val defaults
@MyAnnotation(intValue = 100)                  // str defaults
@MyAnnotation(stringValue = "Testing", intValue = 100) // no defaults
java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
// A simple annotation type.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  String stringValue() default "defaultString";
  int intValue() default 101;
}
@MyAnnotation(stringValue = "for class", intValue = 100)
public class MainClass {
  // Annotate a method.
  @MyAnnotation(intValue = 100)
  public static void myMethod() {
  }
  public static void main(String[] arg) {
    try {
      MainClass ob = new MainClass();
      Method m = ob.getClass( ).getMethod("myMethod");
      Annotation[] annos = m.getAnnotations();
      System.out.println("All annotations for myMeth:");
      for(Annotation a : annos)
      System.out.println(a);
    } catch (Exception exc) {
    }
  }
}
java title=Example.java
All annotations for myMeth:
@MyAnnotation(intValue=100, stringValue=defaultString)
```
