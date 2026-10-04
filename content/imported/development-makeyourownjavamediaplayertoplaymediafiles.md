---
title: Make your own Java Media Player to play media files
nav: Make your own Java Media P...
description: Imported from the java2s.com archive: Make your own Java Media Player to play media files
section: Imported - java2s Archive
order: 2043
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0120__Development/MakeyourownJavaMediaPlayertoplaymediafiles.htm
---
```java title=Example.java
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import javax.media.*;
public class MediaPlayerDemo extends JFrame {
  public static void main(String args[]) {
    Player player;
    File file = new File("yourFile");
    player = Manager.createPlayer(file.toURI().toURL());
//    player.addControllerListener(new EventHandler());
    player.start(); // start player
    player.close();
    Component visual = player.getVisualComponent();
    Component control = player.getControlPanelComponent();
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
