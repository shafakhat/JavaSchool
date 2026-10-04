---
title: Standard Annotations
nav: Standard Annotations
description: Deprecated is a marker annotation type that can be applied to a method or a type (class/interface) to indicate that the method or type is deprecated. Deprecating a method
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/StandardAnnotationsDeprecated.htm
---
Deprecated is a marker annotation type that can be applied to a method or a type (class/interface) to indicate that the method or type is deprecated. Deprecating a method:

```java title=Example.java
publicclass DeprecatedTest {
  @Deprecated
  publicvoid serve() {

  }

}
```

If you use or override a deprecated method, you will get a warning at compile time.

```java title=Example.java
publicclass DeprecatedTest2 {
  publicstaticvoid main(String[] args) {
    DeprecatedTest test = new DeprecatedTest();
    test.serve();
  }
}

class DeprecatedTest {
  @Deprecated
  publicvoid serve() {

  }

}
```
