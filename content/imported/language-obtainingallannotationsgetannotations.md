---
title: Obtaining All Annotations
nav: Obtaining All Annotations
description: @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/ObtainingAllAnnotationsgetAnnotations.htm
---
```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
// A simple annotation type.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  String stringValue();
  int intValue();
}
@Retention(RetentionPolicy.RUNTIME)
@interface What {
  String description();
}
@What(description = "An annotation test class")
@MyAnnotation(stringValue = "for class", intValue = 100)
publicclass MainClass {
  // Annotate a method.
  @What(description = "An annotation test method")
  @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
  publicstaticvoid myMethod(String str, int i) {
  }
  publicstaticvoid main(String[] arg) {
    try {
      MainClass ob = new MainClass();
      Annotation[] annos = ob.getClass().getAnnotations();
      System.out.println("All annotations for Meta2:");
      for(Annotation a : annos)
        System.out.println(a);
    } catch (Exception exc) {
    }
  }
}
java title=Example.java
All annotations for Meta2:
@MyAnnotation(stringValue=for class, intValue=100)
@What(description=An annotation test class)
```
