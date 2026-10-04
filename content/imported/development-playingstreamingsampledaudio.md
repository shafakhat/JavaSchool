---
title: Playing Streaming Sampled Audio
nav: Playing Streaming Sampled ...
description: AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
section: Imported - java2s Archive
order: 2039
source: https://web.archive.org/web/20140829080049/http://www.java2s.com/Tutorial/Java/0120__Development/PlayingStreamingSampledAudio.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.SourceDataLine;
public class Main {
  public static void main(String[] argv) throws Exception {
    AudioInputStream stream = AudioSystem.getAudioInputStream(new File(
        "audiofile"));
//    stream = AudioSystem.getAudioInputStream(new URL(
  //      "http://hostname/audiofile"));
    AudioFormat format = stream.getFormat();
    if (format.getEncoding() != AudioFormat.Encoding.PCM_SIGNED) {
      format = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED, format
          .getSampleRate(), format.getSampleSizeInBits() * 2, format
          .getChannels(), format.getFrameSize() * 2, format.getFrameRate(),
          true); // big endian
      stream = AudioSystem.getAudioInputStream(format, stream);
    }
    SourceDataLine.Info info = new DataLine.Info(SourceDataLine.class, stream
        .getFormat(), ((int) stream.getFrameLength() * format.getFrameSize()));
    SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
    line.open(stream.getFormat());
    line.start();
    int numRead = 0;
    byte[] buf = new byte[line.getBufferSize()];
    while ((numRead = stream.read(buf, 0, buf.length)) >= 0) {
      int offset = 0;
      while (offset < numRead) {
        offset += line.write(buf, offset, numRead - offset);
      }
    }
    line.drain();
    line.stop();
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
