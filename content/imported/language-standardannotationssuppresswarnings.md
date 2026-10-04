---
title: Standard Annotations
nav: Standard Annotations
description: SuppressWarnings is used to suppress compiler warnings. You can apply @SuppressWarnings to types, constructors, methods, fields, parameters, and local variables.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/StandardAnnotationsSuppressWarnings.htm
---
SuppressWarnings is used to suppress compiler warnings. You can apply @SuppressWarnings to types, constructors, methods, fields, parameters, and local variables.

The following are valid parameters to @SuppressWarnings:

- unchecked. Give more detail for unchecked conversion.
- path. Warn about nonexistent path (classpath, sourcepath, etc) directories.
- serial. Warn about missing serialVersionUID definitions on serializable classes.
- finally. Warn about finally clauses that cannot complete normally.
- fallthrough. Check switch blocks for fall-through cases.

```java title=Example.java
switch (i) {
      case 1:
          System.out.println("1");
          break;
      case 2:
          System.out.println ("2");
          // falling through
case 3:
          System.out.println ("3");
      }
```
