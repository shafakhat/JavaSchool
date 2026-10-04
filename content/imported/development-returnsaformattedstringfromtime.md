---
title: Returns a formatted String from time
nav: Returns a formatted String...
description: * Copyright (C) 2004-2008 Jive Software. All rights reserved.
section: Imported - java2s Archive
order: 1732
source: https://web.archive.org/web/20140829080700/http://www.java2s.com/Tutorial/Java/0120__Development/ReturnsaformattedStringfromtime.htm
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
 */
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.BreakIterator;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
/**
 * Utility class to peform common String manipulation algorithms.
 */
public class StringUtils {
    // Constants used by escapeHTMLTags
    private static final char[] QUOTE_ENCODE = "&quot;".toCharArray();
    private static final char[] AMP_ENCODE = "&amp;".toCharArray();
    private static final char[] LT_ENCODE = "&lt;".toCharArray();
    private static final char[] GT_ENCODE = "&gt;".toCharArray();
    private StringUtils() {
        // Not instantiable.
    }
    /**
     *
     * @param diff the amount of elapsed time.
     * @return the formatte String.
     */
    public static String getTimeFromLong(long diff) {
        final String HOURS = "h";
        final String MINUTES = "min";
        final String SECONDS = "sec";
        final long MS_IN_A_DAY = 1000 * 60 * 60 * 24;
        final long MS_IN_AN_HOUR = 1000 * 60 * 60;
        final long MS_IN_A_MINUTE = 1000 * 60;
        final long MS_IN_A_SECOND = 1000;
        Date currentTime = new Date();
        long numDays = diff / MS_IN_A_DAY;
        diff = diff % MS_IN_A_DAY;
        long numHours = diff / MS_IN_AN_HOUR;
        diff = diff % MS_IN_AN_HOUR;
        long numMinutes = diff / MS_IN_A_MINUTE;
        diff = diff % MS_IN_A_MINUTE;
        long numSeconds = diff / MS_IN_A_SECOND;
        diff = diff % MS_IN_A_SECOND;
        long numMilliseconds = diff;
        StringBuffer buf = new StringBuffer();
        if (numHours > 0) {
            buf.append(numHours + " " + HOURS + ", ");
        }
        if (numMinutes > 0) {
            buf.append(numMinutes + " " + MINUTES);
        }
        //buf.append(numSeconds + " " + SECONDS);
        String result = buf.toString();
        if (numMinutes < 1) {
            result = "< 1 minute";
        }
        return result;
    }
}
```

| 6.20.1. | Compute and display elapsed time of an operation |
|---|---|
| 6.20.2. | Get system time using System class |
| 6.20.3. | Get elapsed time in milliseconds |
| 6.20.4. | Get elapsed time in seconds |
| 6.20.5. | Get elapsed time in minutes |
| 6.20.6. | Get elapsed time in hours |
| 6.20.7. | Get elapsed time in days |
| 6.20.8. | Returns a String in the format Xhrs, Ymins, Z sec, for the time difference between two times |
| 6.20.9. | Returns a formatted String from time |
| 6.20.10. | Convert milliseconds to readable string |
