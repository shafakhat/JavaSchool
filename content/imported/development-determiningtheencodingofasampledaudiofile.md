---
title: Determining the Encoding of a Sampled Audio File
nav: Determining the Encoding o...
description: AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20100206191511/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingtheEncodingofaSampledAudioFile.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
public class Main {
  public static void main(String[] argv) throws Exception {
    AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
        "audiofile"));
  }
}
```
