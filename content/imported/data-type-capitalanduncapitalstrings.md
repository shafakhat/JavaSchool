---
title: Capital and uncapital strings
nav: Capital and uncapital stri...
description: /* ------------------------------------------------------------------------
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20100412210647/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Capitalanduncapitalstrings.htm
---
```java title=Example.java
/* ------------------------------------------------------------------------
 * $Id: StringUtil.java,v 1.1 2005/12/26 12:59:25 tpv Exp $
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
public final class StringUtil
{
    private StringUtil()
    {
        // Static utility class
    }
    public static String uncaps(String string)
    {
        if (string.length() == 0)
        {
            return string;
        }
        char ch = string.charAt(0);
        if (Character.isUpperCase(ch))
        {
            ch = Character.toLowerCase(ch);
            return ch + string.substring(1);
        }
        return string;
    }
    public static String caps(String string)
    {
        if (string.length() == 0)
        {
            return string;
        }
        char ch = string.charAt(0);
        if (Character.isLowerCase(ch))
        {
            ch = Character.toUpperCase(ch);
            return ch + string.substring(1);
        }
        return string;
    }
    public static boolean isBlank(String value)
    {
        return value == null || value.length() == 0;
    }
    public static boolean isBlankOrSpace(String value)
    {
        return isBlank(value) || isBlank(value.trim());
    }
}
```
