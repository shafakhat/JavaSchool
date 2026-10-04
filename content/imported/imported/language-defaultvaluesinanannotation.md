---
title: default values in an annotation.
nav: default values in an annot...
description: Imported from the java2s.com archive: default values in an annotation.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/defaultvaluesinanannotation.htm
---
```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str() default"Testing";

  int val() default 9000;
}

class Meta3 {
  @MyAnno()
  publicstaticvoid myMeth() {
    Meta3 ob = new Meta3();

    try {
      Class c = ob.getClass();

      Method m = c.getMethod("myMeth");

      MyAnno anno = m.getAnnotation(MyAnno.class);

      System.out.println(anno.str() + " " + anno.val());
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }

  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```
