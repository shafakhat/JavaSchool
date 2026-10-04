---
title: The 'Class' class also brings the possibility of creating an object without using the new keyword.
nav: The 'Class' class also bri...
description: The static forName method creates a Class object of the given class name. The newInstance method creates a new instance of a class.
section: Imported - java2s Archive
order: 1249
source: https://web.archive.org/web/20140829090212/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/TheClassclassalsobringsthepossibilityofcreatinganobjectwithoutusingthenewkeyword.htm
---
The static forName method creates a Class object of the given class name. The newInstance method creates a new instance of a class.

```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    Class klass = null;
    try {
      klass = Class.forName("java.lang.String");
    } catch (ClassNotFoundException e) {
    }
    if (klass != null) {
      try {
        // create an instance of the Test class
        String test = (String) klass.newInstance();
      } catch (IllegalAccessException e) {
      } catch (InstantiationException e) {
      }
    }
  }
}
```
