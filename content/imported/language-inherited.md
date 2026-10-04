---
title: Inherited
nav: Inherited
description: Imported from the java2s.com archive: Inherited
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Inherited.htm
---
- Use Inherited to annotate an annotation type, any instance of the annotation type will be inherited.
- Use Inherited to annotate a class, the annotation will be inherited by any subclass of the annotated class. If the user queries the annotation type on a class declaration, and the class declaration has no annotation of this type, then the class's parent class will automatically be queried for the annotation type. This process will be repeated until an annotation of this type is found or the root class is reached.
