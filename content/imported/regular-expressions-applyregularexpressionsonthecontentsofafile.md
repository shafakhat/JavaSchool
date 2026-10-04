---
title: Apply Regular Expressions on the contents of a file
nav: Apply Regular Expressions ...
description: ByteBuffer bbuf = channel.map(FileChannel.MapMode.READ_ONLY, 0, (int) channel.size());
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20090504061122/http://www.java2s.com:80/Code/Java/Regular-Expressions/ApplyRegularExpressionsonthecontentsofafile.htm
---
```java title=Example.java
import java.io.FileInputStream;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] argv) throws Exception {
    Pattern pattern = Pattern.compile("pattern");
    FileInputStream input = new FileInputStream("file.txt");
    FileChannel channel = input.getChannel();
    ByteBuffer bbuf = channel.map(FileChannel.MapMode.READ_ONLY, 0, (int) channel.size());
    CharBuffer cbuf = Charset.forName("8859_1").newDecoder().decode(bbuf);
    Matcher matcher = pattern.matcher(cbuf);
    while (matcher.find()) {
      String match = matcher.group();
      System.out.println(match);
    }
  }
}
```

1.  Use FileChannels and ByteBuffers to Store Patterns
---  ---
2.  Using a Regular Expression to Filter Lines from a Reader
3.  Reading Lines from a String Using a Regular Expression
