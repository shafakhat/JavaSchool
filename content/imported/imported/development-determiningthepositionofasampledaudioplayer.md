---
title: Determining the Position of a Sampled Audio Player
nav: Determining the Position o...
description: double timeInSeconds = clip.getMicrosecondPosition() / 1000000.0d;
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20100206191516/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingthePositionofaSampledAudioPlayer.htm
---
```java title=Example.java
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
public class Main {
  public static void main(String[] argv) throws Exception {
    DataLine.Info info = null;
    Clip clip = (Clip) AudioSystem.getLine(info);
    double timeInSeconds = clip.getMicrosecondPosition() / 1000000.0d;
  }
}
```
