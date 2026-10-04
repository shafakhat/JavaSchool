---
title: Get annotation by Annotation class
nav: Get annotation by Annotati...
description: Imported from the java2s.com archive: Get annotation by Annotation class
section: Imported - java2s Archive
order: 2156
source: https://web.archive.org/web/20140829083154/http://www.java2s.com/Tutorial/Java/0125__Reflection/GetannotationbyAnnotationclass.htm
---
```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MySingle {
  int value(); // this variable name must be value
}
class Single {
  @MySingle(100)
  public static void myMeth() {
    Single ob = new Single();
    try {
      Method m = ob.getClass().getMethod("myMeth");
      MySingle anno = m.getAnnotation(MySingle.class);
      System.out.println(anno.value()); // displays 100
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
