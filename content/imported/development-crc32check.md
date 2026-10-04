---
title: CRC32 check
nav: CRC32 check
description: public static long getCRC32(InputStream in) throws IOException {
section: Imported - java2s Archive
order: 1813
source: https://web.archive.org/web/20140829081850/http://www.java2s.com/Tutorial/Java/0120__Development/CRC32check.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.zip.CRC32;
import java.util.zip.Checksum;
public class MainClass {
  public static void main(String[] args) throws IOException {
    FileInputStream fin = new FileInputStream(args[0]);
    System.out.println(args[0] + ":\t" + getCRC32(fin));
    fin.close();
  }
  public static long getCRC32(InputStream in) throws IOException {
    Checksum cs = new CRC32();
    // more efficient to read chunks of data at a time
    for (int b = in.read(); b != -1; b = in.read()) {
      cs.update(b);
    }
    return cs.getValue();
  }
}
```

6.30.1.  CRC32 check
