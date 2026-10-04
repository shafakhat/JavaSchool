---
title: A demo for SuppressWarnings
nav: A demo for SuppressWarnings
description: Uses the SuppressWarnings annotation type to prevent the compiler from issuing unchecked and fallthrough warnings
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/AdemoforSuppressWarningsuncheckedandfallthroughwarnings.htm
---
Uses the SuppressWarnings annotation type to prevent the compiler from issuing unchecked and fallthrough warnings

```java title=Example.java
import java.io.File;
import java.io.Serializable;
import java.util.ArrayList;
@SuppressWarnings (value={"unchecked", "serial"})
publicclass SuppressWarningsTest implements Serializable {
    publicvoid openFile () {
        ArrayList a = new ArrayList ();
        File file = newFile ("X:/java/doc.txt");
    }
}
```
