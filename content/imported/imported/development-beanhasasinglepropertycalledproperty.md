---
title: Bean has a single property called property.
nav: Bean has a single property...
description: Imported from the java2s.com archive: Bean has a single property called property.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20100624051213/http://www.java2s.com:80/Tutorial/Java/0120__Development/Beanhasasinglepropertycalledproperty.htm
---
```java title=Example.java
import java.io.Serializable;
public class BasicBean implements Serializable {
  boolean property;
  public BasicBean() {
  }
  public boolean getProperty() {
    return property;
  }
  public boolean isProperty() {
    return property;
  }
  public void setProperty(boolean newValue) {
    property = newValue;
  }
}
```
