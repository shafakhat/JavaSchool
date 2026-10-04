---
title: Play an audio file from a JAR file
nav: Play an audio file from a ...
description: Imported from the java2s.com archive: Play an audio file from a JAR file
section: Imported - java2s Archive
order: 2034
source: https://web.archive.org/web/20140829080130/http://www.java2s.com/Tutorial/Java/0120__Development/PlayanaudiofilefromaJARfile.htm
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

| 6.50.1. | Determining When a Sampled Audio Player Has Finished Playing |
|---|---|
| 6.50.2. | Setting the Volume of a Sampled Audio Player |
| 6.50.3. | Determining the Position of a Sampled Audio Player |
| 6.50.4. | Determining the Duration of a Sampled Audio File |
| 6.50.5. | Playing Streaming Sampled Audio |
| 6.50.6. | Loading and Playing Sampled Audio |
| 6.50.7. | Play an audio file from a JAR file |
| 6.50.8. | Determining the Encoding of a Sampled Audio File |
| 6.50.9. | Determining the File Format of a Sampled Audio File |
| 6.50.10. | Load image and sound from Jar file |
| 6.50.11. | A simple player for sampled sound files. |
| 6.50.12. | This is a simple program to record sounds and play them back |
| 6.50.13. | Capturing Audio with Java Sound API |
| 6.50.14. | Float Control Component |
| 6.50.15. | Make your own Java Media Player to play media files |
