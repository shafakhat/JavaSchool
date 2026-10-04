---
title: Replace New Lines
nav: Replace New Lines
description: * wingS is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1179
source: https://web.archive.org/web/20100412210130/http://java2s.com:80/Tutorial/Java/0040__Data-Type/ReplaceNewLines.htm
---
```java title=Example.java
/*
 * Copyright 2000,2005 wingS development team.
 *
 * This file is part of wingS (http://wingsframework.org).
 *
 * wingS is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License
 * as published by the Free Software Foundation; either version 2.1
 * of the License, or (at your option) any later version.
 *
 * Please see COPYING for the complete licence.
 */
import java.util.StringTokenizer;
/**
 * Some string manipulation utilities.
 *
 * @author <a href="mailto:haaf@mercatis.de">Armin Haaf</a>
 */
public class StringUtil {
  /**
   * replaces all newlines in the given String 's' with the replacement
   * string 'r'. Each line is trimmed from leading and trailing whitespaces,
   * then the new line-delimiter is added.
   *
   * @param s the source string.
   * @param r the new line delimiter
   * @return the resulting string.
   */
  public static final String replaceNewLines(String s, String r) {
      StringBuilder result = new StringBuilder();
      StringTokenizer t = new StringTokenizer(s, "\n");
      while (t.hasMoreTokens()) {
          result.append(t.nextToken().trim()).append(r);
      }
      return result.toString();
  }
}
```
