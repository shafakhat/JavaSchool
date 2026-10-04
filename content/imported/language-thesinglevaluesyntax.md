---
title: The single-value syntax
nav: The single-value syntax
description: Using the single-value syntax when applying an annotation that has other members, if other members all have default values.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Thesinglevaluesyntax.htm
---
Using the single-value syntax when applying an annotation that has other members, if other members all have default values.

```java title=Example.java
@interface SomeAnno {
  int value();
  int xyz() default 0;
}
@SomeAnno(88)
java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  int value();
  int defaultValue() default 100;
}
@MyAnnotation(102)
public class MainClass {
  // Annotate a method.
  @MyAnnotation(101)
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
@MyAnnotation(defaultValue=100, value=101)
```
