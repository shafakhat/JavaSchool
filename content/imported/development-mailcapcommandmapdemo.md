---
title: MailcapCommandMap Demo
nav: MailcapCommandMap Demo
description: MailcapCommandMap mailcapCommandMap = new MailcapCommandMap();
section: Imported - java2s Archive
order: 1931
source: https://web.archive.org/web/20140829083856/http://www.java2s.com/Tutorial/Java/0120__Development/MailcapCommandMapDemo.htm
---
```java title=Example.java
import javax.activation.CommandInfo;
import javax.activation.MailcapCommandMap;
public class MailcapCommandMapDemo2 {
  public static void main(String[] args) {
    MailcapCommandMap mailcapCommandMap = new MailcapCommandMap();
    String mailcap = "text/plain;; " + "x-java-content-handler=beans.TextHandler;"
        + "x-java-view=beans.TextViewer;" + "x-java-edit=beans.TextEditor";
    mailcapCommandMap.addMailcap(mailcap);
    // Get all MIME types
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
text/plain
 content-handler : beans.TextHandler
 view : beans.TextViewer
 edit : beans.TextEditor
 view : com.sun.activation.viewers.TextViewer
 edit : com.sun.activation.viewers.TextEditor
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
