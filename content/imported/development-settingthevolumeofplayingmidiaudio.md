---
title: Setting the Volume of Playing Midi Audio
nav: Setting the Volume of Play...
description: Imported from the java2s.com archive: Setting the Volume of Playing Midi Audio
section: Imported - java2s Archive
order: 1991
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0120__Development/SettingtheVolumeofPlayingMidiAudio.htm
---
```java title=Example.java
import javax.sound.midi.MidiChannel;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequencer;
import javax.sound.midi.Synthesizer;
public class Main {
  public static void main(String[] argv) throws Exception {
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    if (sequencer instanceof Synthesizer) {
      Synthesizer synthesizer = (Synthesizer) sequencer;
      MidiChannel[] channels = synthesizer.getChannels();
      // gain is a value between 0 and 1 (loudest)
 double gain = 0.9D;
      for (int i = 0; i < channels.length; i++) {
        channels[i].controlChange(7, (int) (gain * 127.0));
      }
    }
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
