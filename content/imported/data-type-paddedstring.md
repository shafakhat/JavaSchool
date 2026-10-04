---
title: Padded String
nav: Padded String
description: /**********************************************************************
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829080859/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PaddedString.htm
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
  /** Utility to return a left-aligned version of a string padded to the
   * number of characters specified.
   * @param input The input string
   * @param length The length desired
   * @return The updated string
   **/
  public static String leftAlignedPaddedString(String input,int length)
  {
      if (length <= 0)
      {
          return null;
      }
      StringBuffer output=new StringBuffer();
      char         space=' ';
      if (input != null)
      {
          if (input.length() < length)
          {
              output.append(input);
              for (int i=input.length();i<length;i++)
              {
                  output.append(space);
              }
          }
          else
          {
              output.append(input.substring(0,length));
          }
      }
      else
      {
          for (int i=0;i<length;i++)
          {
              output.append(space);
          }
      }
      return output.toString();
  }
  /** Utility to return a right-aligned version of a string padded to the
   * number of characters specified.
   * @param input The input string
   * @param length The length desired
   * @return The updated string
   **/
  public static String rightAlignedPaddedString(String input,int length)
  {
      if (length <= 0)
      {
          return null;
      }
      StringBuffer output=new StringBuffer();
      char         space=' ';
      if (input != null)
      {
          if (input.length() < length)
          {
              for (int i=input.length();i<length;i++)
              {
                  output.append(space);
              }
              output.append(input);
          }
          else
          {
              output.append(input.substring(0,length));
          }
      }
      else
      {
          for (int i=0;i<length;i++)
          {
              output.append(space);
          }
      }
      return output.toString();
  }
}
```

| 2.22.1. | String concatenation: '+' operation generates a new String object |
|---|---|
| 2.22.2. | String concatenation: The + contains null |
| 2.22.3. | String concatenation: Convert an integer to String and join with two other strings |
| 2.22.4. | String concatenation: Combining a string and integers |
| 2.22.5. | String concatenation: Combining integers and a string |
| 2.22.6. | Substring replacement. |
| 2.22.7. | Pad string |
| 2.22.8. | Padded String |
| 2.22.9. | Return a string padded with the given string for the given count. |
