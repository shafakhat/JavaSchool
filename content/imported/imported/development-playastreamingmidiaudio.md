---
title: Play a streaming Midi audio
nav: Play a streaming Midi audio
description: InputStream input = new BufferedInputStream(new FileInputStream(new File("midiaudiofile")));
section: Imported
order: 20075
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/PlayastreamingMidiaudio.htm
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
    InputStream input = new BufferedInputStream(new FileInputStream(new File("midiaudiofile")));
    // From URL
    input = new BufferedInputStream(new URL("http://hostname/rmffile").openStream());
    sequencer.setSequence(input);
    // Start playing
    sequencer.start();
  }
}
```
