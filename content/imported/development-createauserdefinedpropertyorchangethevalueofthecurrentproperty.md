---
title: Create a user-defined property or change the value of the current property
nav: Create a user-defined prop...
description: Imported from the java2s.com archive: Create a user-defined property or change the value of the current property
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20070716104133/http://www.java2s.com:80/Tutorial/Java/0120__Development/Createauserdefinedpropertyorchangethevalueofthecurrentproperty.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    System.setProperty("password", "myPassword");
    System.out.println(System.getProperty("password"));
  }
}
```

```java title=Example.java
myPassword
```
