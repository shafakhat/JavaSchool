---
title: Determines if the specified string is permissible as a Java identifier.
nav: Determines if the specifie...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20140829082933/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminesifthespecifiedstringispermissibleasaJavaidentifier.htm
---
```java title=Example.java
/*
 * Copyright 2005 Joe Walker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
/**
 * @author Joe Walker [joe at getahead dot ltd dot uk]
 */
public class Main {
  /**
   * Returns true if the string is non-null, non-zero length with a Java
   * identifier start as the first character and Java identifier parts in all
   * remaining characters.
   * @param test the string to be tested.
   * @return true if the string is a Java identifier, false otherwise.
   * @see java.lang.Character#isJavaIdentifierPart(char)
   * @see java.lang.Character#isJavaIdentifierStart(char)
   */
  public static boolean isJavaIdentifier(String test)
  {
      if (test == null || test.length() == 0)
      {
          return false;
      }
      if (!Character.isJavaIdentifierStart(test.charAt(0)) && test.charAt(0) != '_')
      {
          return false;
      }
      for (int i = 1; i < test.length(); i++)
      {
          if (!Character.isJavaIdentifierPart(test.charAt(i)) && test.charAt(i) != '_')
          {
              return false;
          }
      }
      return true;
  }
}
```
