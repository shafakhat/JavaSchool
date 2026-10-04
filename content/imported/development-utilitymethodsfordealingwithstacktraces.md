---
title: Utility methods for dealing with stack traces
nav: Utility methods for dealin...
description: /**************************************************************************************
section: Imported - java2s Archive
order: 1795
source: https://web.archive.org/web/20140829080025/http://www.java2s.com/Tutorial/Java/0120__Development/Utilitymethodsfordealingwithstacktraces.htm
---
```java title=Example.java
/**************************************************************************************
 * Copyright (c) Jonas BonŽr, Alexandre Vasseur. All rights reserved.                 *
 * http://aspectwerkz.codehaus.org                                                    *
 * ---------------------------------------------------------------------------------- *
 * The software in this package is published under the terms of the LGPL license      *
 * a copy of which has been included with this distribution in the license.txt file.  *
 **************************************************************************************/
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;
/**
 *
 * @author <a href="mailto:jboner@codehaus.org">Jonas BonŽr </a>
 */
public final class StackTraceHelper {
    /**
     * Removes the AspectWerkz specific elements from the stack trace.
     *
     * @param exception the Throwable to modify the stack trace on
     * @param className the name of the fake origin class of the exception
     */
    public static void hideFrameworkSpecificStackTrace(final Throwable exception, final String className) {
        if (exception == null) {
            throw new IllegalArgumentException("exception can not be null");
        }
        if (className == null) {
            throw new IllegalArgumentException("class name can not be null");
        }
        final List newStackTraceList = new ArrayList();
        final StackTraceElement[] stackTrace = exception.getStackTrace();
        int i;
        for (i = 1; i < stackTrace.length; i++) {
            if (stackTrace[i].getClassName().equals(className)) {
                break;
            }
        }
        for (int j = i; j < stackTrace.length; j++) {
            newStackTraceList.add(stackTrace[j]);
        }
        final StackTraceElement[] newStackTrace = new StackTraceElement[newStackTraceList.size()];
        int k = 0;
        for (Iterator it = newStackTraceList.iterator(); it.hasNext(); k++) {
            final StackTraceElement element = (StackTraceElement) it.next();
            newStackTrace[k] = element;
        }
        exception.setStackTrace(newStackTrace);
    }
}
```

| 6.23.1. | Error Handling |
|---|---|
| 6.23.2. | Types of Exceptions |
| 6.23.3. | Java's Unchecked RuntimeException Subclasses |
| 6.23.4. | Java's Checked Exceptions Defined in java.lang |
| 6.23.5. | Throwing an Exception from a Method |
| 6.23.6. | Write a catch block that handles java.lang.Exception |
| 6.23.7. | Handling Exceptions |
| 6.23.8. | Multiple catch Blocks |
| 6.23.9. | The finally Block |
| 6.23.10. | Exception Objects: stack trace |
| 6.23.11. | Defining Your Own Exceptions, Throwing Your Own Exception |
| 6.23.12. | Demonstrate exception chaining. |
| 6.23.13. | Getting the Stack Trace of an Exception |
| 6.23.14. | Put printStackTrace() into a String: redirect the StackTrace to a String with a StringWriter/PrintWriter |
| 6.23.15. | Check whether given exception is compatible with the exceptions declared in a throws clause |
| 6.23.16. | Convert an exception to a String with full stack trace |
| 6.23.17. | Get Deepest Throwable |
| 6.23.18. | Get the stack trace of the supplied exception. |
| 6.23.19. | Is Checked Exception |
| 6.23.20. | Locates a particular type of exception |
| 6.23.21. | Make a string representation of the exception |
| 6.23.22. | Print all of the thread's information and stack traces |
| 6.23.23. | Return stack trace from the passed exception as a string |
| 6.23.24. | Returns the root cause of an exception |
| 6.23.25. | Create a new Exception, setting the cause if possible. |
| 6.23.26. | Returns the output of printStackTrace as a String. |
| 6.23.27. | This program creates a custom exception type. |
| 6.23.28. | Utility methods for dealing with stack traces |
