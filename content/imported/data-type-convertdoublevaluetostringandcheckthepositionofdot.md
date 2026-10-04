---
title: Convert double value to string and check the position of dot
nav: Convert double value to st...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 1414
source: https://web.archive.org/web/20140829085629/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertdoublevaluetostringandcheckthepositionofdot.htm
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
 */
public class ToStringDemo {
  public static void main(String[] args) {
    double d = 858.48;
    String s = Double.toString(d);
    int dot = s.indexOf('.');
    System.out.println(dot + " digits before decimal point.");
    System.out.println((s.length() - dot - 1) + " digits after decimal point.");
  }
}
```

| 2.12.1. | Java double: double is 64 bit double precision type and used when fractional precision calculation is required. |
|---|---|
| 2.12.2. | How to declare floating-point variables: double |
| 2.12.3. | Create a Double object using one of the below given constructors |
| 2.12.4. | Use Double constructor to convert double primitive type to a Double object. |
| 2.12.5. | Double value |
| 2.12.6. | Demonstrate isInfinite() and isNaN() |
| 2.12.7. | Java Double isInfinite |
| 2.12.8. | Convert double value to string and check the position of dot |
| 2.12.9. | Java Double isNaN method |
| 2.12.10. | Java Double compare example |
| 2.12.11. | Format double with System.out.format |
| 2.12.12. | Trigonometric Demo |
| 2.12.13. | Decimal Format |
| 2.12.14. | Min and Max values of data type double |
| 2.12.15. | Convert java Double to numeric primitive data types |
| 2.12.16. | Convert Java String to Double |
| 2.12.17. | Convert from double to String |
| 2.12.18. | Convert from String to double |
| 2.12.19. | Converting a String to a double type Number |
| 2.12.20. | Use toString method of Double class to convert Double into String. |
| 2.12.21. | Compare Two Java double Arrays |
| 2.12.22. | Ternary operator on double value |
| 2.12.23. | Read double value from console and check the format |
