---
title: Determine the duration of a Midi audio file
nav: Determine the duration of ...
description: Sequence sequence = MidiSystem.getSequence(new File("midiaudiofile"));
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20110502085400/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminethedurationofaMidiaudiofile.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;
public class Main {
  public static void main(String[] argv) throws Exception {
    Sequence sequence = MidiSystem.getSequence(new File("midiaudiofile"));
    sequence = MidiSystem.getSequence(new URL("http://hostname/midiaudiofile"));
    // Create a sequencer for the sequence
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    sequencer.setSequence(sequence);
    double durationInSecs = sequencer.getMicrosecondLength() / 1000000.0;
  }
}
```
