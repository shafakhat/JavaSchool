---
title: Define new annotation type
nav: Define new annotation type
description: @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Definenewannotationtype.htm
---
- All annotation types automatically extend the Annotation interface.
- Annotation is a super-interface of all annotations.
- It overrides hashCode( ), equals( ), and toString() defined by Object.
- It defines annotationType( ), which returns a Class object that represents the invoking annotation.
- When you apply an annotation, you give values to its members.

```java title=Example.java
// A simple annotation type.
@interface MyAnnotation {
  String stringValue();

  int intValue();
}

publicclass MainClass {
  // Annotate a method.
  @MyAnnotation(stringValue = "Annotation Example", intValue = 100)
  publicstaticvoid myMethod() {
  }

}
```
