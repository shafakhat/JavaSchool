---
title: Determining the File Format of a Sampled Audio File
nav: Determining the File Forma...
description: AudioFileFormat fformat = AudioSystem.getAudioFileFormat(new File(
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20100206191310/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeterminingtheFileFormatofaSampledAudioFile.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioSystem;
public class Main {
  public static void main(String[] argv) throws Exception {
    AudioFileFormat fformat = AudioSystem.getAudioFileFormat(new File(
        "audiofile"));
    fformat = AudioSystem.getAudioFileFormat(new URL(
        "http://hostname/audiofile"));
    if (fformat.getType() == AudioFileFormat.Type.AIFC) {
    } else if (fformat.getType() == AudioFileFormat.Type.AIFF) {
    } else if (fformat.getType() == AudioFileFormat.Type.AU) {
    } else if (fformat.getType() == AudioFileFormat.Type.WAVE) {
    }
  }
}
```
