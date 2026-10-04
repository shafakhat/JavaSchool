---
title: Arrays are automatically cloneable
nav: Arrays are automatically c...
description: Imported from the java2s.com archive: Arrays are automatically cloneable
section: Imported - java2s Archive
order: 1200
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Arraysareautomaticallycloneable.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int[] ints = new int[] { 123, 234 };
    int[] intsClone = (int[]) ints.clone();
  }
}
```

| 5.18.1. | Demonstrate the clone() method. |
|---|---|
| 5.18.2. | Override the clone() method. |
| 5.18.3. | Copying Objects implements Cloneable |
| 5.18.4. | Construct clone of an object |
| 5.18.5. | construct clone of an object and call constructor in the super class |
| 5.18.6. | public Object clone() throws CloneNotSupportedException |
| 5.18.7. | Cast after cloning |
| 5.18.8. | Shallow copy then deep copy |
| 5.18.9. | Uses serialization to perform deep copy cloning. |
| 5.18.10. | Deep clone Object |
| 5.18.11. | Deep clone serializing/de-serializng Clone |
| 5.18.12. | Serializable Clone |
| 5.18.13. | Manipulate properties after clone operation |
| 5.18.14. | Clone an object with clone method from parent |
| 5.18.15. | Arrays are automatically cloneable |
| 5.18.16. | A collection of utilities to workaround limitations of Java clone framework |
| 5.18.17. | Copy an serializable object deeply |
| 5.18.18. | Clone an array |
