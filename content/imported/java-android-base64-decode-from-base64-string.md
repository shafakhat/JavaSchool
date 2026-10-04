---
title: Android Base64 decode from base64 String
nav: Android Base64 decode from...
description: }//from w ww . j ava2s.c om public static String decodeFromBase64(String base64Str) {
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/android-base64-decode-from-base64-string.html
---
- android.util
- android.util Base64

## Description

```java title=Example.java
import android.util.Base64;
public class Main {
    public static void main(String[] argv) throws Exception {
        String base64Str = "";
        System.out.println(decodeFromBase64(base64Str));
    }public static String decodeFromBase64(String base64Str) {
        return new String(Base64.decode(base64Str, Base64.DEFAULT));
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
