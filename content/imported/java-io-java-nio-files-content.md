---
title: Java IO Tutorial - Java Files Content
nav: Java IO Tutorial - Java Fi...
description: Files.probeContentType(Path path) method probes the content type of a file.
section: Imported - java2s Archive
order: 50234
source: https://www.java2s.com/Tutorials/Java/Java_io/1010__Java_nio_Files_Content.html
---
## Content Type of a File

Files.probeContentType(Path path) method probes the content type of a file.

The method returns the content type in the string form of the value of a Multipurpose Internet Mail Extension (MIME) content type.

If the content type of a file cannot be determined, it returns null.

The following code shows how to probe the content type of a file.

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path p = Paths.get("C:\\Java_Dev\\test1.txt");
    try {
      String contentType = Files.probeContentType(p);
      System.out.format("Content type   of  %s  is %s%n", p, contentType);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Reading the Contents of a File

The Files class contains the following methods to read the contents of a file as bytes and lines of text:

- static byte[] readAllBytes(Path path) - reads all bytes from a file.
- static List readAllLines(Path path) - reads the entire contents of a file lines of text.
- static List readAllLines(Path path, Charset cs)

The Files class can obtain InputStream and BufferedReader objects from a Path object.

newInputStream(Path path, OpenOption... options) method returns an InputStream object for the specified path. It assumes that the file's contents are in the UTF-8 charset.

The newBufferedReader(Path path) and newBufferedReader(Path path, Charset cs) method returns a BufferedReader. We can specify the charset.

The Files class provides methods to obtain a SeekableByteChannel object from a Path object using its newByteChannel(Path path, OpenOption... options) method.

OpenOption type configures the file being opened. The following table lists the values with their descriptions for the OpenOption type. OpenOption is an interface in the java.nio.file package.

The StandardOpenOption enum in the java.nio.file package implements the OpenOption interface.

StandardOpenOption  Description
---  ---
APPEND  Appends the written data to the existing file, if the file is opened for writing.
CREATE  Creates a new file, if it does not exist.
CREATE_NEW  Creates a new file, if it does not exist. If the file already exists, it fails the operation.
DELETE_ON_CLOSE  Deletes the file when the stream is closed. It is useful when used with a temporary file.
DSYNC  Keeps the contents of the file synchronized with the underlying storage.
READ  Opens a file with a read access.
SPARSE  If it is used with the CREATE_NEW option, it is a hint to the file system that the new file should be a sparse file.
SYNC  Keeps the content and the metadata of the file synchronized with the underlying storage.
TRUNCATE_EXISTING  Truncates the length of an existing file to zero if the file is opened for a write access.
WRITE  Opens a file for a write access.

The following code obtains a SeekableByteChannel object for test2.txt file in the default directory.

It opens the file for a READ and WRITE access. It uses the CREATE option, so the file is created if it does not exist.

```java title=Example.java
import static java.nio.file.StandardOpenOption.CREATE;
import static java.nio.file.StandardOpenOption.READ;
import static java.nio.file.StandardOpenOption.WRITE;
import java.nio.channels.SeekableByteChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    Path src = Paths.get("test2.txt");
    SeekableByteChannel sbc = Files.newByteChannel(src, READ, WRITE, CREATE);
  }
}
```

The following code demonstrates how to read and display the contents of a file test1.txt in our default directory. The program displays an error message if the file does not exist.

```java title=Example.java
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception{
    Charset cs = Charset.forName("US-ASCII");
    Path source = Paths.get("test1.txt");
    List<String> lines = Files.readAllLines(source, cs);
    for (String line : lines) {
        System.out.println(line);
    }
  }
}
```

## Writing to a File

We can use the following write() methods of the Files class to write contents to a file.

```java title=Example.java
static Path  write(Path path, byte[]  bytes,  OpenOption... options)
static Path  write(Path path, Iterable lines, OpenOption... options)
static Path  write(Path path, Iterable lines, Charset cs, OpenOption... options)
```

The write() method opens the file, writes the passed in contents to the file, and closes it.

If no open options are present, it opens the file with CREATE, TRUNCATE_EXISTING, and WRITE options.

If we are writing text to a file, it writes a platform-dependent line separator.

If charset is not specified when lines of text are written, UTF-8 charset is assumed.

The following code demonstrates how to write lines of texts to a file using the write() method.

```java title=Example.java
importstatic java.nio.file.StandardOpenOption.CREATE;
importstatic java.nio.file.StandardOpenOption.WRITE;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    List<String> texts = new ArrayList<>();
    texts.add("test");
    texts.add("test");
    Path dest = Paths.get("twinkle.txt");
    Charset cs = Charset.forName("US-ASCII");
    try {
      Path p = Files.write(dest, texts, cs, WRITE, CREATE);
      System.out.println("Text was written to " + p.toAbsolutePath());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

Files.newOutputStream(Path path, OpenOption... options) returns an OutputStream for the specified path.

Files.newBufferedWriter(Path path, Charset cs, OpenOption... options) method returns a BufferedWriter for the specified path.

The code above generates the following result.

## Random Access to a File

A SeekableByteChannel object provides random access to a file.

We can get a SeekableByteChannel object for a Path using the newByteChannel() method of the Files class as follows:

```java title=Example.java
Path  src = Paths.get("test.txt");
SeekableByteChannel seekableChannel  = Files.newByteChannel(src, READ,  WRITE,  CREATE,  TRUNCATE_EXISTING);
```

We can get the size of the entity of a SeekableByteChannel in bytes using its size() method.

As the data is truncated or written to the channel, the size is updated.

```java title=Example.java
importstatic java.nio.file.StandardOpenOption.CREATE;
importstatic java.nio.file.StandardOpenOption.READ;
importstatic java.nio.file.StandardOpenOption.TRUNCATE_EXISTING;
importstatic java.nio.file.StandardOpenOption.WRITE;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.channels.SeekableByteChannel;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path src = Paths.get("test.txt");
    String encoding = System.getProperty("file.encoding");
    Charset cs = Charset.forName(encoding);
    try (SeekableByteChannel seekableChannel = Files.newByteChannel(src, READ,
        WRITE, CREATE, TRUNCATE_EXISTING)) {
      printDetails(seekableChannel, "Before writing data");
      writeData(seekableChannel, cs);
      printDetails(seekableChannel, "After writing data");
      seekableChannel.position(0);
      printDetails(seekableChannel, "After resetting position to 0");
      readData(seekableChannel, cs);
      printDetails(seekableChannel, "After reading data");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  publicstaticvoid writeData(SeekableByteChannel seekableChannel, Charset cs)
      throws IOException {
    String separator = System.getProperty("line.separator");
    StringBuilder sb = new StringBuilder();
    sb.append("test");
    sb.append(separator);
    sb.append("test2");
    sb.append(separator);
    CharBuffer charBuffer = CharBuffer.wrap(sb);
    ByteBuffer byteBuffer = cs.encode(charBuffer);
    seekableChannel.write(byteBuffer);
  }
  publicstaticvoid readData(SeekableByteChannel seekableChannel, Charset cs)
      throws IOException {
    ByteBuffer byteBuffer = ByteBuffer.allocate(128);
    String encoding = System.getProperty("file.encoding");
    while (seekableChannel.read(byteBuffer) > 0) {
      byteBuffer.rewind();
      CharBuffer charBuffer = cs.decode(byteBuffer);
      System.out.print(charBuffer);
      byteBuffer.flip();
    }
  }
  publicstaticvoid printDetails(SeekableByteChannel seekableChannel,
      String msg) {
    try {
      System.out.println(msg + ": Size   = " + seekableChannel.size()
          + ", Position = " + seekableChannel.position());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
