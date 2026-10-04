---
title: Java Annotation reflection at run time
nav: Java Annotation reflection...
description: Here is a program uses reflection to display the annotation associated with a method:
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20210102121619/http://www.java2s.com/ref/java/java-annotation-reflection-at-run-time.html
---
- java.lang.annotation
- java.lang.annotation Annotation

## Introduction

Here is a program uses reflection to display the annotation associated with a method:

The code uses reflection to get and display the values of str and val in the MyAnno annotation associated with myMeth().

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
// An annotation type declaration.
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();intval();
}
publicclass Main {
  // Annotate a method.
  @MyAnno(str = "Annotation Example", val = 100)
  publicstaticvoid myMethod() {
    Main ob = new Main();
    // Obtain the annotation for this method// and display the values of the members.try {
      // First, get a Class object that represents// this class.Class<?> c = ob.getClass();
      // Now, get a Method object that represents// this method.Method m = c.getMethod("myMethod");
      // Next, get the annotation for this class.
      MyAnno anno = m.getAnnotation(MyAnno.class);
      System.out.println(anno.str() + " " + anno.val());
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }
  publicstaticvoid main(String args[]) {
    myMethod();
  }
}
```

PreviousNext

## Related

- Java Annotation
- Java Annotation create repeating annotations
- Java Annotation retention policy
- Java Annotation get all annotations
- Java Annotation default values
