---
title: Invoke the default editor to edit a file
nav: Invoke the default editor ...
description: Imported from the java2s.com archive: Invoke the default editor to edit a file
section: Imported - java2s Archive
order: 1877
source: https://web.archive.org/web/20140829090243/http://www.java2s.com/Tutorial/Java/0120__Development/Invokethedefaulteditortoeditafile.htm
---
```java title=Example.java
import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
public class Test {
  public static void main(String[] a) {
    try {
      Desktop desktop = null;
      if (Desktop.isDesktopSupported()) {
        desktop = Desktop.getDesktop();
      }
       desktop.edit(new File("c:\\a.txt"));
    } catch (IOException ioe) {
      ioe.printStackTrace();
    }
  }
}
```

| 6.39.1. | Using the Desktop class to launch a URL with default browser |
|---|---|
| 6.39.2. | Invoke the default editor to edit a file |
| 6.39.3. | Using the system default setting to open a file |
| 6.39.4. | Open a office word file with Java |
| 6.39.5. | Using system default printer to print a file out |
| 6.39.6. | Send out email |
| 6.39.7. | Open Mail client |
| 6.39.8. | Desktop Help Applications |
