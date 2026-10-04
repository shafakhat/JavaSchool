---
title: Validate
nav: Validate
description: // Validate.isTrue(i > 40, "Invalid value: ", i); // throws custom Exception
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20071105011704/http://www.java2s.com:80/Code/Java/Apache-Common/Validateistruenotemptynonullelement.htm
---
Validate: is true, not empty, no null element

```java title=Example.java
import org.apache.commons.lang.Validate;
import java.util.List;
import java.util.ArrayList;
public class ValidateExampleV1 {
  public static void main(String args[]) {
    int i = 35;
    Validate.isTrue(i > 30); // Passes ok
    // Validate.isTrue(i > 40, "Invalid value: ", i); // throws custom Exception
    List data = new ArrayList();
    // Validate.notEmpty(data, "Collection cannot be empty"); // throws custom Exception
    data.add(null);
    Validate.noNullElements(data, "Collection contains null elements"); // throws custom Exception
  }
}
```

| BeanUtilsValidateExampleV1.zip( 1,004 k) | w_ww___.__j_a__va___2s_._com___
