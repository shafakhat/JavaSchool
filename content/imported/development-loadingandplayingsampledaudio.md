---
title: Loading and Playing Sampled Audio
nav: Loading and Playing Sample...
description: AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
section: Imported - java2s Archive
order: 2038
source: https://web.archive.org/web/20140829080045/http://www.java2s.com/Tutorial/Java/0120__Development/LoadingandPlayingSampledAudio.htm
---
```java title=Example.java
import java.io.File;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
public class Main {
  public static void main(String[] argv) throws Exception {
    AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
        "audiofile"));
    // From URL
    // stream = AudioSystem.getAudioInputStream(new URL(
    // "http://hostname/audiofile"));
    AudioFormat format = stream.getFormat();
    if (format.getEncoding() != AudioFormat.Encoding.PCM_SIGNED) {
      format = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED, format
          .getSampleRate(), format.getSampleSizeInBits() * 2, format
          .getChannels(), format.getFrameSize() * 2, format.getFrameRate(),
          true); // big endian
      stream = AudioSystem.getAudioInputStream(format, stream);
    }
    DataLine.Info info = new DataLine.Info(Clip.class, stream.getFormat(),
        ((int) stream.getFrameLength() * format.getFrameSize()));
    Clip clip = (Clip) AudioSystem.getLine(info);
    clip.open(stream);
    clip.start();
  }
}
```

| 6.50.1. | Determining When a Sampled Audio Player Has Finished Playing |
|---|---|
| 6.50.2. | Setting the Volume of a Sampled Audio Player |
| 6.50.3. | Determining the Position of a Sampled Audio Player |
| 6.50.4. | Determining the Duration of a Sampled Audio File |
| 6.50.5. | Playing Streaming Sampled Audio |
| 6.50.6. | Loading and Playing Sampled Audio |
| 6.50.7. | Play an audio file from a JAR file |
| 6.50.8. | Determining the Encoding of a Sampled Audio File |
| 6.50.9. | Determining the File Format of a Sampled Audio File |
| 6.50.10. | Load image and sound from Jar file |
| 6.50.11. | A simple player for sampled sound files. |
| 6.50.12. | This is a simple program to record sounds and play them back |
| 6.50.13. | Capturing Audio with Java Sound API |
| 6.50.14. | Float Control Component |
| 6.50.15. | Make your own Java Media Player to play media files |
