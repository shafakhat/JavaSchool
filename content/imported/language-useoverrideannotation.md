---
title: Use Override annotation
nav: Use Override annotation
description: Imported from the java2s.com archive: Use Override annotation
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/UseOverrideannotation.htm
---
```java title=Example.java
public class Main {
  private String field;
  private String attribute;
  @Override
  public int hashCode() {
    return field.hashCode() + attribute.hashCode();
  }
  @Override
  public String toString() {
    return field + " " + attribute;
  }
}
```
