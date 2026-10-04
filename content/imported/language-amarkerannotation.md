---
title: A marker annotation
nav: A marker annotation
description: Imported from the java2s.com archive: A marker annotation
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Amarkerannotation.htm
---
```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyMarker {
}
class Marker {
  @MyMarker
  publicstaticvoid myMeth() {
    Marker ob = new Marker();
    try {
      Method m = ob.getClass().getMethod("myMeth");
      if (m.isAnnotationPresent(MyMarker.class))
        System.out.println("MyMarker is present.");
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```
