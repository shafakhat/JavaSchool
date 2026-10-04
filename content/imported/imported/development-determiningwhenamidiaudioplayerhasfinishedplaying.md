---
title: Determining When a Midi Audio Player Has Finished Playing
nav: Determining When a Midi Au...
description: Imported from the java2s.com archive: Determining When a Midi Audio Player Has Finished Playing
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20110503081051/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingWhenaMidiAudioPlayerHasFinishedPlaying.htm
---
```java title=Example.java
import javax.sound.midi.MetaEventListener;
import javax.sound.midi.MetaMessage;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequencer;
public class Main {
  public static void main(String[] argv) throws Exception {
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    sequencer.addMetaEventListener(new MetaEventListener() {
      public void meta(MetaMessage event) {
        if (event.getType() == 47) {
          // Sequencer is done playing
        }
      }
    });
  }
}
```
