---
title: Getting java.lang.Class
nav: Getting java.lang.Class
description: Imported from the java2s.com archive: Getting java.lang.Class
section: Imported - java2s Archive
order: 1206
source: https://web.archive.org/web/20140829090216/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/GettingjavalangClassInformationaboutyourobject.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    String country = "Canada";
    Class myClass = country.getClass();
    System.out.println(myClass.getName());
  }
}
java title=Example.java
java.lang.String
```

| 5.17.1. | Getting java.lang.Class: Information about your object |
|---|---|
| 5.17.2. | Comparing Objects |
| 5.17.3. | Class Object |
| 5.17.4. | Storing a reference to the String object as type Object |
| 5.17.5. | The 'Class' class also brings the possibility of creating an object without using the new keyword. |
| 5.17.6. | Assignment with objects is a bit tricky. |
| 5.17.7. | Demonstrate Run-Time Type Information. |
