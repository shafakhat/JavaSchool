---
title: Android Color random RGB value
nav: Android Color random RGB v...
description: Imported from the java2s.com archive: Android Color random RGB value
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-color-random-rgb-value.html
---
- android.graphics
- android graphics Color

## Description

```java title=Example.java
import android.graphics.Color;
import java.util.Random;
publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        System.out.println(randomRGB());
    }publicstaticint randomRGB() {
        String r, g, b;
        Random random = newRandom();
        r = Integer.toHexString(random.nextInt(256)).toUpperCase();
        g = Integer.toHexString(random.nextInt(256)).toUpperCase();
        b = Integer.toHexString(random.nextInt(256)).toUpperCase();
        r = r.length() == 1 ? "0" + r : r;
        g = g.length() == 1 ? "0" + g : g;
        b = b.length() == 1 ? "0" + b : b;
        returnColor.parseColor("#" + (r + g + b));
    }
}
```

PreviousNext

## Related

- Android Intent send text
- Android Intent share photo
- Android PackageInfo get package version name
- Android ClipboardManager set text
- Android Base64 decode from base64 String
