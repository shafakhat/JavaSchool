---
title: import javax.activation.CommandInfo;
nav: import javax.activation.Co...
description: MailcapCommandMap mailcapCommandMap = new MailcapCommandMap();
section: Imported - java2s Archive
order: 1926
source: https://web.archive.org/web/20140829090019/http://www.java2s.com/Tutorial/Java/0120__Development/importjavaxactivationCommandInfo.htm
---
```java title=Example.java
import javax.activation.MailcapCommandMap;
public class MailcapCommandMapDemo1 {
  public static void main(String[] args) {
    MailcapCommandMap mailcapCommandMap = new MailcapCommandMap();
    String[] mimeTypes = mailcapCommandMap.getMimeTypes();
    for (String mimeType : mimeTypes) {
      System.out.println(mimeType);
      CommandInfo[] commandInfos = mailcapCommandMap.getAllCommands(mimeType);
      for (CommandInfo info : commandInfos) {
        System.out.println(" " + info.getCommandName() + " : "
            + info.getCommandClass());
      }
    }
  }
}
/*
*/
java title=Example.java
image/jpeg
 view : com.sun.activation.viewers.ImageViewer
image/gif
 view : com.sun.activation.viewers.ImageViewer
text/*
 view : com.sun.activation.viewers.TextViewer
 edit : com.sun.activation.viewers.TextEditor
```

| 6.43.1. | Java activation framework |
|---|---|
| 6.43.2. | import javax.activation.CommandInfo; |
| 6.43.3. | MailcapCommandMap Demo |
