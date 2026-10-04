---
title: Parse with a custom format
nav: Parse with a custom format
description: Format formatter = new SimpleDateFormat("HH:mm:ss Z", Locale.CANADA);
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829090700/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parsewithacustomformat.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("HH:mm:ss Z", Locale.CANADA);
    Date date = (Date) formatter.parseObject("21:44:07 Heure normale du Pacifique");
  }
}
```
