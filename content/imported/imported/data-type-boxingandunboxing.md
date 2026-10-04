---
title: Boxing and Unboxing
nav: Boxing and Unboxing
description: Imported from the java2s.com archive: Boxing and Unboxing
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/BoxingandUnboxing.htm
---
- Boxing refers to the conversion of a primitive to a corresponding wrapper instance, such as from an int to a java.lang.Integer.
- Unboxing is the conversion of a wrapper instance to a primitive type, such as from Byte to byte.

```java title=Example.java
publicclass MainClass{

  publicstaticvoid main(String[] args){

     Integer number = newInteger (100);
     int [] ints = newint [2];
     ints [0] = number;
  }

}
```
