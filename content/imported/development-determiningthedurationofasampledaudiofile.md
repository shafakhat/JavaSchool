---
title: Determining the Duration of a Sampled Audio File
nav: Determining the Duration o...
description: / (clip.getFormat().getFrameSize() * clip.getFormat().getFrameRate());
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20100206191305/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingtheDurationofaSampledAudioFile.htm
---
```java title=Example.java
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
public class Main {
  public static void main(String[] argv) throws Exception {
    DataLine.Info info = null;
    Clip clip = (Clip) AudioSystem.getLine(info);
    double durationInSecs = clip.getBufferSize()
        / (clip.getFormat().getFrameSize() * clip.getFormat().getFrameRate());
  }
}
```
