---
title: Single-Member Annotations
nav: Single-Member Annotations
description: Imported from the java2s.com archive: Single-Member Annotations
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20070523085351/http://www.java2s.com:80/Tutorial/Java/0020__Language/SingleMemberAnnotations.htm
---
- Single-Member Annotations contains only one member.
- Single-Member Annotations allow a shorthand form of specifying the value.
- The name of the member must be value.

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  int value();
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
```

```java title=Example.java
All annotations for myMeth:
@MyAnnotation(value=101)
```
