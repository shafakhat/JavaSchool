---
title: Pack200.newUnpacker
nav: Pack200.newUnpacker
description: Imported from the java2s.com archive: Pack200.newUnpacker
section: Imported - java2s Archive
order: 1844
source: https://web.archive.org/web/20140829090206/http://www.java2s.com/Tutorial/Java/0120__Development/Pack200newUnpacker.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.jar.JarOutputStream;
import java.util.jar.Pack200;
import java.util.zip.GZIPInputStream;
public class MainClass {
  public static void main(String[] args) throws Exception {
    String inName = args[0];
    String outName;
    if (inName.endsWith(".pack.gz")) {
      outName = inName.substring(0, inName.length() - 8);
    } else if (inName.endsWith(".pack")) {
      outName = inName.substring(0, inName.length() - 5);
    } else {
      outName = inName + ".unpacked";
    }
    JarOutputStream out = null;
    InputStream in = null;
    Pack200.Unpacker unpacker = Pack200.newUnpacker();
    out = new JarOutputStream(new FileOutputStream(outName));
    in = new FileInputStream(inName);
    if (inName.endsWith(".gz"))
      in = new GZIPInputStream(in);
    unpacker.unpack(in, out);
    out.close();
  }
}
```

6.35.1.  Pack200.newUnpacker
