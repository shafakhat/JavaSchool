---
title: Sorts methods according to their name, number of parameters, and parameter types.
nav: Sorts methods according to...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 2120
source: https://web.archive.org/web/20140829092207/http://www.java2s.com/Tutorial/Java/0125__Reflection/Sortsmethodsaccordingtotheirnamenumberofparametersandparametertypes.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import java.lang.reflect.Method;
import java.util.Comparator;
/**
 * Sorts methods according to their name, number of parameters, and parameter
 * types.
 */
public class MethodComparator implements Comparator<Method> {
    public int compare(Method m1, Method m2) {
        int val = m1.getName().compareTo(m2.getName());
        if (val == 0) {
            val = m1.getParameterTypes().length - m2.getParameterTypes().length;
            if (val == 0) {
                Class[] types1 = m1.getParameterTypes();
                Class[] types2 = m2.getParameterTypes();
                for (int i = 0; i < types1.length; i++) {
                    val = types1[i].getName().compareTo(types2[i].getName());
                    if (val != 0) {
                        break;
                    }
                }
            }
        }
        return val;
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
