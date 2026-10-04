---
title: Android ActivityManager get top Activity
nav: Android ActivityManager ge...
description: }/*fromwww.java2s.com*/publicstaticboolean isTopActivity(Context context, String activityClassName) {
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20210102122033/http://www.java2s.com/ref/java/android-activitymanager-get-top-activity.html
---
- android.app
- android.app ActivityManager KeyguardManager

## Description

```java title=Example.java
import android.app.ActivityManager;
import android.app.ActivityManager.RunningTaskInfo;

import android.content.Context;

import java.util.List;

publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
    }/*fromwww.java2s.com*/publicstaticboolean isTopActivity(Context context, String activityClassName) {
        List<RunningTaskInfo> tasksInfo = ((ActivityManager) context.getSystemService(Context.ACTIVITY_SERVICE))
                .getRunningTasks(1);
        if (tasksInfo.size() > 0) {
            if (activityClassName.equals(tasksInfo.get(0).topActivity.getClassName())) {
                return true;
            }
        }
        return false;
    }

    publicstaticboolean isTopActivity(Context context) {
        String activityName = context.getClass().getName();
        return isTopActivity(context, activityName);
    }
}
```

PreviousNext

## Related

- Java XML Element get text content
- Java XML Element append child
- Java XML Node get type
- Android KeyguardManager key board lock mode
- Android Intent send text
