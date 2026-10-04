---
title: Android Intent send text
nav: Android Intent send text
description: }/*fromwww.java2s.com*/publicstaticvoid SendTo(Context ctx, String sendWhat) {
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-intent-send-text.html
---
- android.content
- android.content Intent

## Description

```java title=Example.java
import android.content.Context;
import android.content.Intent;
publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
    }publicstaticvoid SendTo(Context ctx, String sendWhat) {
        Intent shareIntent = new Intent(Intent.ACTION_SEND);
        shareIntent.setType("text/plain");
        shareIntent.putExtra(Intent.EXTRA_TEXT, sendWhat);
        ctx.startActivity(shareIntent);
    }
}
```

PreviousNext

## Related

- Java XML Node get type
- Android ActivityManager get top Activity
- Android KeyguardManager key board lock mode
- Android Intent share photo
- Android PackageInfo get package version name
