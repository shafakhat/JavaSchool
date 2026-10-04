---
title: Loading and Playing Midi Audio
nav: Loading and Playing Midi A...
description: Sequence sequence = MidiSystem.getSequence(new File("midifile"));
section: Imported - java2s Archive
order: 1977
source: https://web.archive.org/web/20140829082407/http://www.java2s.com/Tutorial/Java/0120__Development/LoadingandPlayingMidiAudio.htm
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

| 6.51.1. | Load and play Midi audio |
|---|---|
| 6.51.2. | Playing Streaming Midi Audio |
| 6.51.3. | Determining When a Midi Audio Player Has Finished Playing |
| 6.51.4. | Setting the Volume of Playing Midi Audio |
| 6.51.5. | Play a streaming Midi audio |
| 6.51.6. | Loading and Playing Midi Audio |
| 6.51.7. | Determine the duration of a Midi audio file |
| 6.51.8. | Determining the File Format of a Midi Audio File |
