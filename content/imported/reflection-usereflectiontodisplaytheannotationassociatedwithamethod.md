---
title: Use reflection to display the annotation associated with a method.
nav: Use reflection to display ...
description: Imported from the java2s.com archive: Use reflection to display the annotation associated with a method.
section: Imported - java2s Archive
order: 2171
source: https://web.archive.org/web/20140829082403/http://www.java2s.com/Tutorial/Java/0125__Reflection/Usereflectiontodisplaytheannotationassociatedwithamethod.htm
---
```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();
  int val();
}
class Meta {
  @MyAnno(str = "Annotation Example", val = 100)
  public static void myMeth() {
    Meta ob = new Meta();
    try {
      Class c = ob.getClass();
      Method m = c.getMethod("myMeth");
      MyAnno anno = m.getAnnotation(MyAnno.class);
      System.out.println(anno.str() + " " + anno.val());
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
