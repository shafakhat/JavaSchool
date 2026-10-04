---
title: How to get all annotations by using Java reflection
nav: How to get all annotations...
description: You can obtain all annotations that have RUNTIME retention that are associated with an item by calling getAnnotations( ) on that item.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20141115062943/http://www.java2s.com:80/Tutorials/Java/Annotations/How_to_get_all_annotations_by_using_Java_reflection.htm
---
In this chapter you will learn:

- How to get all annotations
- Syntax for Java Annotation reflection
- Example - Java Annotation reflection

### Description

You can obtain all annotations that have RUNTIME retention that are associated with an item by calling getAnnotations( ) on that item.

### Syntax

It has this general form:

```java title=Example.java

Annotation[ ] getAnnotations( )
```

### Example

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
/*fromwww.java2s.com*/
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
  String str();

  int val();
}

@Retention(RetentionPolicy.RUNTIME)
@interface What {
  String description();
}

@What(description = "An annotation")
@MyAnno(str = "Meta2", val = 99)
publicclass Main {
  @What(description = "test method")
  @MyAnno(str = "Testing", val = 100)
  publicstaticvoid myMeth() throws Exception {
    Main ob = new Main();
    Annotation annos[] = ob.getClass().getAnnotations();
    System.out.println("All annotations for Meta2:");
    for (Annotation a : annos) {
      System.out.println(a);
    }
    Method m = ob.getClass().getMethod("myMeth");
    annos = m.getAnnotations();
    for (Annotation a : annos) {
      System.out.println(a);
    }

  }

  publicstaticvoid main(String args[]) throws Exception {
    myMeth();
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Annotation Default Values
- Syntax for Java Annotation Default Values
- Example - How to use the default value from an annotation
