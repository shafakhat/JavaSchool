---
title: Invoke method with wrong parameters
nav: Invoke method with wrong p...
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2135
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0125__Reflection/Invokemethodwithwrongparameters.htm
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
 */import java.lang.reflect.Method;
public class MethodTroubleToo {
  public void ping() {
    System.out.format("PONG!%n");
  }
  public static void main(String... args) {
    try {
      MethodTroubleToo mtt = new MethodTroubleToo();
      Method m = MethodTroubleToo.class.getMethod("ping");
      switch (Integer.parseInt(args[0])) {
      case 0:
        m.invoke(mtt); // works
 break;
      case 1:
        m.invoke(mtt, null); // works (expect compiler warning)
 break;
      case 2:
        Object arg2 = null;
        m.invoke(mtt, arg2); // IllegalArgumentException
 break;
      case 3:
        m.invoke(mtt, new Object[0]); // works
 break;
      case 4:
        Object arg4 = new Object[0];
        m.invoke(mtt, arg4); // IllegalArgumentException
 break;
      default:
        System.out.format("Test not found%n");
      }
      // production code should handle these exceptions more gracefully
    } catch (Exception x) {
      x.printStackTrace();
    }
  }
}
```

| 7.5.1. | List methods of a class using Reflection |
|---|---|
| 7.5.2. | Design your own class loader |
| 7.5.3. | Get method my parameters |
| 7.5.4. | Show public methods. |
| 7.5.5. | Method Inspector |
| 7.5.6. | Invoke methods of an object using reflection |
| 7.5.7. | Call a member function to get the value |
| 7.5.8. | Prints out the declared methods on java.lang.Number |
| 7.5.9. | Demonstrates how to get simple method information |
| 7.5.10. | Prints out the declared methods on java.lang.Object |
| 7.5.11. | Demonstrates how to get specific method information |
| 7.5.12. | Get the current method name |
| 7.5.13. | Get the current method name With JDK1.5 |
| 7.5.14. | Get method from a class by name |
| 7.5.15. | Get super class and all its declared methods |
| 7.5.16. | Invoke a method with parameter |
| 7.5.17. | Call a class method with 2 arguments |
| 7.5.18. | Call all possible exceptions during method invocation with reflection |
| 7.5.19. | get Declared Method by name and parameter type |
| 7.5.20. | Getting the Methods of a Class Object: By obtaining a list of all declared methods |
| 7.5.21. | Getting the Methods of a Class Object: By obtaining a list of all public methods, both declared and inherited. |
| 7.5.22. | Getting the Methods of a Class Object: By obtaining a particular Method object. |
| 7.5.23. | Invoke method with wrong parameters |
| 7.5.24. | Checks whether the specified class contains a method matching the specified name. |
| 7.5.25. | Find method |
| 7.5.26. | Returns method with the specified name |
| 7.5.27. | Sorts methods according to their name, number of parameters, and parameter types. |
| 7.5.28. | Contains Same Method Signature |
