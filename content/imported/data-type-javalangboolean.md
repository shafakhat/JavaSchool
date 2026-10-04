---
title: java.lang.Boolean
nav: java.lang.Boolean
description: The java.lang.Boolean class wraps a boolean. You can construct a Boolean object from a boolean or a String, using one of these constructors.
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20140218005301/http://www.java2s.com/Tutorial/Java/0040__Data-Type/javalangBoolean.htm
---
The java.lang.Boolean class wraps a boolean. You can construct a Boolean object from a boolean or a String, using one of these constructors.

```java title=Example.java
public Boolean (boolean value)
     public Boolean (String value)
```

For example:

```java title=Example.java
Boolean b1 = new Boolean (false);
     Boolean b2 = new Boolean ("true");
```

To convert a Boolean to a boolean, use its booleanValue method: public boolean booleanValue()

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    Boolean b1 = new Boolean(false);
    Boolean b2 = new Boolean("true");
    System.out.println(b1.booleanValue());
    System.out.println(b2.booleanValue());
  }
}
java title=Example.java
false
true
```
