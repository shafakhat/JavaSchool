---
title: Java IO Tutorial - Java File Lock
nav: Java IO Tutorial - Java Fi...
description: NIO supports file locking to synchronize access to a file. We have the ability to lock a region of a file or the entire file.
section: Imported - java2s Archive
order: 50227
source: https://www.java2s.com/Tutorials/Java/Java_io/0950__Java_nio_File_Locks.html
---
```java title=Example.java
« Previous
```

- Next »

NIO supports file locking to synchronize access to a file. We have the ability to lock a region of a file or the entire file.

The file locking mechanism is handled by the operating system.

There are two kinds of file locking: exclusive and shared.

Only one program can hold an exclusive lock on a region of a file.

Multiple programs can hold shared locks on the same region of a file.

We cannot mix an exclusive lock and a shared lock on the same region of a file.

java.nio.channels.FileLock class represents a file lock.

We acquire a lock on a file by using the lock() or tryLock() method of the FileChannel object.

The lock() method blocks if the lock on the requested region is not available.

The tryLock() method does not block; it returns immediately an object of the FileLock class if the lock was acquired; otherwise, it returns null.

Both lock() and tryLock() methods have two versions: one without an argument and another with arguments.

The version without an argument locks the entire file.

The version with arguments accepts the starting position of the region to lock, the number of bytes to lock, and a boolean flag to indicate if the lock is shared.

The isShared() method of the FileLock object returns true if the lock is shared; otherwise, it returns false.

The following code shows different ways of obtaining locks on a file.

```java title=Example.java
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    RandomAccessFile raf = new RandomAccessFile("test.txt", "rw");
    FileChannel fileChannel = raf.getChannel();
    FileLock lock = fileChannel.lock();
  }
}
```

## Example

Get an exclusive lock on first 10 bytes

```java title=Example.java
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    RandomAccessFile raf = new RandomAccessFile("test.txt", "rw");
    FileChannel fileChannel = raf.getChannel();
    // Get an exclusive lock on first 10 bytes
    FileLock lock = fileChannel.lock(0, 10, false);
  }
}
```

Try to get an exclusive lock on the entire file

```java title=Example.java

import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    RandomAccessFile raf = new RandomAccessFile("test.txt", "rw");
    FileChannel fileChannel = raf.getChannel();
    FileLock lock = fileChannel.tryLock();
    if (lock == null) {
      // Could not get the lock
    } else {
      // Got the lock
    }
  }
}
```

Try to lock 100 bytes starting from the 11th byte in a shared mode

```java title=Example.java

import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    RandomAccessFile raf = new RandomAccessFile("test.txt", "rw");
    FileChannel fileChannel = raf.getChannel();
    FileLock lock = fileChannel.tryLock(11, 100, true);
    if (lock == null) {
      // Could not get the lock
    } else {
      // Got the lock
    }
  }
}
```

The following code shows how to use a try-catch-finally block to acquire and release a file lock as follows:

```java title=Example.java

import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    RandomAccessFile raf = new RandomAccessFile("test.txt", "rw");
    FileChannel fileChannel = raf.getChannel();
    FileLock lock = null;
    try {
      lock = fileChannel.lock(0, 10, true);
    } catch (IOException e) {
      // Handle the exception
    } finally {
      if (lock != null) {
        try {
          lock.release();
        } catch (IOException e) {
          // Handle the exception
        }
      }
    }
  }
}
```

- Next »
- « Previous
