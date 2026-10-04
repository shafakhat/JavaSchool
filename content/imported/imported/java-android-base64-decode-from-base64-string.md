---
title: Android Base64 decode from base64 String
nav: Android Base64 decode from...
description: }//fromwww.java2s.compublicstaticString decodeFromBase64(String base64Str) {
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-base64-decode-from-base64-string.html
---
- android.util
- android.util Base64

## Description

Android Base64 decode from base64 String

```java title=Example.java
import android.util.Base64;

publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        String base64Str = "";
        System.out.println(decodeFromBase64(base64Str));
    }//fromwww.java2s.compublicstaticString decodeFromBase64(String base64Str) {
        returnnewString(Base64.decode(base64Str, Base64.DEFAULT));
    }
}
```

PreviousNext

## Related

- Android PackageInfo get package version name
- Android Color random RGB value
- Android ClipboardManager set text
- Android TextView set text
- Java AWTEvent mask window event
