---
title: Android Intent share photo
nav: Android Intent share photo
description: }//www.java2s.compublicstaticvoid sharePhoto(final Activity activity, String photoUri) {
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-intent-share-photo.html
---
- android.content
- android.content Intent

## Description

Android Intent share photo

```java title=Example.java
import android.app.Activity;

import android.content.Intent;

import android.net.Uri;

import java.io.File;

publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
    }//www.java2s.compublicstaticvoid sharePhoto(final Activity activity, String photoUri) {
        Intent shareIntent = new Intent(Intent.ACTION_SEND);
        File file = newFile(photoUri);
        shareIntent.putExtra(Intent.EXTRA_STREAM, Uri.fromFile(file));
        shareIntent.setType("image/jpeg");
        activity.startActivity(Intent.createChooser(shareIntent, activity.getTitle()));
    }
}
```

PreviousNext

## Related

- Android ActivityManager get top Activity
- Android KeyguardManager key board lock mode
- Android Intent send text
- Android PackageInfo get package version name
- Android Color random RGB value
