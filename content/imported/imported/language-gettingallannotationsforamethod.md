---
title: Getting all annotations for a method
nav: Getting all annotations fo...
description: @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Gettingallannotationsforamethod.htm
---
```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

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
  publicstaticvoid myMethod() {
  }

  publicstaticvoid main(String[] arg) {
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
```

```java title=Example.java
All annotations for myMeth:
@What(description=An annotation test method)
@MyAnnotation(stringValue=Annotation Example, intValue=100)
```
