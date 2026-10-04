---
title: Loading and Playing Midi Audio
nav: Loading and Playing Midi A...
description: Sequence sequence = MidiSystem.getSequence(new File("midifile"));
section: Imported
order: 20061
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/LoadingandPlayingMidiAudio.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;
public class Main {
  public static void main(String[] argv) throws Exception {
    Sequence sequence = MidiSystem.getSequence(new File("midifile"));
    // From URL
    sequence = MidiSystem.getSequence(new URL("http://hostname/midifile"));
    // Create a sequencer for the sequence
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    sequencer.setSequence(sequence);
    // Start playing
    sequencer.start();
  }
}
```
