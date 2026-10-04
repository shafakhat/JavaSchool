---
title: Multiple Constructors
nav: Multiple Constructors
description: Imported from the java2s.com archive: Multiple Constructors
section: Imported - java2s Archive
order: 1086
source: https://web.archive.org/web/20140829082804/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MultipleConstructors.htm
---
```java title=Example.java
class Sphere {
  int radius = 0;
  Sphere() {
    radius = 1;
  }
  Sphere(int radius) {
    this.radius = radius;
  }
}
```

| 5.2.1. | Using Constructors |
|---|---|
| 5.2.2. | The Default Constructor |
| 5.2.3. | Multiple Constructors |
| 5.2.4. | Calling a Constructor From a Constructor |
| 5.2.5. | Duplicating Objects using a Constructor |
| 5.2.6. | Class Initializer: during declaration |
| 5.2.7. | Order of constructor calls |
