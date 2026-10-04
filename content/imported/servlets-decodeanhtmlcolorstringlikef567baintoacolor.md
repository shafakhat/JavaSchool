---
title: Decode an HTML color string like '#F567BA;' into a Color
nav: Decode an HTML color strin...
description: Decode an HTML color string like '#F567BA;' into a Color : HTML Output « Servlets « Java
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20091006124627/http://www.java2s.com:80/Code/Java/Servlets/DecodeanHTMLcolorstringlikeF567BAintoaColor.htm
---
Decode an HTML color string like '#F567BA;' into a Color : HTML Output « Servlets « Java
Decode an HTML color string like '#F567BA;' into a Color

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
import java.awt.Color;
/**
 * Utilities for working with colors.
 * @author Joe Walker [joe at getahead dot ltd dot uk]
 */
public class ColorUtil
{
    /**
     * Decode an HTML color string like '#F567BA;' into a {@link Color}
     * @param colorString The string to decode
     * @return The decoded color
     * @throws IllegalArgumentException if the color sequence is not valid
     */
    public static Color decodeHtmlColorString(String colorString)
    {
        Color color;
        if (colorString.startsWith("#"))
        {
            colorString = colorString.substring(1);
        }
        if (colorString.endsWith(";"))
        {
            colorString = colorString.substring(0, colorString.length() - 1);
        }
        int red, green, blue;
        switch (colorString.length())
        {
        case 6:
            red = Integer.parseInt(colorString.substring(0, 2), 16);
            green = Integer.parseInt(colorString.substring(2, 4), 16);
            blue = Integer.parseInt(colorString.substring(4, 6), 16);
            color = new Color(red, green, blue);
            break;
        case 3:
            red = Integer.parseInt(colorString.substring(0, 1), 16);
            green = Integer.parseInt(colorString.substring(1, 2), 16);
            blue = Integer.parseInt(colorString.substring(2, 3), 16);
            color = new Color(red, green, blue);
            break;
        case 1:
            red = green = blue = Integer.parseInt(colorString.substring(0, 1), 16);
            color = new Color(red, green, blue);
            break;
        default:
            throw new IllegalArgumentException("Invalid color: " + colorString);
        }
        return color;
    }
}
```

1.  Servlet Output HTML Demo
---  ---
2.  Servlet Display Static HTML
3.  Prints a conversion table of miles per gallon to kilometers per liter
4.  Servlet: Print Table
5.  Html utilities
6.  Html Parse Servlet
7.  Escape and unescape string
8.  Escapes newlines, tabs, backslashes, and quotes in the specified string
9.  Web Calendar
10.  HTML Helper
11.  Escape HTML
12.  Convert HTML to text
13.  Text To HTML
14.  Unescape HTML
15.  Java object representations of the HTML table structure
16.  Entity Decoder
17.  Format a color to HTML RGB color format (e.g. #FF0000 for Color.red)
18.  Definitions of HTML character entities and conversions between unicode characters and HTML character entities
19.  Encode special characters and do formatting for HTML output
20.  HTML color names
21.  Utility methods for dealing with HTML
22.  Filter the specified message string for characters that are sensitive in HTML
23.  A collection of all character entites defined in the HTML4 standard.
24.  Normalize Post Data
25.  Get HTML Color String from Java Color object
26.  HTML Decoder
27.  HTML Parser
28.  HTML color and Java Color
29.  HTML form Utilites
30.  Html Dimensions
31.  break Lines with HTML
32.  insert HTML block dynamically
33.  Convert an integer to an HTML RGB value
34.  Convert to HTML string
