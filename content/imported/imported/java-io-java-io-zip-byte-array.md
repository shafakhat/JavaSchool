---
title: Java IO Tutorial - Java Zip Byte Array
nav: Java IO Tutorial - Java Zi...
description: Java provides an Adler32 class in the java.util.zip package to compute the Adler-32 checksum for bytes of data.
section: Imported - java2s Archive
order: 50217
source: https://www.java2s.com/Tutorials/Java/Java_io/0800__Java_io_Zip_Byte_Array.html
---
```java title=Example.java
« Previous
```

- Next »

## checksum

Java provides an Adler32 class in the java.util.zip package to compute the Adler-32 checksum for bytes of data.

We need to call the update() method of this class to pass bytes to it.

There is also another class named CRC32 in the same package, which lets you compute a checksum using the CRC32 algorithm.

The following code illustrates how to use the Adler32 and CRC32 classes to compute checksums.

```java title=Example.java
import java.util.zip.Adler32;
import java.util.zip.CRC32;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String str = "HELLO";
    byte[] data = str.getBytes("UTF-8");
    System.out.println("Adler32 and  CRC32  checksums  for " + str);
    // Compute Adler32 checksum
    Adler32 ad = new Adler32();
    ad.update(data);
    long adler32Checksum = ad.getValue();
    System.out.println("Adler32: " + adler32Checksum);
    // Compute CRC32 checksum
    CRC32 crc = new CRC32();
    crc.update(data);
    long crc32Checksum = crc.getValue();
    System.out.println("CRC32: " + crc32Checksum);
  }
}
```

The code above generates the following result.

## Compressing Byte Arrays

We can use the Deflater and Inflater classes in the java.util.zip package to compress and decompress data in a byte array, respectively.

We can specify the compression level using one of the constants in the Deflater class.

Those constant are BEST_COMPRESSION, BEST_ SPEED, DEFAULT_COMPRESSION, and NO_COMPRESSION.

The best speed means lower compression ratio and the best compression means slower compression speed.

```java title=Example.java

Deflater  compressor = new Deflater(Deflater.BEST_COMPRESSION);
```

By default, the compressed data using the Deflater object will be in the ZLIB format.

To compress data in GZIP or PKZIP format, specify that by using the boolean flag as true in the constructor.

```java title=Example.java

// Uses  the   best speed  compression and  GZIP format
Deflater  compressor = new Deflater(Deflater.BEST_SPEED, true);
```

The following code shows how to do Compressing and Decompressing a byte Array Using Deflater and the Inflater classes

```java title=Example.java
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.zip.DataFormatException;
import java.util.zip.Deflater;
import java.util.zip.Inflater;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String input = "Hello world!";
    byte[] uncompressedData = input.getBytes("UTF-8");
    byte[] compressedData = compress(uncompressedData,
        Deflater.BEST_COMPRESSION, false);
    byte[] decompressedData = decompress(compressedData, false);
    String output = new String(decompressedData, "UTF-8");
    System.out.println("Uncompressed data length: " + uncompressedData.length);
    System.out.println("Compressed data length:  " + compressedData.length);
    System.out.println("Decompressed data length:  " + decompressedData.length);
  }
  publicstaticbyte[] compress(byte[] input, int compressionLevel,
      boolean GZIPFormat) throws IOException {
    Deflater compressor = new Deflater(compressionLevel, GZIPFormat);
    compressor.setInput(input);
    compressor.finish();
    ByteArrayOutputStream bao = new ByteArrayOutputStream();
    byte[] readBuffer = newbyte[1024];
    int readCount = 0;
    while (!compressor.finished()) {
      readCount = compressor.deflate(readBuffer);
      if (readCount > 0) {
        bao.write(readBuffer, 0, readCount);
      }
    }
    compressor.end();
    return bao.toByteArray();
  }
  publicstaticbyte[] decompress(byte[] input, boolean GZIPFormat)
      throws IOException, DataFormatException {
    Inflater decompressor = new Inflater(GZIPFormat);
    decompressor.setInput(input);
    ByteArrayOutputStream bao = new ByteArrayOutputStream();
    byte[] readBuffer = newbyte[1024];
    int readCount = 0;
    while (!decompressor.finished()) {
      readCount = decompressor.inflate(readBuffer);
      if (readCount > 0) {
        bao.write(readBuffer, 0, readCount);
      }
    }
    decompressor.end();
    return bao.toByteArray();
  }
}
```

The code above generates the following result.

- Next »
- « Previous
