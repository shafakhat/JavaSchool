---
title: Using the Desktop class to launch a URL with default browser
nav: Using the Desktop class to...
description: Imported from the java2s.com archive: Using the Desktop class to launch a URL with default browser
section: Imported - java2s Archive
order: 1876
source: https://web.archive.org/web/20140829090208/http://www.java2s.com/Tutorial/Java/0120__Development/UsingtheDesktopclasstolaunchaURLwithdefaultbrowser.htm
---
```java title=Example.java
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
public class UsingDesltopClassToLaunch {
  public static void main(String[] a) {
    try {
      URI uri = new URI("http:");
      Desktop desktop = null;
      if (Desktop.isDesktopSupported()) {
        desktop = Desktop.getDesktop();
      }
      if (desktop != null)
        desktop.browse(uri);
    } catch (IOException ioe) {
      ioe.printStackTrace();
    } catch (URISyntaxException use) {
      use.printStackTrace();
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
