---
title: Determining the File Format of a Midi Audio File
nav: Determining the File Forma...
description: MidiFileFormat fformat = MidiSystem.getMidiFileFormat(new File("midifile"));
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20110502090249/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingtheFileFormatofaMidiAudioFile.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.midi.MidiFileFormat;
import javax.sound.midi.MidiSystem;
public class Main {
  public static void main(String[] argv) throws Exception {
    // From file
    MidiFileFormat fformat = MidiSystem.getMidiFileFormat(new File("midifile"));
    // From URL
 //   fformat = MidiSystem.getMidiFileFormat(new URL("http://hostname/midifile"));
    // Get file format
    switch (fformat.getType()) {
    case 0:
      // mid
      break;
    case 1:
      // rmf
      break;
    }
  }
}
```
