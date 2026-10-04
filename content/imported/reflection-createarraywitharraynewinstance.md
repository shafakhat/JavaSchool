---
title: Create array with Array.newInstance
nav: Create array with Array.ne...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2161
source: https://web.archive.org/web/20140829091932/http://www.java2s.com/Tutorial/Java/0125__Reflection/CreatearraywithArraynewInstance.htm
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
import static java.lang.System.out;
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class ArrayCreator {
  private static String s = "java.math.BigInteger bi[] = { 123, 234, 345 }";
  private static Pattern p = Pattern
      .compile("^\\s*(\\S+)\\s*\\w+\\[\\].*\\{\\s*([^}]+)\\s*\\}");
  public static void main(String... args) {
    Matcher m = p.matcher(s);
    if (m.find()) {
      String cName = m.group(1);
      String[] cVals = m.group(2).split("[\\s,]+");
      int n = cVals.length;
      try {
        Class<?> c = Class.forName(cName);
        Object o = Array.newInstance(c, n);
        for (int i = 0; i < n; i++) {
          String v = cVals[i];
          Constructor ctor = c.getConstructor(String.class);
          Object val = ctor.newInstance(v);
          Array.set(o, i, val);
        }
        Object[] oo = (Object[]) o;
        out.format("%s[] = %s%n", cName, Arrays.toString(oo));
        // production code should handle these exceptions more gracefully
      } catch (ClassNotFoundException x) {
        x.printStackTrace();
      } catch (NoSuchMethodException x) {
        x.printStackTrace();
      } catch (IllegalAccessException x) {
        x.printStackTrace();
      } catch (InstantiationException x) {
        x.printStackTrace();
      } catch (InvocationTargetException x) {
        x.printStackTrace();
      }
    }
  }
}
```

| 7.9.1. | Determining If an Object Is an Array |
|---|---|
| 7.9.2. | Demonstrates the use of the Array class |
| 7.9.3. | Create array with Array.newInstance |
| 7.9.4. | Is field an array |
| 7.9.5. | Create integer array with Array.newInstance |
| 7.9.6. | Use Array.setInt to fill an array |
| 7.9.7. | Use Array.setShort and Array.setLong |
| 7.9.8. | Getting the Length and Dimensions of an Array Object |
| 7.9.9. | Getting the Component Type of an Array Object |
| 7.9.10. | Array reflection and two dimensional array |
| 7.9.11. | class name for double and float array |
| 7.9.12. | Returns the length of the specified array, can deal with Object arrays and with primitive arrays. |
