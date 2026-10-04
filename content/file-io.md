---
title: Java File I/O
nav: File I/O
description: Read and write text files with Files, BufferedReader, Files.lines and NIO paths in Java.
section: Core Java
order: 20
---

## Two worlds: `java.io` and `java.nio`

- **Classic streams** (`FileReader`, `BufferedReader`) - byte/char streams, great for incremental reading.
- **NIO (`java.nio.file`)** - `Path`, `Files`, one-liners for whole-file operations.

Modern Java code usually starts with `Files` from NIO.

## Paths

```java title=PathsDemo.java
import java.nio.file.Path;
import java.nio.file.Paths;

public class PathsDemo {
    public static void main(String[] args) {
        Path p = Paths.get("data", "notes.txt");     // relative path

        System.out.println(p);            // data/notes.txt
        System.out.println(p.toAbsolutePath());
        System.out.println(p.getFileName());         // notes.txt
        System.out.println(p.getParent());           // data
        System.out.println(p.toString().replace('\\', '/'));

        Path abs = Path.of("/etc/hostname");         // Java 11+ factory
        System.out.println(abs.isAbsolute());
    }
}
```

## Writing a text file

```java title=WriteFile.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class WriteFile {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("report.txt");

        // one string (overwrites)
        Files.writeString(file, "line one\nline two\n");

        // many lines
        Files.write(file, List.of("alpha", "beta", "gamma"));

        // append - use Files.newBufferedWriter with the APPEND option
        Files.writeString(file, "extra line\n",
            java.nio.file.StandardOpenOption.APPEND);

        System.out.println("bytes: " + Files.size(file));
    }
}
```

> **Note:** Methods that can fail with I/O errors either `throws IOException` (as above) or you handle it in a `try/catch`. The compiler forces you to choose.

## Reading a text file

```java title=ReadFile.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class ReadFile {
    public static void main(String[] args) throws IOException {
        Path file = Path.of("report.txt");

        // 1. whole file as one String
        String all = Files.readString(file);
        System.out.println("--- full ---");
        System.out.print(all);

        // 2. whole file as a List<String>, one element per line
        List<String> lines = Files.readAllLines(file);
        System.out.println("--- lines (" + lines.size() + ") ---");
        for (int i = 0; i < lines.size(); i++) {
            System.out.println((i + 1) + ": " + lines.get(i));
        }
    }
}
```

## Large files: stream line by line

Never `readAllLines` on a 10 GB file - process it lazily:

```java title=StreamLines.java
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class StreamLines {
    public static void main(String[] args) {
        try (BufferedReader br = Files.newBufferedReader(Path.of("report.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {     // null = end of file
                if (line.contains("beta")) {
                    System.out.println("found: " + line);
                }
            }
        } catch (IOException e) {
            System.out.println("read error: " + e.getMessage());
        }
    }
}
```

Or with the stream version (also auto-closable):

```java title=FilesLines.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class FilesLines {
    public static void main(String[] args) {
        try (var stream = Files.lines(Path.of("report.txt"))) {
            long count = stream.filter(l -> !l.isBlank()).count();
            System.out.println("non-blank lines: " + count);
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## Working with files and directories

```java title=FilesOps.java
import java.io.IOException;
import java.nio.file.*;

public class FilesOps {
    public static void main(String[] args) throws IOException {
        Path dir = Paths.get("tmp-demo");
        Files.createDirectories(dir);

        Path f = dir.resolve("a.txt");
        Files.writeString(f, "content");

        System.out.println("exists? " + Files.exists(f));
        System.out.println("size   = " + Files.size(f));
        System.out.println("is dir? " + Files.isDirectory(dir));

        // list a directory (lazily)
        try (var s = Files.list(dir)) {
            s.forEach(p -> System.out.println("file: " + p.getFileName()));
        }

        // copy / move / delete
        Path copy = dir.resolve("b.txt");
        Files.copy(f, copy, StandardCopyOption.REPLACE_EXISTING);
        Files.move(copy, dir.resolve("c.txt"), StandardCopyOption.REPLACE_EXISTING);
        Files.deleteIfExists(dir.resolve("c.txt"));
        Files.deleteIfExists(dir.resolve("a.txt"));
        Files.deleteIfExists(dir);
    }
}
```

## Classic byte streams (still everywhere)

```java title=ByteStreams.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ByteStreams {
    public static void main(String[] args) {
        // write bytes
        try (FileOutputStream out = new FileOutputStream("blob.bin")) {
            out.write("binary-ish".getBytes(java.nio.charset.StandardCharsets.UTF_8));
        } catch (IOException e) {
            System.out.println("write failed");
        }

        // read bytes
        try (FileInputStream in = new FileInputStream("blob.bin")) {
            byte[] buffer = new byte[64];
            int n = in.read(buffer);                 // n = bytes actually read
            System.out.println("read " + n + " bytes");
            System.out.println(new String(buffer, 0, n, java.nio.charset.StandardCharsets.UTF_8));
        } catch (IOException e) {
            System.out.println("read failed");
        }
    }
}
```

Remember the pattern: **loop over `read()` into a buffer**, because a single read may return fewer bytes than requested.

## Always handle charset explicitly

```java title=Charset.java
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class Charset {
    public static void main(String[] args) throws IOException {
        Files.writeString(Path.of("uni.txt"), "こんにちは - नमस्ते", StandardCharsets.UTF_8);
        String back = Files.readString(Path.of("uni.txt"), StandardCharsets.UTF_8);
        System.out.println(back);
    }
}
```

> **Warning:** The platform default charset differs across machines (Windows often Cp1252, servers often UTF-8). For anything persisted, specify `StandardCharsets.UTF_8` explicitly.

## Which API should I use?

| Task | Use |
|---|---|
| Read whole file (< ~100 MB) | `Files.readString` / `readAllLines` |
| Write whole file / list | `Files.writeString` / `Files.write` |
| Huge files, line processing | `Files.lines` or `BufferedReader` |
| Binary data | `InputStream`/`OutputStream` with buffers |
| Structured data (CSV/JSON) | parser library on top of the above |

Next: [Threads](threads.html) - doing multiple things at once.
