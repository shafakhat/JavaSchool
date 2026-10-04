---
title: Creating Annotations
nav: Creating Annotations
description: Imported from the java2s.com archive: Creating Annotations
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20070705184247/http://www.java2s.com:80/Tutorial/Java/0020__Language/CreatingAnnotations.htm
---
Annotation is created based on the interface.

- Adding '@' before the keyword interface to declare an annotation type.
- All annotations consist only method declarations.
- These methods act much like fields.

Our first annotation type:

```java title=Example.java
// A simple annotation type.
@interface MyAnnotation {
  String stringValue();
  int intValue();
}
```
