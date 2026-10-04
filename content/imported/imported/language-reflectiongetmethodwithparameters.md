---
title: Reflection
nav: Reflection
description: @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/ReflectiongetMethodwithparameters.htm
---
```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

// A simple annotation type.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
  String stringValue();

  int intValue();
}

publicclass MainClass {
  // Annotate a method.
  @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
  publicstaticvoid myMethod(String str, int i) {
  }

  publicstaticvoid main(String[] a) {
    try {
      MainClass ob = new MainClass();
      Class c = ob.getClass();

      Method m = c.getMethod("myMethod", String.class, int.class);

      MyAnnotation anno = m.getAnnotation(MyAnnotation.class);

      System.out.println(anno.stringValue() + " " + anno.intValue());
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }

  }
}
```

```java title=Example.java
Annotation Example 100
```
