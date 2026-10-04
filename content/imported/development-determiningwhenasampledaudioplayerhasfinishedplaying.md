---
title: Determining When a Sampled Audio Player Has Finished Playing
nav: Determining When a Sampled...
description: Imported from the java2s.com archive: Determining When a Sampled Audio Player Has Finished Playing
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20100206191300/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingWhenaSampledAudioPlayerHasFinishedPlaying.htm
---
```java title=Example.java
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.LineEvent;
import javax.sound.sampled.LineListener;
public class Main {
  public static void main(String[] argv) throws Exception {
    DataLine.Info info = null;
    Clip clip = (Clip) AudioSystem.getLine(info);
    clip.addLineListener(new LineListener() {
      public void update(LineEvent evt) {
        if (evt.getType() == LineEvent.Type.STOP) {
        }
      }
    });
  }
}
```
