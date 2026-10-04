---
title: Java IO Tutorial - Java Reader Writer
nav: Java IO Tutorial - Java Re...
description: A reader is used when we want to read character-based data from a data source. A writer is used when we want to write character-based data.
section: Imported - java2s Archive
order: 50211
source: https://www.java2s.com/Tutorials/Java/Java_io/0500__Java_io_Reader_Writer.html
---
```java title=Example.java
```

Java readers and writers are character-based streams.

A reader is used when we want to read character-based data from a data source. A writer is used when we want to write character-based data.

If we have a stream that supplies bytes and we want to read characters by getting those bytes decoded into characters, we should use the InputStreamReader class.

For example, if we have an InputStream object called iso, and we want to get a Reader object instance, we can do so as follows:

```java title=Example.java

Reader  reader = new InputStreamReader(iso);
```

If we know the encoding used in the byte-based stream, we can specify it while creating a Reader object as follows:

```java title=Example.java

Reader  reader = new InputStreamReader(iso,  "US-ASCII");
```

Similarly, we can create a Writer object to spit out characters from a bytes-based output stream as follows, assuming that oso is an OutputStream object:

The following code creates a Writer object from OutputStream using the platform default encoding.

```java title=Example.java

Writer writer  = new OutputStreamWriter(oso);
```

Create a Writer object from OutputStream using the "US-ASCII" encoding

```java title=Example.java

Writer writer  = new OutputStreamWriter(oso,  "US-ASCII");
```

Sample

```java title=Example.java

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
publicclass Main {
  publicstatic void main(String[] args) {
    String destFile = "test.txt";
    try (BufferedWriter bw = new BufferedWriter(new FileWriter(destFile))) {
      bw.append("test");
      bw.newLine();
      bw.append("test1");
      bw.newLine();
      bw.append("test2");
      bw.newLine();
      bw.append("test3");
      bw.flush();
    }  catch (Exception e2) {
      e2.printStackTrace();
    }
  }
}
```

The following code reads the text from the test.txt file.

```java title=Example.java

import java.io.BufferedReader;
import java.io.FileReader;
publicclass Main {
  publicstatic void main(String[] args) throws Exception{
    String srcFile = "test.txt";
    BufferedReader br = new BufferedReader(new FileReader(srcFile));
    String text = null;
    while ((text = br.readLine()) != null) {
      System.out.println(text);
    }
    br.close();
  }
}
```

Converting a byte-based stream to a character-based stream is straightforward.

If we have an InputStream object, we can get a Reader object by wrapping it inside an InputStreamReader object, like so:

```java title=Example.java

InputStream is = create your  InputStream object here;
Reader  reader = new InputStreamReader(is);
```

To construct a BufferedReader object from an InputStream object, we can do that as follows:

```java title=Example.java

InputStream is = create your  InputStream object here;
BufferedReader br  = new BufferedReader(new InputStreamReader(is));
```

We can construct a Writer object from an OutputStream object as follows:

```java title=Example.java

OutputStream os  = create your  OutputStream object here; Writer writer  = new OutputStreamWriter(os);
```

## Example

```java title=Example.java
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.Reader;
import java.io.FilterReader;
import java.io.IOException;
//fromwww.java2s.comclass LowerCaseReader extends FilterReader {
  public LowerCaseReader(Reader in) {
    super(in);
  }
  @Override
  publicint read(char[] cbuf, int off, int len) throws IOException {
    int count = super.read(cbuf, off, len);
    if (count != -1) {
      // Convert all read characters to lowercase
int limit = off + count;
      for (int i = off; i < limit; i++) {
        cbuf[i] = Character.toLowerCase(cbuf[i]);
      }
    }
    return count;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    String fileName = "test.txt";
    LowerCaseReader lcr = new LowerCaseReader(new FileReader(fileName));
    int c = -1;
    while ((c = lcr.read()) != -1) {
      System.out.print((char) c);
    }
    lcr.close();
    BufferedReader br = new BufferedReader(new LowerCaseReader(new FileReader(
        fileName)));
    String str = null;
    while ((str = br.readLine()) != null) {
      System.out.println(str);
    }
    br.close();
  }
}
```

The code above generates the following result.

- « Previous
