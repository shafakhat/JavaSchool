---
title: Getting the Component Type of an Array Object
nav: Getting the Component Type...
description: Imported from the java2s.com archive: Getting the Component Type of an Array Object
section: Imported - java2s Archive
order: 2167
source: https://web.archive.org/web/20140829091742/http://www.java2s.com/Tutorial/Java/0125__Reflection/GettingtheComponentTypeofanArrayObject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new int[1][2][3];
    o.getClass().getComponentType();
  }
}
```

| 7.9.1. | Determining If an Object Is an Array |
|---|---|
| 7.9.2. | Demonstrates the use of the Array class |
| 7.9.3. | Create array with Array.newInstance |
| 7.9.4. | Is field an array |
| 7.9.5. | Create integer array with Array.newInstance |
| 7.9.6. | Use Array.setInt to fill an array |
| 7.9.7. | Use Array.setShort and Array.setLong |
| 7.9.8. | Getting the Length and Dimensions of an Array Object |
| 7.9.9. | Getting the Component Type of an Array Object |
| 7.9.10. | Array reflection and two dimensional array |
| 7.9.11. | class name for double and float array |
| 7.9.12. | Returns the length of the specified array, can deal with Object arrays and with primitive arrays. |
