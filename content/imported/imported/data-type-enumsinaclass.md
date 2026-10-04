---
title: Enums in a Class
nav: Enums in a Class
description: Imported from the java2s.com archive: Enums in a Class
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20070429210504/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/EnumsinaClass.htm
---
```java title=Example.java
public class Shape {
  private enum ShapeType {
    RECTANGLE, TRIANGLE, OVAL
  };
  private ShapeType type = ShapeType.RECTANGLE;
  public String toString() {
    if (this.type == ShapeType.RECTANGLE) {
      return "Shape is rectangle";
    }
    if (this.type == ShapeType.TRIANGLE) {
      return "Shape is triangle";
    }
    return "Shape is oval";
  }
}
```
