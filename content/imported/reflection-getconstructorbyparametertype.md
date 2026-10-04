---
title: Get constructor by parameter type
nav: Get constructor by paramet...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2071
source: https://web.archive.org/web/20140829084112/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getconstructorbyparametertype.htm
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
import java.lang.reflect.InvocationTargetException;
public class ConstructorTroubleAgain {
  public ConstructorTroubleAgain() {
  }
  public ConstructorTroubleAgain(Integer i) {
  }
  public ConstructorTroubleAgain(Object o) {
    out.format("Constructor passed Object%n");
  }
  public ConstructorTroubleAgain(String s) {
    out.format("Constructor passed String%n");
  }
  public static void main(String... args) {
    String argType = (args.length == 0 ? "" : args[0]);
    try {
      Class<?> c = Class.forName("ConstructorTroubleAgain");
      if ("".equals(argType)) {
        // IllegalArgumentException: wrong number of arguments
        Object o = c.getConstructor().newInstance("foo");
      } else if ("int".equals(argType)) {
        // NoSuchMethodException - looking for int, have Integer
        Object o = c.getConstructor(int.class);
      } else if ("Object".equals(argType)) {
        // newInstance() does not perform method resolution
        Object o = c.getConstructor(Object.class).newInstance("foo");
      } else {
        assert false;
      }
      // production code should handle these exceptions more gracefully
    } catch (ClassNotFoundException x) {
      x.printStackTrace();
    } catch (NoSuchMethodException x) {
      x.printStackTrace();
    } catch (InvocationTargetException x) {
      x.printStackTrace();
    } catch (InstantiationException x) {
      x.printStackTrace();
    } catch (IllegalAccessException x) {
      x.printStackTrace();
    }
  }
}
```
