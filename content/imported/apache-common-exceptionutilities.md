---
title: Exception Utilities
nav: Exception Utilities
description: Imported from the java2s.com archive: Exception Utilities
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20061027010112/http://www.java2s.com/Code/Java/Apache-Common/ExceptionUtilities.htm
---
Exception Utilities

```java title=Example.java
import org.apache.commons.lang.exception.ExceptionUtils;
import org.apache.commons.lang.exception.NestableException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
public class ExceptionUtilsV1 {
  public static void main(String args[]) {
    try {
      loadFile();
    } catch(Exception e) {
      e.printStackTrace();
    }
  }
  public static void loadFile() throws Exception {
    try {
      FileInputStream fis =
       new FileInputStream(new File("nosuchfile"));
    } catch (FileNotFoundException fe) {
      throw new NestableException(fe);
    }
  }
}
```

Download: ExceptionUtilsV1.zip ( 1,004 K )
Related examples in the same category
