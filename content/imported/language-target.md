---
title: Target
nav: Target
description: Target indicates which program element(s) can be annotated using instances of the annotated annotation type. The value of Target is one of the members of the java.lang.an
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0020__Language/Target.htm
---
Target indicates which program element(s) can be annotated using instances of the annotated annotation type. The value of Target is one of the members of the java.lang.annotation.ElementType enum:

- ANNOTATION_TYPE. The annotated annotation type can be used to annotate annotation type declaration.
- CONSTRUCTOR. The annotated annotation type can be used to annotate constructor declaration.
- FIELD. The annotated annotation type can be used to annotate field declaration.
- LOCAL_VARIABLE. The annotated annotation type can be used to annotate local variable declaration.
- METHOD. The annotated annotation type can be used to annotate method declaration.
- PACKAGE. The annotated annotation type can be used to annotate package declarations.
- PARAMETER. The annotated annotation type can be used to annotate parameter declarations.
- TYPE. The annotated annotation type can be used to annotate type declarations.

```java title=Example.java
@Target(value=METHOD)
```

You can have multiple values in the Target annotation.

@Target(value={TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE})
