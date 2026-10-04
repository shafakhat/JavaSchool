---
title: To change a date/time component, use its set method
nav: To change a date/time comp...
description: Imported from the java2s.com archive: To change a date/time component, use its set method
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Tochangeadatetimecomponentuseitssetmethodpublicvoidsetintfieldintvalue.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    calendar.set(Calendar.MONTH, Calendar.DECEMBER);
  }
}
```
