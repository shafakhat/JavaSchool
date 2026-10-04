---
title: Catch InvocationTargetException
nav: Catch InvocationTargetExce...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2144
source: https://web.archive.org/web/20140829075303/http://www.java2s.com/Tutorial/Java/0125__Reflection/CatchInvocationTargetException.htm
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
import static java.lang.System.err;
import static java.lang.System.out;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Type;
import java.util.Locale;
public class Deet<T> {
  private boolean testDeet(Locale l) {
    // getISO3Language() may throw a MissingResourceException
    out.format("Locale = %s, ISO Language Code = %s%n", l.getDisplayName(), l
        .getISO3Language());
    return true;
  }
  private int testFoo(Locale l) {
    return 0;
  }
  private boolean testBar() {
    return true;
  }
  public static void main(String... args) {
    if (args.length != 4) {
      err.format("Usage: java Deet <classname> <langauge> <country> <variant>%n");
      return;
    }
    try {
      Class<?> c = Class.forName(args[0]);
      Object t = c.newInstance();
      Method[] allMethods = c.getDeclaredMethods();
      for (Method m : allMethods) {
        String mname = m.getName();
        if (!mname.startsWith("test")|| (m.getGenericReturnType() != boolean.class)) {
          continue;
        }
        Type[] pType = m.getGenericParameterTypes();
        if ((pType.length != 1)|| Locale.class.isAssignableFrom(pType[0].getClass())) {
          continue;
        }
        out.format("invoking %s()%n", mname);
        try {
          m.setAccessible(true);
          Object o = m.invoke(t, new Locale(args[1], args[2], args[3]));
          out.format("%s() returned %b%n", mname, (Boolean) o);
          // Handle any exceptions thrown by method to be invoked.
        } catch (InvocationTargetException x) {
          Throwable cause = x.getCause();
          err.format("invocation of %s failed: %s%n", mname, cause.getMessage());
        }
      }
      // production code should handle these exceptions more gracefully
    } catch (ClassNotFoundException x) {
      x.printStackTrace();
    } catch (InstantiationException x) {
      x.printStackTrace();
    } catch (IllegalAccessException x) {
      x.printStackTrace();
    }
  }
}
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
