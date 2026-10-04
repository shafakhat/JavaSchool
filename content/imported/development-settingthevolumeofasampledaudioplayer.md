---
title: Setting the Volume of a Sampled Audio Player
nav: Setting the Volume of a Sa...
description: Imported from the java2s.com archive: Setting the Volume of a Sampled Audio Player
section: Imported - java2s Archive
order: 2037
source: https://web.archive.org/web/20140829075955/http://www.java2s.com/Tutorial/Java/0120__Development/SettingtheVolumeofaSampledAudioPlayer.htm
---
```java title=Example.java
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.BooleanControl;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.FloatControl;
public class Main {
  public static void main(String[] argv) throws Exception {
    DataLine.Info info = null;
    Clip clip = (Clip) AudioSystem.getLine(info);
    FloatControl gainControl = (FloatControl) clip
        .getControl(FloatControl.Type.MASTER_GAIN);
    double gain = .5D; // number between 0 and 1 (loudest)
    float dB = (float) (Math.log(gain) / Math.log(10.0) * 20.0);
    gainControl.setValue(dB);
    BooleanControl muteControl = (BooleanControl) clip
        .getControl(BooleanControl.Type.MUTE);
    muteControl.setValue(true);
    muteControl.setValue(false);
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
