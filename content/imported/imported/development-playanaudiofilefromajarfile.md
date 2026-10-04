---
title: Play an audio file from a JAR file
nav: Play an audio file from a ...
description: Imported from java2s.com: Play an audio file from a JAR file
section: Imported
order: 20076
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/PlayanaudiofilefromaJARfile.htm
---
```java title=Example.java
import java.io.InputStream;
import sun.audio.AudioPlayer;
import sun.audio.AudioStream;
public class Main {
  public static void main(String args[]) throws Throwable {
    InputStream in = Main.class.getResourceAsStream(args[0]);
    AudioStream as = new AudioStream(in);
    AudioPlayer.player.start(as);
    Thread.sleep(5000);
  }
}
```
