---
title: Marker Annotations
nav: Marker Annotations
description: Imported from the java2s.com archive: Marker Annotations
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/MarkerAnnotations.htm
---
- Marker Annotations are used to mark a declaration.
- A marker annotation is a special kind of annotation.
- A marker annotation contains no members.
- Using isAnnotationPresent( ) to determine if the marker is present.

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
}
@MyAnnotation
publicclass MainClass {
  // Annotate a method.
  @MyAnnotation()
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
java title=Example.java
All annotations for myMeth:
@MyAnnotation()
```
