---
title: A simple player for sampled sound files.
nav: A simple player for sample...
description: * Copyright (c) 1999 Sun Microsystems, Inc. All Rights Reserved.
section: Imported - java2s Archive
order: 2036
source: https://web.archive.org/web/20140223082230/http://www.java2s.com/Tutorial/Java/0120__Development/Asimpleplayerforsampledsoundfiles.htm
---
```java title=Example.java
/*
 *
 * Copyright (c) 1999 Sun Microsystems, Inc. All Rights Reserved.
 *
 * Sun grants you ("Licensee") a non-exclusive, royalty free,
 * license to use, modify and redistribute this software in
 * source and binary code form, provided that i) this copyright
 * notice and license appear on all copies of the software; and
 * ii) Licensee does not utilize the software in a manner
 * which is disparaging to Sun.
 *
 * This software is provided "AS IS," without a warranty
 * of any kind. ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS
 * AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT, ARE
 * HEREBY EXCLUDED. SUN AND ITS LICENSORS SHALL NOT BE LIABLE FOR
 * ANY DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
 * OR DISTRIBUTING THE SOFTWARE OR ITS DERIVATIVES. IN NO EVENT
 * WILL SUN OR ITS LICENSORS BE LIABLE FOR ANY LOST REVENUE, PROFIT
 * OR DATA, OR FOR DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL,
 * INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS
 * OF THE THEORY OF LIABILITY, ARISING OUT OF THE USE OF OR INABILITY
 * TO USE SOFTWARE, EVEN IF SUN HAS BEEN ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGES.
 This software is not designed or intended for use in on-line
 control of aircraft, air traffic, aircraft navigation or
 aircraft communications; or in the design, construction,
 operation or maintenance of any nuclear facility. Licensee
 represents and warrants that it will not use or redistribute
 the Software for such purposes.
 */
/*  The above copyright statement is included because this
 * program uses several methods from the JavaSoundDemo
 * distributed by SUN. In some cases, the sound processing methods
 * unmodified or only slightly modified.
 * All other methods copyright Steve Potts, 2002
 */
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.util.Vector;
import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MetaEventListener;
import javax.sound.midi.MetaMessage;
import javax.sound.midi.MidiChannel;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;
import javax.sound.midi.Synthesizer;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.LineEvent;
import javax.sound.sampled.LineListener;
/**
 *
 *
 * @author Steve Potts
 */
public class SimpleSoundPlayer implements Runnable, LineListener, MetaEventListener {
  final int bufSize = 16384;
  Vector sounds = new Vector();
  Thread thread;
  Sequencer sequencer;
  boolean midiEOM, audioEOM;
  Synthesizer synthesizer;
  MidiChannel channels[];
  Object currentSound;
  String currentName;
  double duration;
  int num;
  boolean bump;
  boolean paused = false;
  String errStr;
  public void open() {
    try {
      sequencer = MidiSystem.getSequencer();
      if (sequencer instanceof Synthesizer) {
        synthesizer = (Synthesizer) sequencer;
        channels = synthesizer.getChannels();
      }
    } catch (Exception ex) {
      ex.printStackTrace();
      return;
    }
    sequencer.addMetaEventListener(this);
  }
  public void close() {
    if (sequencer != null) {
      sequencer.close();
    }
  }
  private void addSound(File file) {
    sounds.add(file);
  }
  public boolean loadSound(Object object) {
    duration = 0.0;
    currentName = ((File) object).getName();
    try {
      currentSound = AudioSystem.getAudioInputStream((File) object);
    } catch (Exception e1) {
      try {
        FileInputStream is = new FileInputStream((File) object);
        currentSound = new BufferedInputStream(is, 1024);
      } catch (Exception e3) {
        e3.printStackTrace();
        currentSound = null;
        return false;
      }
      // }
    }
    // user pressed stop or changed tabs while loading
    if (sequencer == null) {
      currentSound = null;
      return false;
    }
    if (currentSound instanceof AudioInputStream) {
      try {
        AudioInputStream stream = (AudioInputStream) currentSound;
        AudioFormat format = stream.getFormat();
        /**
         * we can't yet open the device for ALAW/ULAW playback, convert
         * ALAW/ULAW to PCM
         */
        if ((format.getEncoding() == AudioFormat.Encoding.ULAW)
            || (format.getEncoding() == AudioFormat.Encoding.ALAW)) {
          AudioFormat tmp = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED,
              format.getSampleRate(), format.getSampleSizeInBits() * 2, format.getChannels(),
              format.getFrameSize() * 2, format.getFrameRate(), true);
          stream = AudioSystem.getAudioInputStream(tmp, stream);
          format = tmp;
        }
        DataLine.Info info = new DataLine.Info(Clip.class, stream.getFormat(), ((int) stream
            .getFrameLength() * format.getFrameSize()));
        Clip clip = (Clip) AudioSystem.getLine(info);
        clip.addLineListener(this);
        clip.open(stream);
        currentSound = clip;
        // seekSlider.setMaximum((int) stream.getFrameLength());
      } catch (Exception ex) {
        ex.printStackTrace();
        currentSound = null;
        return false;
      }
    } else if (currentSound instanceof Sequence || currentSound instanceof BufferedInputStream) {
      try {
        sequencer.open();
        if (currentSound instanceof Sequence) {
          sequencer.setSequence((Sequence) currentSound);
        } else {
          sequencer.setSequence((BufferedInputStream) currentSound);
        }
      } catch (InvalidMidiDataException imde) {
        System.out.println("Unsupported audio file.");
        currentSound = null;
        return false;
      } catch (Exception ex) {
        ex.printStackTrace();
        currentSound = null;
        return false;
      }
    }
    duration = getDuration();
    return true;
  }
  public void playSound() {
    midiEOM = audioEOM = bump = false;
    if (currentSound instanceof Sequence || currentSound instanceof BufferedInputStream
        && thread != null) {
      sequencer.start();
      while (!midiEOM && thread != null && !bump) {
        try {
          thread.sleep(99);
        } catch (Exception e) {
          break;
        }
      }
      sequencer.stop();
      sequencer.close();
    } else if (currentSound instanceof Clip) {
      Clip clip = (Clip) currentSound;
      clip.start();
      try {
        thread.sleep(99);
      } catch (Exception e) {
      }
      while ((paused || clip.isActive()) && thread != null && !bump) {
        try {
          thread.sleep(99);
        } catch (Exception e) {
          break;
        }
      }
      clip.stop();
      clip.close();
    }
    currentSound = null;
  }
  public double getDuration() {
    double duration = 0.0;
    if (currentSound instanceof Sequence) {
      duration = ((Sequence) currentSound).getMicrosecondLength() / 1000000.0;
    } else if (currentSound instanceof BufferedInputStream) {
      duration = sequencer.getMicrosecondLength() / 1000000.0;
    } else if (currentSound instanceof Clip) {
      Clip clip = (Clip) currentSound;
      duration = clip.getBufferSize()
          / (clip.getFormat().getFrameSize() * clip.getFormat().getFrameRate());
    }
    return duration;
  }
  public void update(LineEvent event) {
    if (event.getType() == LineEvent.Type.STOP && !paused) {
      audioEOM = true;
    }
  }
  public void meta(MetaMessage message) {
    if (message.getType() == 47) { // 47 is end of track
      midiEOM = true;
    }
  }
  private void reportStatus(String msg) {
    if ((errStr = msg) != null) {
      System.out.println(errStr);
    }
  }
  public Thread getThread() {
    return thread;
  }
  public void start() {
    thread = new Thread(this);
    thread.setName("SimpleSamplePlayer");
    thread.start();
  }
  public void stop() {
    if (thread != null) {
      thread.interrupt();
    }
    thread = null;
  }
  public void run() {
    for (; num < sounds.size() && thread != null; num++) {
      if (loadSound(sounds.get(num)) == true) {
        playSound();
      }
      // take a little break between sounds
      try {
        thread.sleep(222);
      } catch (Exception e) {
        break;
      }
    }
    num = 0;
    thread = null;
    currentName = null;
    currentSound = null;
    System.out.println("Press <ctrl-c> to exit");
  }
  public void loadSounds(String name) {
    try {
      File file = new File(name);
      if (file != null && file.isDirectory()) {
        String files[] = file.list();
        for (int i = 0; i < files.length; i++) {
          File leafFile = new File(file.getAbsolutePath(), files[i]);
          addSound(leafFile);
        }
      }
    } catch (Exception e) {
      System.out.println("Exception " + e);
    }
  }
  public static void main(String args[]) {
    // every file in this directory will be played
    String media = "c:/unleashed/ch18/sounds";
    final SimpleSoundPlayer ssp = new SimpleSoundPlayer();
    ssp.open();
    // we first load the sound file names in a vector
    ssp.loadSounds(media);
    // Then we start a thread to play the sounds
    ssp.start();
    // We have to wait for a while so that the process doesn't
    // terminate, killing the playing thread
    try {
      Thread.sleep(500000);
    } catch (Exception e) {
      System.out.println("Interrupted");
    }
    // close and exit
    ssp.close();
    System.exit(0);
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
