---
title: Show all annotations for a class and a method.
nav: Show all annotations for a...
description: Imported from the java2s.com archive: Show all annotations for a class and a method.
section: Imported - java2s Archive
order: 2155
source: https://web.archive.org/web/20140829081814/http://www.java2s.com/Tutorial/Java/0125__Reflection/Showallannotationsforaclassandamethod.htm
---
```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  int val();
}
@Retention(RetentionPolicy.RUNTIME)
@interface What {
  String description();
}
@What(description = "An annotation test class")
@MyAnno(str = "Meta2", val = 99)
class Meta2 {
  @What(description = "An annotation test method")
  @MyAnno(str = "Testing", val = 100)
  public static void myMeth() {
    Meta2 ob = new Meta2();
    try {
      Annotation annos[] = ob.getClass().getAnnotations();
      System.out.println("All annotations for Meta2:");
      for (Annotation a : annos)
        System.out.println(a);
      Method m = ob.getClass().getMethod("myMeth");
      annos = m.getAnnotations();
      System.out.println("All annotations for myMeth:");
      for (Annotation a : annos)
        System.out.println(a);
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  public static void main(String args[]) {
    myMeth();
  }
}
```

| 7.8.1. | Use reflection to display the annotation associated with a method. |
|---|---|
| 7.8.2. | Show all annotations for a class and a method. |
| 7.8.3. | Get annotation by Annotation class |
| 7.8.4. | Get annotation by type |
