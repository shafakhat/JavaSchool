---
title: Convert an exception to a String with full stack trace
nav: Convert an exception to a ...
description: /**********************************************************************
section: Imported - java2s Archive
order: 1785
source: https://web.archive.org/web/20140829075944/http://www.java2s.com/Tutorial/Java/0120__Development/ConvertanexceptiontoaStringwithfullstacktrace.htm
---
```java title=Example.java
/**********************************************************************
Copyright (c) 2003 Andy Jefferson and others. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Contributors:
2003 Erik Bengtson - moved replaceAll from Column class to here
2004 Andy Jefferson - moved intArrayToString, booleanArrayToString from SM
2007 Xuan Baldauf - toJVMIDString hex fix
    ...
**********************************************************************/
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.URLDecoder;
import java.util.Collection;
import java.util.Iterator;
import java.util.Properties;
import java.util.StringTokenizer;
import java.util.jar.JarFile;
/**
 * Utilities for String manipulation.
 *
 * @version $Revision: 1.23 $
 **/
public class StringUtils
{
  /**
   * @param ex the exception
   * @return a String with the full stacktrace error text
   */
  public static String getStringFromStackTrace(Throwable ex)
  {
      if (ex==null)
      {
          return "";
      }
      StringWriter str = new StringWriter();
      PrintWriter writer = new PrintWriter(str);
      try
      {
          ex.printStackTrace(writer);
          return str.getBuffer().toString();
      }
      finally
      {
          try
          {
              str.close();
              writer.close();
          }
          catch (IOException e)
          {
              //ignore
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
