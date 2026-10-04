---
title: Is Inheritable
nav: Is Inheritable
description: //$Id: IntrospectionUtil.java 1540 2007-01-19 12:24:10Z janb $
section: Imported - java2s Archive
order: 2197
source: https://web.archive.org/web/20140829074727/http://www.java2s.com/Tutorial/Java/0125__Reflection/IsInheritable.htm
---
```java title=Example.java
//
//$Id: IntrospectionUtil.java 1540 2007-01-19 12:24:10Z janb $
//Copyright 2006 Mort Bay Consulting Pty. Ltd.
//------------------------------------------------------------------------
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//http://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
//
import java.lang.reflect.Member;
import java.lang.reflect.Modifier;
public class Utils {
  public static boolean isInheritable(Package pack, Member member) {
    if (pack == null)
      return false;
    if (member == null)
      return false;
    int modifiers = member.getModifiers();
    if (Modifier.isPublic(modifiers))
      return true;
    if (Modifier.isProtected(modifiers))
      return true;
    if (!Modifier.isPrivate(modifiers) && pack.equals(member.getDeclaringClass().getPackage()))
      return true;
    return false;
  }
}
```

| 7.13.1. | Get super class of an object |
|---|---|
| 7.13.2. | Superclass of Object is null |
| 7.13.3. | Get all methods including the inherited method. Using the getMethods(), we can only access public methods. |
| 7.13.4. | The superclass of primitive types is always null |
| 7.13.5. | Getting the Superclass of an Object |
| 7.13.6. | Is Inheritable |
