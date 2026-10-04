---
title: Play a streaming Midi audio
nav: Play a streaming Midi audio
description: InputStream input = new BufferedInputStream(new FileInputStream(new File("midiaudiofile")));
section: Imported - java2s Archive
order: 1976
source: https://web.archive.org/web/20140829082745/http://www.java2s.com/Tutorial/Java/0120__Development/PlayastreamingMidiaudio.htm
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

| 6.51.1. | Load and play Midi audio |
|---|---|
| 6.51.2. | Playing Streaming Midi Audio |
| 6.51.3. | Determining When a Midi Audio Player Has Finished Playing |
| 6.51.4. | Setting the Volume of Playing Midi Audio |
| 6.51.5. | Play a streaming Midi audio |
| 6.51.6. | Loading and Playing Midi Audio |
| 6.51.7. | Determine the duration of a Midi audio file |
| 6.51.8. | Determining the File Format of a Midi Audio File |
