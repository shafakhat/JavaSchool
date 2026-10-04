---
title: Determine bean's property type
nav: Determine bean's property ...
description: Class type = PropertyUtils.getPropertyType(recording, "title");
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20100624050824/http://www.java2s.com:80/Tutorial/Java/0120__Development/Determinebeanspropertytype.htm
---
```java title=Example.java
import org.apache.commons.beanutils.PropertyUtils;
public class Main {
  public static void main(String[] args) throws Exception {
    Recording recording = new Recording();
    recording.setTitle("Magical Mystery Tour");
    Class type = PropertyUtils.getPropertyType(recording, "title");
    System.out.println("type = " + type.getName());
    String value = (String) PropertyUtils.getProperty(recording, "title");
    System.out.println("value = " + value);
  }
}
```
