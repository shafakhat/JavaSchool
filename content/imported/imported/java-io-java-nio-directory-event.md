---
title: Java IO Tutorial - Java Directory Event
nav: Java IO Tutorial - Java Di...
description: We can listen to a watch service to get alert when an object in a file system is modified.
section: Imported - java2s Archive
order: 50237
source: https://www.java2s.com/Tutorials/Java/Java_io/1040__Java_nio_Directory_Event.html
---
```java title=Example.java
```

We can listen to a watch service to get alert when an object in a file system is modified.

The following classes and interfaces in the java.nio.file package provide the watch service.

- Watchable interface
- WatchService interface
- WatchKey interface
- WatchEvent interface
- WatchEvent.Kind interface
- StandardWatchEventKinds class

A Watchable object represents a file-system object that can be watched. A Watchable object can be registered with a watch service.

A Path object is a Watchable object.

A WatchService represents a watch service. When an object is registered with a WatchService, the WatchService returns a WatchKey that serves as a token for the registration.

A WatchEvent represents an event on an object registered with a watch service. Its kind() method returns the kind of event occured.

Its context() method returns a Path object that represents the entry on which the event occurs.

The count() method returns the number of times the event occurs for a specific notification. If it returns a value greater than 1, it is a repeated event.

A WatchEvent.Kind<T> represents the kind of event occured.

The StandardWatchEventKinds class defines constants to represent the kind of an event as follows.

- ENTRY_CREATE
- ENTRY_DELETE
- ENTRY_MODIFY
- OVERFLOW

OVERFLOW represents a lost or discarded event.

To create a watch service to watch a directory for changes.

```java title=Example.java

WatchService ws = FileSystems.getDefault().newWatchService();
```

To register the Directory with the Watch Service, use the register() method which will return a WatchKey object as a registration token.

```java title=Example.java

// Get  a  Path  object for C:\myName  directory  to watch
Path  dirToWatch  = Paths.get("C:\\myName");
WatchKey token   = dirToWatch.register(ws, ENTRY_CREATE,  ENTRY_MODIFY,  ENTRY_DELETE);
```

To cancel the registration, use the cancel() method of the WatchKey.

When a directory is registered, its WatchKey is in the ready state.

We can register multiple directories with a watch service.

To retrieve a WatchKey from the Watch Service Queue, use the take() or poll() method of the WatchService object to retrieve and remove a signaled and queued WatchKey.

The take() method waits until a WatchKey is available. The poll() method lets we specify a timeout for the wait.

The following code uses an infinite loop is used to retrieve a signaled WatchKey.

```java title=Example.java
while(true)  {
    WatchKey key  = ws.take();
}
```

## Process the Events

The pollEvents() method of the WatchKey retrieves and removes all its pending events. It returns a List of WatchEvent. Each element of the List represents an event on the WatchKey.

The following code shows the typical logic for processing an event:

```java title=Example.java
while(true)  {
    WatchKey key  = ws.take();
    // Process all  events of  the   WatchKey
    for(WatchEvent<?> event  : key.pollEvents())  {
       // Process each  event here
    }
}
```

## Reset the WatchKey after Processing Events

We need to reset the WatchKey object by calling its reset() method to receive event notifications again.

The reset() method puts the WatchKey into the ready state. The reset() method returns true if the WatchKey is still valid. Otherwise, it returns false.

A WatchKey may become invalid if it is cancelled or its watch service is closed.

```java title=Example.java

// Reset   the   WatchKey
boolean isKeyValid = key.reset();
if (!isKeyValid)  {
    System.out.println("No  longer  watching "  + dirToWatch);
}
```

The WatchService is AutoCloseable. We can create an object of the WatchService in a try-with-resources block, it will be automatically closed when the program exits the block.

## Example

The following code shows how to implement a Watch Service to Monitor Changes in a Directory.

```java title=Example.java
importstatic java.nio.file.StandardWatchEventKinds.ENTRY_CREATE;
importstatic java.nio.file.StandardWatchEventKinds.ENTRY_DELETE;
importstatic java.nio.file.StandardWatchEventKinds.ENTRY_MODIFY;
importstatic java.nio.file.StandardWatchEventKinds.OVERFLOW;
//www.java2s.comimport java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.WatchEvent;
import java.nio.file.WatchEvent.Kind;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
publicclass Main {
  publicstaticvoid main(String[] args) {
    try (WatchService ws = FileSystems.getDefault().newWatchService()) {
      Path dirToWatch = Paths.get("C:\\myName");
      dirToWatch.register(ws, ENTRY_CREATE, ENTRY_MODIFY, ENTRY_DELETE);
      while (true) {
        WatchKey key = ws.take();
        for (WatchEvent<?> event : key.pollEvents()) {
          Kind<?> eventKind = event.kind();
          if (eventKind == OVERFLOW) {
            System.out.println("Event  overflow occurred");
            continue;
          }
          WatchEvent<Path> currEvent = (WatchEvent<Path>) event;
          Path dirEntry = currEvent.context();
          System.out.println(eventKind + "  occurred on  " + dirEntry);
        }
        boolean isKeyValid = key.reset();
        if (!isKeyValid) {
          System.out.println("No  longer  watching " + dirToWatch);
          break;
        }
      }
    } catch (IOException | InterruptedException e) {
      e.printStackTrace();
    }
  }
}
```

- « Previous
