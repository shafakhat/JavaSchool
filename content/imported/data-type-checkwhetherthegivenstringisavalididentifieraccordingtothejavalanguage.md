---
title: Check whether the given String is a valid identifier according to the Java Language specifications.
nav: Check whether the given St...
description: 2.31.12.Check whether the given String is a valid identifier according to the Java Language specifications. Previous / Next
section: Imported - java2s Archive
order: 1356
source: https://web.archive.org/web/20140614112938/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckwhetherthegivenStringisavalididentifieraccordingtotheJavaLanguagespecifications.htm
---
2.31.12.Check whether the given String is a valid identifier according to the Java Language specifications. Previous / Next

```java title=Example.java
import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.net.URLDecoder;
import java.util.Map;
/*
  * JBoss, Home of Professional Open Source
  * Copyright 2005, JBoss Inc., and individual contributors as indicated
  * by the @authors tag. See the copyright.txt in the distribution for a
  * full listing of individual contributors.
  *
  * This is free software; you can redistribute it and/or modify it
  * under the terms of the GNU Lesser General Public License as
  * published by the Free Software Foundation; either version 2.1 of
  * the License, or (at your option) any later version.
  *
  * This software is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  * Lesser General Public License for more details.
  *
  * You should have received a copy of the GNU Lesser General Public
  * License along with this software; if not, write to the Free
  * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
  * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
  */
public class Main{
  /**
   * Check whether the given String is a valid identifier according
   * to the Java Language specifications.
   *
   * See The Java Language Specification Second Edition, Section 3.8
   * for the definition of what is a valid identifier.
   *
   * @param s String to check
   *
   * @return <code>true</code> if the given String is a valid Java
   *         identifier, <code>false</code> otherwise.
   */
  public final static boolean isValidJavaIdentifier(String s)
  {
     // an empty or null string cannot be a valid identifier
     if (s == null || s.length() == 0)
     {
        return false;
     }
     char[] c = s.toCharArray();
     if (!Character.isJavaIdentifierStart(c[0]))
     {
        return false;
     }
     for (int i = 1; i < c.length; i++)
     {
        if (!Character.isJavaIdentifierPart(c[i]))
        {
           return false;
        }
     }
     return true;
  }
}
```

| 2.31.1. | Match Phone Number |
|---|---|
| 2.31.2. | Match Zip Codes |
| 2.31.3. | Match Dates |
| 2.31.4. | Match Name Formats |
| 2.31.5. | Case insensitive check if a String ends with a specified suffix. |
| 2.31.6. | Case insensitive check if a String starts with a specified prefix. |
| 2.31.7. | Case insensitive removal of a substring if it is at the begining of a source string, otherwise returns the source string. |
| 2.31.8. | Case insensitive removal of a substring if it is at the end of a source string, otherwise returns the source string. |
| 2.31.9. | Check if a String ends with a specified suffix. |
| 2.31.10. | Check if a String starts with a specified prefix. |
| 2.31.11. | Check if a string is present at the current position in another string. |
| 2.31.12. | Check whether the given String is a valid identifier according to the Java Language specifications. |
| 2.31.13. | Checks if String contains a search String irrespective of case, handling null |
| 2.31.14. | Checks if String contains a search String, handling null |
| 2.31.15. | Checks if String contains a search character, handling null |
| 2.31.16. | Checks if a String is empty ("") or null. |
| 2.31.17. | Checks if a String is not empty ("") and not null. |
| 2.31.18. | Checks if a String is whitespace, empty ("") or null. |
| 2.31.19. | Checks if the String contains any character in the given set of characters. |
| 2.31.20. | Checks if the String contains only certain characters. |
