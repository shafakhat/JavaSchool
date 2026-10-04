---
title: Android ClipboardManager set text
nav: Android ClipboardManager s...
description: ClipboardManager cbm = (ClipboardManager) ctx.getSystemService(Context.CLIPBOARD_SERVICE);
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-clipboardmanager-set-text.html
---
- android.text
- android.text ClipboardManager

## Description

```java title=Example.java
import android.app.Activity;
import android.content.Context;
import android.text.ClipboardManager;
publicclass Main{
    publicstaticvoid copyText(Activity ctx, String text) {
        ClipboardManager cbm = (ClipboardManager) ctx.getSystemService(Context.CLIPBOARD_SERVICE);
        cbm.setText(text);
    }
}
```

PreviousNext

## Related

- Android Intent share photo
- Android PackageInfo get package version name
- Android Color random RGB value
- Android Base64 decode from base64 String
- Android TextView set text
