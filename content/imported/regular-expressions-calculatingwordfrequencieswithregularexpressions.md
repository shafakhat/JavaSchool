---
title: Calculating Word Frequencies with Regular Expressions
nav: Calculating Word Frequenci...
description: MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0,
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20061201084831/http://www.java2s.com:80/Code/Java/Regular-Expressions/CalculatingWordFrequencieswithRegularExpressions.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.nio.CharBuffer;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class WordCount {
  public static void main(String args[]) throws Exception {
    String filename = "WordCount.java";
    // Map File from filename to byte buffer
    FileInputStream input = new FileInputStream(filename);
    FileChannel channel = input.getChannel();
    int fileLength = (int) channel.size();
    MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0,
        fileLength);
    // Convert to character buffer
    Charset charset = Charset.forName("ISO-8859-1");
    CharsetDecoder decoder = charset.newDecoder();
    CharBuffer charBuffer = decoder.decode(buffer);
    // Create line pattern
    Pattern linePattern = Pattern.compile(".*$", Pattern.MULTILINE);
    // Create word pattern
    Pattern wordBreakPattern = Pattern.compile("[\\p{Punct}\\s}]");
    // Match line pattern to buffer
    Matcher lineMatcher = linePattern.matcher(charBuffer);
    Map map = new TreeMap();
    Integer ONE = new Integer(1);
    // For each line
    while (lineMatcher.find()) {
      // Get line
      CharSequence line = lineMatcher.group();
      // Get array of words on line
      String words[] = wordBreakPattern.split(line);
      // For each word
      for (int i = 0, n = words.length; i < n; i++) {
        if (words[i].length() > 0) {
          Integer frequency = (Integer) map.get(words[i]);
          if (frequency == null) {
            frequency = ONE;
          } else {
            int value = frequency.intValue();
            frequency = new Integer(value + 1);
          }
          map.put(words[i], frequency);
        }
      }
    }
    System.out.println(map);
  }
}
```

Related examples in the same category
---
1. Regular expression: Split Demo
2. Replacing String Tokenizer
3. String replace
4. String split
5. Simple split
6. Print all the strings that match a given pattern from a file
7. Quick demo of Regular Expressions substitution
8. Parse an Apache log file with StringTokenizer
9. StringConvenience -- demonstrate java.lang.String convenience routine
10. Split a String into a Java Array of Strings divided by an Regular Expressions
11. Regular Expression Replace
12. Java Regular Expression : Split text
13. Java Regular Expression :split 2
