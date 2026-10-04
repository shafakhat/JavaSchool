---
title: Removes newline, carriage return and tab characters from a string
nav: Removes newline, carriage ...
description: /**************************************************************************************
section: Imported - java2s Archive
order: 1163
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removesnewlinecarriagereturnandtabcharactersfromastring.htm
---
```java title=Example.java
/**************************************************************************************
 * Copyright (c) Jonas Bonr, Alexandre Vasseur. All rights reserved.                 *
 * http://aspectwerkz.codehaus.org                                                    *
 * ---------------------------------------------------------------------------------- *
 * The software in this package is published under the terms of the LGPL license      *
 * a copy of which has been included with this distribution in the license.txt file.  *
 **************************************************************************************/import java.util.List;
import java.util.ArrayList;
/**
 * Utility methods for strings.
 *
 * @author <a href="mailto:jboner@codehaus.org">Jonas Bonr </a>
 */public class Strings {
    /**
     *
     * @param toBeEscaped string to escape
     * @return the escaped string
     */ public static String removeFormattingCharacters(final String toBeEscaped) {
        StringBuffer escapedBuffer = new StringBuffer();
        for (int i = 0; i < toBeEscaped.length(); i++) {
            if ((toBeEscaped.charAt(i) != '\n') && (toBeEscaped.charAt(i) != '\r') && (toBeEscaped.charAt(i) != '\t')) {
                escapedBuffer.append(toBeEscaped.charAt(i));
            }
        }
        String s = escapedBuffer.toString();
        return s;//
 // Strings.replaceSubString(s, "\"", "")
    }
}
```
