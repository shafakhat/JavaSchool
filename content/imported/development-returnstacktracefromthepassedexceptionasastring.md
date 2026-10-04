---
title: Return stack trace from the passed exception as a string
nav: Return stack trace from th...
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1815
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0120__Development/Returnstacktracefromthepassedexceptionasastring.htm
---
```java title=Example.java
/*
 * Copyright (C) 2001-2003 Colin Bell
 * colbell@users.sourceforge.net
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */import java.io.*;
import java.text.NumberFormat;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 * General purpose utilities functions.
 *
 * @author <A HREF="mailto:colbell@users.sourceforge.net">Colin Bell</A>
 */public class Utilities
{
   /**
    * Return the stack trace from the passed exception as a string
    *
    * @param  th  The exception to retrieve stack trace for.
    */ public static String getStackTrace(Throwable th)
   {
      if (th == null)
      {
         throw new IllegalArgumentException("Throwable == null");
      }
      StringWriter sw = new StringWriter();
      try
      {
         PrintWriter pw = new PrintWriter(sw);
         try
         {
            th.printStackTrace(pw);
            return sw.toString();
         }
         finally
         {
            pw.close();
         }
      }
      finally
      {
         try
         {
            sw.close();
         }
         catch (IOException ex)
         {
         }
      }
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
