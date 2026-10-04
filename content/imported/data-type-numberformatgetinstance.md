---
title: NumberFormat.getInstance()
nav: NumberFormat.getInstance()
description: Imported from the java2s.com archive: NumberFormat.getInstance()
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/NumberFormatgetInstance.htm
---
```java title=Example.java
import java.text.NumberFormat;
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    NumberFormat nf = NumberFormat.getInstance();
    for (double x = Math.PI; x < 100000; x *= 10) {
      String formattedNumber = nf.format(x);
      System.out.println(formattedNumber + "\t" + x);
    }
  }
}
java title=Example.java
3.142	3.141592653589793
31.416	31.41592653589793
314.159	314.1592653589793
3,141.593	3141.5926535897934
31,415.927	31415.926535897932
```
