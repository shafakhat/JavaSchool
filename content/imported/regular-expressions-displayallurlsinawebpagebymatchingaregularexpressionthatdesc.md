---
title: Display all URLs in a web page by matching a regular expression that describes the <a href=...> HTML tag
nav: Display all URLs in a web ...
description: Display all URLs in a web page by matching a regular expression that describes the HTML tag
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20110924024033/http://www.java2s.com:80/Code/Java/Regular-Expressions/DisplayallURLsinawebpagebymatchingaregularexpressionthatdescribestheahrefHTMLtag.htm
---
Display all URLs in a web page by matching a regular expression that describes the HTML tag

```java title=Example.java
/*
   This program is a part of the companion code for Core Java 8th ed.
   (http://horstmann.com/corejava)
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
/**
 * This program displays all URLs in a web page by matching a regular expression that describes the
 * <a href=...> HTML tag. Start the program as <br>
 * java HrefMatch URL
 * @version 1.01 2004-06-04
 * @author Cay Horstmann
 */
public class HrefMatch
{
   public static void main(String[] args)
   {
      try
      {
         // get URL string from command line or use default
         String urlString;
         if (args.length > 0) urlString = args[0];
         else urlString = "http://java.sun.com";
         // open reader for URL
         InputStreamReader in = new InputStreamReader(new URL(urlString).openStream());
         // read contents into string builder
         StringBuilder input = new StringBuilder();
         int ch;
         while ((ch = in.read()) != -1)
            input.append((char) ch);
         // search for all occurrences of pattern
         String patternString = "<a\\s+href\\s*=\\s*(\"[^\"]*\"|[^\\s>]*)\\s*>";
         Pattern pattern = Pattern.compile(patternString, Pattern.CASE_INSENSITIVE);
         Matcher matcher = pattern.matcher(input);
         while (matcher.find())
         {
            int start = matcher.start();
            int end = matcher.end();
            String match = input.substring(start, end);
            System.out.println(match);
         }
      }
      catch (IOException e)
      {
         e.printStackTrace();
      }
      catch (PatternSyntaxException e)
      {
         e.printStackTrace();
      }
   }
}
```

1.  Meta-characters to match against certain string boundaries
---  ---
2.  Characters classes specifies a list of possible characters
3.  POSIX character classes and Java character classes
4.  Character Class Matches
5.  Greedy Operator Description
6.  Reluctant (Lazy) Operator Description
7.  Displays directory listing using regular expressions
8.  Like Regular Expression Demo in a TextField
9.  StringConvenience -- demonstrate java.lang.String convenience routine
10.  Split a String into a Java Array of Strings divided by an Regular Expressions
11.  Simple example of using Regular Expressions class.
12.  Match the Q[^u] pattern against strings from command line
13.  demonstrate Regular Expressions: Match -> group()
14.  Show case control using Regular Expressions class.
15.  Matcher and Pattern demo
16.  Matcher and Pattern demo 2
17.  Standalone Swing GUI application for demonstrating Regular expressions.
18.  Regular Expressions in Action
19.  Match SQL string
