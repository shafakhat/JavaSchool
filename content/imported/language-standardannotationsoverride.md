---
title: Standard Annotations
nav: Standard Annotations
description: Override is a marker annotation type that can be applied to a method to indicate to the compiler that the method overrides a method in a superclass. This annotation type
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/StandardAnnotationsOverride.htm
---
Override is a marker annotation type that can be applied to a method to indicate to the compiler that the method overrides a method in a superclass. This annotation type guards the programmer against making a mistake when overriding a method. For example, consider this class Parent:

```java title=Example.java
class Parent {
    publicfloat calculate (float a, float b) {
        return a * b;
    }
}
Whenever you want to override a method, declare the Override annotation type before the method:
publicclass Child extends Parent {
    @Override
    publicint calculate (int a, int b) {
        return (a + 1) * b;
    }
}
```
