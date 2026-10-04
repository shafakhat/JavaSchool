---
title: Playing Streaming Midi Audio
nav: Playing Streaming Midi Audio
description: InputStream is = new BufferedInputStream(new FileInputStream(new File(
section: Imported
order: 20077
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/PlayingStreamingMidiAudio.htm
---
```java title=Example.java
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URL;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequencer;
public class Main {
  public static void main(String[] argv) throws Exception {
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    // From file
    InputStream is = new BufferedInputStream(new FileInputStream(new File(
        "midifile")));
    // From URL
//    is = new BufferedInputStream(new URL("http://hostname/rmffile")
  //      .openStream());
    sequencer.setSequence(is);
    // Start playing
    sequencer.start();
  }
}
```
