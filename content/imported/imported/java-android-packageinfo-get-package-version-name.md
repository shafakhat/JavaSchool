---
title: Android PackageInfo get package version name
nav: Android PackageInfo get pa...
description: try {/*fromwww.java2s.com*/String pkName = context.getPackageName();
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20210102122034/http://www.java2s.com/ref/java/android-packageinfo-get-package-version-name.html
---
- android.content.pm
- android.content.pm PackageInfo

## Description

Android PackageInfo get package version name

```java title=Example.java
import android.content.Context;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;

publicclass Main {
    publicstaticString getVersionName(Context context) {
        try {/*fromwww.java2s.com*/String pkName = context.getPackageName();
            PackageManager pkg = context.getPackageManager();
            PackageInfo info = pkg.getPackageInfo(pkName, 0);
            String versionName = info.versionName;
            return versionName;
        } catch (Exception e) {

        }
        return"";

    }
}
```

PreviousNext

## Related

- Android KeyguardManager key board lock mode
- Android Intent send text
- Android Intent share photo
- Android Color random RGB value
- Android ClipboardManager set text
