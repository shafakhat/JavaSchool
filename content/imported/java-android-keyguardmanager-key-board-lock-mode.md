---
title: Android KeyguardManager key board lock mode
nav: Android KeyguardManager ke...
description: KeyguardManager mKeyguardManager = (KeyguardManager) c.getSystemService(c.KEYGUARD_SERVICE);
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20210102122033/http://www.java2s.com/ref/java/android-keyguardmanager-key-board-lock-mode.html
---
- android.app
- android.app ActivityManager KeyguardManager

## Description

```java title=Example.java
import android.app.KeyguardManager;
import android.content.Context;
publicclass Main {
    publicfinalstaticboolean isScreenLocked(Context c) {
        KeyguardManager mKeyguardManager = (KeyguardManager) c.getSystemService(c.KEYGUARD_SERVICE);
        return mKeyguardManager.inKeyguardRestrictedInputMode();
    }
}
```

PreviousNext

## Related

- Java XML Element append child
- Java XML Node get type
- Android ActivityManager get top Activity
- Android Intent send text
- Android Intent share photo
