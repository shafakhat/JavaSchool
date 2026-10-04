---
title: Android Color random RGB value
nav: Android Color random RGB v...
description: Imported from the java2s.com archive: Android Color random RGB value
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/android-color-random-rgb-value.html
---
- android.graphics
- android graphics Color

## Description

```java title=Example.java
import android.graphics.Color;
import java.util.Random;
public class Main {
    public static void main(String[] argv) throws Exception {
        System.out.println(randomRGB());
    }public static int randomRGB() {
        String r, g, b;
        Random random = new Random();
        r = Integer.toHexString(random.nextInt(256)).toUpperCase();
        g = Integer.toHexString(random.nextInt(256)).toUpperCase();
        b = Integer.toHexString(random.nextInt(256)).toUpperCase();
        r = r.length() == 1 ? "0" + r : r;
        g = g.length() == 1 ? "0" + g : g;
        b = b.length() == 1 ? "0" + b : b;
        return Color.parseColor("#" + (r + g + b));
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
