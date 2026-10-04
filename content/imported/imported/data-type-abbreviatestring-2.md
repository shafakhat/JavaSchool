---
title: Abbreviate string
nav: Abbreviate string
description: * Copyright (C) 2004-2008 Jive Software. All rights reserved.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Abbreviatestring.htm
---
```java title=Example.java
/**
 * $Revision: 10205 $
 * $Date: 2008-04-11 15:48:27 -0700 (Fri, 11 Apr 2008) $
 *
 * Copyright (C) 2004-2008 Jive Software. All rights reserved.
 *
 * This software is published under the terms of the GNU Public License (GPL),
 * a copy of which is included in this distribution, or a commercial license
 * agreement with Jive.
 */import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.BreakIterator;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Utility class to peform common String manipulation algorithms.
 */publicclass StringUtils {

    // Constants used by escapeHTMLTags
privatestaticfinalchar[] QUOTE_ENCODE = "&quot;".toCharArray();
    privatestaticfinalchar[] AMP_ENCODE = "&amp;".toCharArray();
    privatestaticfinalchar[] LT_ENCODE = "&lt;".toCharArray();
    privatestaticfinalchar[] GT_ENCODE = "&gt;".toCharArray();

    private StringUtils() {
        // Not instantiable.
    }

    /**
     * Abbreviates a string to a specified length and then adds an ellipsis
     * if the input is greater than the maxWidth. Example input:
     * <pre>
     *      user1@jivesoftware.com/home
     * </pre>
     * and a maximum length of 20 characters, the abbreviate method will return:
     * <pre>
     *      user1@jivesoftware.c...
     * </pre>
     * @param str the String to abbreviate.
     * @param maxWidth the maximum size of the string, minus the ellipsis.
     * @return the abbreviated String, or <tt>null</tt> if the string was <tt>null</tt>.
     */publicstatic String abbreviate(String str, int maxWidth) {
        if (null == str) {
            return null;
        }

        if (str.length() <= maxWidth) {
            return str;
        }

        return str.substring(0, maxWidth) + "...";
    }

}
```
