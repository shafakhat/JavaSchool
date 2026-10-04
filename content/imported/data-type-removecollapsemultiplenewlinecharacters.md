---
title: Remove/collapse multiple newline characters.
nav: Remove/collapse multiple n...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1315
source: https://web.archive.org/web/20140407041240/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removecollapsemultiplenewlinecharacters.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
/**
 *
 *  @author <a href="mailto:jvanzyl@apache.org">Jason van Zyl</a>
 *  @author <a href="mailto:dlr@finemaltcoding.com">Daniel Rall</a>
 *  @version $Id: StringUtils.java 685685 2008-08-13 21:43:27Z nbubna $
 */
public class Main {
  /**
   *
   * @param argStr string to collapse newlines in.
   * @return String
   */
  public static String collapseNewlines(String argStr)
  {
      char last = argStr.charAt(0);
      StringBuffer argBuf = new StringBuffer();
      for (int cIdx = 0 ; cIdx < argStr.length(); cIdx++)
      {
          char ch = argStr.charAt(cIdx);
          if (ch != '\n' || last != '\n')
          {
              argBuf.append(ch);
              last = ch;
          }
      }
      return argBuf.toString();
  }
}
```
