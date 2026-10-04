---
title: Format long with System.out.format
nav: Format long with System.ou...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormatlongwithSystemoutformat.htm
---
```java title=Example.java
/*
 * Copyright (c) 1995 - 2008 Sun Microsystems, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Sun Microsystems nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */import java.util.Calendar;
import java.util.Locale;
public class TestFormat {
  public static void main(String[] args) {
    long n = 461012;
    System.out.format("%d%n", n);
    System.out.format("%08d%n", n);
    System.out.format("%+8d%n", n);
    System.out.format("%,8d%n", n);
    System.out.format("%+,8d%n%n", n);
    double pi = Math.PI;
    System.out.format("%f%n", pi);
    System.out.format("%.3f%n", pi);
    System.out.format("%10.3f%n", pi);
    System.out.format("%-10.3f%n", pi);
    System.out.format(Locale.FRANCE, "%-10.4f%n%n", pi);
    Calendar c = Calendar.getInstance();
    System.out.format("%tB %te, %tY%n", c, c, c);
    System.out.format("%tl:%tM %tp%n", c, c, c);
    System.out.format("%tD%n", c);
  }
}
```

| 2.8.1. | Long Integer Literal |
|---|---|
| 2.8.2. | Create a Long object |
| 2.8.3. | Add two long integers, checking for overflow. |
| 2.8.4. | Multiply two long integers, checking for overflow. |
| 2.8.5. | Subtract two long integers, checking for overflow. |
| 2.8.6. | Convert Long to numeric primitive data types example |
| 2.8.7. | Convert long primitive to Long object Example |
| 2.8.8. | Compute distance light travels using long variables |
| 2.8.9. | Java long Example: long is 64 bit signed type |
| 2.8.10. | Min and Max values of datatype long |
| 2.8.11. | Gets the maximum of three long values. |
| 2.8.12. | Gets the minimum of three long values. |
| 2.8.13. | Convert Java String to Long example |
| 2.8.14. | Use toString method of Long class to convert Long into String. |
| 2.8.15. | Convert from long to String |
| 2.8.16. | Convert from String to long |
| 2.8.17. | A utility class for converting a long into a human readable string. |
| 2.8.18. | Java Sort long Array Example |
| 2.8.19. | Compare Two Java long Arrays Example |
| 2.8.20. | Format long with System.out.format |
