---
title: Open Mail client
nav: Open Mail client
description: Imported from the java2s.com archive: Open Mail client
section: Imported - java2s Archive
order: 1886
source: https://web.archive.org/web/20140829090017/http://www.java2s.com/Tutorial/Java/0120__Development/OpenMailclient.htm
---
```java title=Example.java
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
public class Test {
  public static void main(String[] a)throws Exception {
      Desktop desktop = null;
      if (Desktop.isDesktopSupported()) {
        desktop = Desktop.getDesktop();
      }
       desktop.mail();
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
