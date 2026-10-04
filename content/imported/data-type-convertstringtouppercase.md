---
title: Convert string to uppercase
nav: Convert string to uppercase
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1468
source: https://web.archive.org/web/20140407035411/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertstringtouppercase.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Properties;
/*
   Derby - Class org.apache.derby.iapi.util.PropertyUtil
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to you under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */
public class Main {
   * Always use the java.util.ENGLISH locale
   * @param s   string to uppercase
   * @return uppercased string
   */
  public static String SQLToUpperCase(String s)
  {
      return s.toUpperCase(Locale.ENGLISH);
  }
}
```

| 2.30.1. | Format Calendar with String.format() |
|---|---|
| 2.30.2. | Format strings into table |
| 2.30.3. | String.format(): right pad a string |
| 2.30.4. | String.format(): left pad a string |
| 2.30.5. | Format a String (JDK1.5) |
| 2.30.6. | Pass value array to String.format() |
| 2.30.7. | Remove/collapse multiple newline characters. |
| 2.30.8. | Abbreviate string |
| 2.30.9. | Capital and uncapital strings |
| 2.30.10. | Transforms words to singular, plural, humanized (human readable), underscore, camel case, or ordinal form |
| 2.30.11. | Replace New Lines |
| 2.30.12. | Fix Line Separator |
| 2.30.13. | Abbreviates a String using ellipses in both sides. |
| 2.30.14. | Abbreviates a String using ellipses. |
| 2.30.15. | Capitalize the first character of the given string |
| 2.30.16. | Centers a String in a larger String of size size using the space character (' '). |
| 2.30.17. | Centers a String in a larger String of size size. Uses a supplied String as the value to pad the String with. |
| 2.30.18. | Centers a String in a larger String of size size. Uses a supplied character as the value to pad the String with. |
| 2.30.19. | Convert string to uppercase |
| 2.30.20. | Left pad a String with a specified String. |
| 2.30.21. | Left pad a String with a specified character. |
| 2.30.22. | Left pad a String with spaces (' '). |
| 2.30.23. | Makes the first letter caps and the rest lowercase. |
| 2.30.24. | Put quotes around the given String if necessary. |
| 2.30.25. | Quote a string so that it can be used as an identifier or a string literal in SQL statements. |
| 2.30.26. | Right pad a String with a specified String. |
| 2.30.27. | Right pad a String with a specified character. |
| 2.30.28. | Right pad a String with spaces (' '). |
| 2.30.29. | Trim off trailing blanks but not leading blanks |
| 2.30.30. | Truncate a String to the given length with no warnings or error raised if it is bigger. |
| 2.30.31. | Uncapitalizes a String changing the first letter to title case as per Character.toLowerCase(char). No other letters are changed. |
| 2.30.32. | Repeat String |
| 2.30.33. | Repeat a String repeat times to form a new String. |
| 2.30.34. | Strip Line Breaks |
| 2.30.35. | Trim any of the characters |
| 2.30.36. | Removes one newline from end of a String if it's there, otherwise leave it alone. |
| 2.30.37. | Removes newline, carriage return and tab characters from a string |
| 2.30.38. | Remove the leading and trailing quotes from str. |
