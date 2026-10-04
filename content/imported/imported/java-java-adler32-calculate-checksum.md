---
title: Java Adler32 calculate checksum
nav: Java Adler32 calculate che...
description: ad.update(data);//www.java2s.comlong adler32Checksum = ad.getValue();
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20210102122012/http://www.java2s.com/ref/java/java-adler32-calculate-checksum.html
---
- java.util.zip
- java.util.zip Adler32 CRC32 CRC32C Deflater Inflater ZipFile ZipInputStream ZipOutputStream

## Description

Java Adler32 calculate checksum

```java title=Example.java
import java.util.zip.Adler32;

publicclass Main {
  publicstaticvoid main(String[] args) throwsException {
    String str = "demo2s.com";
    byte[] data = str.getBytes("UTF-8");

    // Compute Adler32 checksum
    Adler32 ad = new Adler32();
    ad.update(data);//www.java2s.comlong adler32Checksum = ad.getValue();
    System.out.println("Adler32: " + adler32Checksum);

  }
}
```

PreviousNext

## Related

- Java Stream sort operation
- Java Stream Spliterator
- Java Stream Spliterator try to split
- Java CRC32 calculate checksum
- Java CRC32C calculate check sum
