---
title: Java IO Tutorial - Java ZIP File
nav: Java IO Tutorial - Java ZI...
description: Java has direct support for the ZIP file format. Typically, we would be using the following four classes from the java.util.zip package to work with the ZIP file format:
section: Imported - java2s Archive
order: 50218
source: https://www.java2s.com/Tutorials/Java/Java_io/0810__Java_io_Zip_File.html
---
```java title=Example.java
« Previous
```

- Next »

Java has direct support for the ZIP file format. Typically, we would be using the following four classes from the java.util.zip package to work with the ZIP file format:

- ZipEntry
- ZipInputStream
- ZipOutputStream
- ZipFile

A ZipEntry object represents an entry in an archive file in a ZIP file format.

A zip entry may be compressed or uncompressed.

The ZipEntry class has methods to set and get information about an entry in a ZIP file.

ZipInputStream can read data from a ZIP file for each entry.

ZipOutputStream can write data to a ZIP file for each entry.

ZipFile is a utility class to read the entries from a ZIP file.

The following code shows how to create a ZIP File

```java title=Example.java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.Deflater;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    String zipFileName = "ziptest.zip";
    String[] entries = new String[2];
    entries[0] = "test1.txt";
    entries[1] = "notes" + File.separator + "test2.txt";
    zip(zipFileName, entries);
  }
  publicstaticvoid zip(String zipFileName, String[] zipEntries) {
    try (ZipOutputStream zos = new ZipOutputStream(new BufferedOutputStream(
        new FileOutputStream(zipFileName)))) {
      // Set the compression level to best compression
      zos.setLevel(Deflater.BEST_COMPRESSION);
      for (int i = 0; i < zipEntries.length; i++) {
        File entryFile = newFile(zipEntries[i]);
        if (!entryFile.exists()) {
          System.out.println("The entry file  " + entryFile.getAbsolutePath()
              + "  does  not  exist");
          System.out.println("Aborted   processing.");
          return;
        }
        ZipEntry ze = new ZipEntry(zipEntries[i]);
        zos.putNextEntry(ze);
        addEntryContent(zos, zipEntries[i]);
        zos.closeEntry();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  publicstaticvoid addEntryContent(ZipOutputStream zos, String entryFileName)
      throws IOException, FileNotFoundException {
    BufferedInputStream bis = new BufferedInputStream(new FileInputStream(
        entryFileName));
    byte[] buffer = newbyte[1024];
    int count = -1;
    while ((count = bis.read(buffer)) != -1) {
      zos.write(buffer, 0, count);
    }
    bis.close();
  }
}
```

The code above generates the following result.

## Read Zip File

The following code shows how to read contents of a ZIP File.

```java title=Example.java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    String zipFileName = "ziptest.zip";
    String unzipdirectory = "extracted";
    unzip(zipFileName, unzipdirectory);
  }
  publicstaticvoid unzip(String zipFileName, String unzipdir) {
    try (ZipInputStream zis = new ZipInputStream(new BufferedInputStream(
        new FileInputStream(zipFileName)))) {
      ZipEntry entry = null;
      while ((entry = zis.getNextEntry()) != null) {
        // Extract teh entry's contents
        extractEntryContent(zis, entry, unzipdir);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  publicstaticvoid extractEntryContent(ZipInputStream zis, ZipEntry entry,
      String unzipdir) throws IOException, FileNotFoundException {
    String entryFileName = entry.getName();
    String entryPath = unzipdir + File.separator + entryFileName;
    createFile(entryPath);
    BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(
        entryPath));
    byte[] buffer = newbyte[1024];
    int count = -1;
    while ((count = zis.read(buffer)) != -1) {
      bos.write(buffer, 0, count);
    }
    bos.close();
  }
  publicstaticvoid createFile(String filePath) throws IOException {
    File file = newFile(filePath);
    File parent = file.getParentFile();
    if (!parent.exists()) {
      parent.mkdirs();
    }
    file.createNewFile();
  }
}
```

## Example 2

The following code shows how to use the ZipFile class.

The ZipFile class comes in handy when you just want to list the entries in a ZIP file.

```java title=Example.java
import java.io.InputStream;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    ZipFile zf = new ZipFile("ziptest.zip");
    // Get the enumeration for all zip entries and loop through them
    Enumeration<? extends ZipEntry> e = zf.entries();
    ZipEntry entry = null;
    while (e.hasMoreElements()) {
      entry = e.nextElement();
      // Get the input stream for the current zip entry
      InputStream is = zf.getInputStream(entry);
      /* Read data for the entry using the is object */// Print the name of the entry
      System.out.println(entry.getName());
    }
  }
}
```

The following code rewrites the above code using the Stream class and a lambda expression.

```java title=Example.java

import java.io.IOException;
import java.io.InputStream;
import java.util.stream.Stream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    ZipFile zf = new ZipFile("ziptest.zip");
    Stream<? extends ZipEntry> entryStream = zf.stream();
    entryStream.forEach(entry -> {
      try {
        // Get the input stream for the current zip entry
        InputStream is = zf.getInputStream(entry);
        System.out.println(entry.getName());
      } catch (IOException e) {
        e.printStackTrace();
      }
    });
  }
}
```

The GZIPInputStream and GZIPOutputStream classes are used to work with the GZIP file format.

- Next »
- « Previous
