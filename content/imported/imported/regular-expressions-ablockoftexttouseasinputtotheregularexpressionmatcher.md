---
title: A block of text to use as input to the regular expression matcher
nav: A block of text to use as ...
description: A block of text to use as input to the regular expression matcher
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20070115014418/http://www.java2s.com:80/Code/Java/Regular-Expressions/Ablockoftexttouseasinputtotheregularexpressionmatcher.htm
---
```java title=Example.java
// : c12:TheReplacements.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/*
 * ! Here's a block of text to use as input to the regular expression matcher.
 * Note that we'll first extract the block of text by looking for the special
 * delimiters, then process the extracted block. !
 */
public class TheReplacements {
  public static void main(String[] args) throws Exception {
    String s = TextFile.read("TheReplacements.java");
    // Match the specially-commented block of text above:
    Matcher mInput = Pattern.compile("/\\*!(.*)!\\*/", Pattern.DOTALL)
        .matcher(s);
    if (mInput.find())
      s = mInput.group(1); // Captured by parentheses
    // Replace two or more spaces with a single space:
    s = s.replaceAll(" {2,}", " ");
    // Replace one or more spaces at the beginning of each
    // line with no spaces. Must enable MULTILINE mode:
    s = s.replaceAll("(?m)^ +", "");
    System.out.println(s);
    s = s.replaceFirst("[aeiou]", "(VOWEL1)");
    StringBuffer sbuf = new StringBuffer();
    Pattern p = Pattern.compile("[aeiou]");
    Matcher m = p.matcher(s);
    // Process the find information as you
    // perform the replacements:
    while (m.find())
      m.appendReplacement(sbuf, m.group().toUpperCase());
    // Put in the remainder of the text:
    m.appendTail(sbuf);
    System.out.println(sbuf);
  }
} ///:~
class TextFile extends ArrayList {
  // Tools to read and write files as single strings:
  public static String read(String fileName) throws IOException {
    StringBuffer sb = new StringBuffer();
    BufferedReader in = new BufferedReader(new FileReader(fileName));
    String s;
    while ((s = in.readLine()) != null) {
      sb.append(s);
      sb.append("\n");
    }
    in.close();
    return sb.toString();
  }
  public static void write(String fileName, String text) throws IOException {
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(
        fileName)));
    out.print(text);
    out.close();
  }
  public TextFile(String fileName) throws IOException {
    super(Arrays.asList(read(fileName).split("\n")));
  }
  public void write(String fileName) throws IOException {
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(
        fileName)));
    for (int i = 0; i < size(); i++)
      out.println(get(i));
    out.close();
  }
  // Simple test:
  public static void main(String[] args) throws Exception {
    String file = read("TextFile.java");
    write("test.txt", file);
    TextFile text = new TextFile("test.txt");
    text.write("test2.txt");
  }
} ///:~
```

Related examples in the same category
---
1. Simple Pattern
2. Pattern Match
3. Pattern Split
4. Another pattern split
5. Reg Exp Example
6. PatternConvenience -- demonstrate java.util.regex.Pattern convenience routine
7. Simple example of using Regular Expressions functionality in String class
8. Show use of Pattern.CANON_EQ
9. Allows you to easly try out regular expressions
10. Regular expressions: start End
11. Pattern: Resetting
12. Pattern: flags
