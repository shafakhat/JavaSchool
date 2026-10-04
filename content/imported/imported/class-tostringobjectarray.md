---
title: toString(Object[] array)
nav: toString(Object[] array)
description: /* ------------------------------------------------------------------------
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20091030212836/http://www.java2s.com:80/Code/Java/Class/toStringObjectarray.htm
---
```java title=Example.java
/* ------------------------------------------------------------------------
 * $Id: ToString.java,v 1.1 2005/07/23 12:56:13 tpv Exp $
 * Copyright 2005 Tim Vernum
 * ------------------------------------------------------------------------
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ------------------------------------------------------------------------
 */
/**
 * @version $Revision: 1.1 $
 */
public final class ToString
{
    public static String toString(Object[] array)
    {
        StringBuffer buffer = new StringBuffer();
        Class type = array.getClass().getComponentType();
        if (type != Object.class)
        {
            buffer.append(type.getName());
        }
        if (array.length == 0)
        {
            buffer.append("[0]");
        }
        else
        {
            buffer.append("[");
            buffer.append(array.length);
            buffer.append("]{");
            for (int i = 0; i < array.length; i++)
            {
                buffer.append(array[i]);
                buffer.append(',');
            }
            buffer.setCharAt(buffer.length() - 1, '}');
        }
        return buffer.toString();
    }
    private ToString()
    {
        // Utility class
    }
}
```

1.  ShowToString -- demo program to show default toString methods
---  ---
2.  ToString -- demo program to show a toString method
3.  Demonstrate toString() without an override
4.  To String Demo
5.  Reflection based toString() utilities
6.  Use a generic toString()
7.  Constructs pretty string representation of object value
8.  Null Safe To String
9.  Array To String
10.  Gets the toString of an Object returning an empty string ("") if null input.
11.  Gets the toString that would be produced by Object if a class did not override toString itself.
