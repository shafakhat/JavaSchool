---
title: Creates and uses a single-member annotation
nav: Creates and uses a single-...
description: Imported from the java2s.com archive: Creates and uses a single-member annotation
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Createsandusesasinglememberannotation.htm
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
  publicstaticvoid myMeth() {
    Single ob = new Single();
    try {
      Method m = ob.getClass().getMethod("myMeth");
      MySingle anno = m.getAnnotation(MySingle.class);
      System.out.println(anno.value()); // displays 100
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```
