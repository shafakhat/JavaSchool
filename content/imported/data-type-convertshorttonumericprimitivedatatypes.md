---
title: Convert Short to numeric primitive data types
nav: Convert Short to numeric p...
description: Imported from the java2s.com archive: Convert Short to numeric primitive data types
section: Imported - java2s Archive
order: 1458
source: https://web.archive.org/web/20140829091444/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertShorttonumericprimitivedatatypes.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Short sObj = new Short("10");
    byte b = sObj.byteValue();
    System.out.println(b);
    short s = sObj.shortValue();
    System.out.println(s);
    int i = sObj.intValue();
    System.out.println(i);
    float f = sObj.floatValue();
    System.out.println(f);
    double d = sObj.doubleValue();
    System.out.println(d);
    long l = sObj.longValue();
    System.out.println(l);
  }
}
/*
10
10
10
10.0
10.0
10
*/
```

| 2.5.1. | Java short: short is 16 bit signed type ranges from –32,768 to 32,767. |
|---|---|
| 2.5.2. | Using short data type |
| 2.5.3. | Min and Max values of datatype short |
| 2.5.4. | Compare Two Java short Arrays |
| 2.5.5. | Cast back to short |
| 2.5.6. | Cast result of plus opertion to byte |
| 2.5.7. | Convert Java String to Short |
| 2.5.8. | Use toString method of Short class to convert Short into String. |
| 2.5.9. | Use Short constructor to convert short primitive type to Short object |
| 2.5.10. | Convert String to short primitive |
| 2.5.11. | Convert Short to numeric primitive data types |
| 2.5.12. | Java Sort short Array |
| 2.5.13. | Computation with Shorter Integer Types |
