---
title: A Bare Bones Player
nav: A Bare Bones Player
description: A Bare Bones Player: play the media object : Java examples (example source code) » 2D Graphics GUI » Media
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20060506155216/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/ABareBonesPlayerplaythemediaobject.htm
---
A Bare Bones Player: play the media object : Java examples (example source code) » 2D Graphics GUI » Media

A Bare Bones Player: play the media object

```java title=Example.java
/*
Java Media APIs: Cross-Platform Imaging, Media and Visualization
Alejandro Terrazas
Sams, Published November 2002,
ISBN 0672320940
*/
/*******************************************************************************
 * A "Bare Bones" Player Applet (BBP Applet) that will play the media object
 * indicated in the "media2Play" property of the Applet tag.
 *
 * <p>
 * The applet demonstrates the relative ease with which the JMF can be employed,
 * particularly for playing. The applet a minimal player, placing the controls
 * for the player and the visual component for the played object within the
 * Applet. The object plays once, but can be controlled by the user through the
 * control panel provided.
 *
 * <p>
 * The tag for the Applet should look something like:
 *
 * <!-- Sample HTML <applet code="BBPApplet.class" width=300 height=400> <param
 * name="media2Play" value="myVideo.mpg"> </applet> -->
 *
 * @author Spike Barlow
 ******************************************************************************/
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.net.*;
import java.io.*;
import java.util.*;
import javax.media.*;
public class BBPApplet extends Applet implements ControllerListener {
  /***************************************************************************
   * Object to play the media. Only attribute that the Applet really needs.
   **************************************************************************/
  protected Player player;
  /***************************************************************************
   * The name of the media to be played.
   **************************************************************************/
  protected String nameOfMedia2Play;
  /***************************************************************************
   * Name of the Property field within the applet tage indicating the name of
   * the media to play.
   **************************************************************************/
  private static final String MEDIA_NAME_PROPERTY = "media2Play";
  /***************************************************************************
   * Object describing the location of the media to be played.
   **************************************************************************/
  protected MediaLocator locator;
  /***************************************************************************
   * Initialise the applet by attempting to create and start a Player object
   * capable of playing the media specified in the applet tag.
   **************************************************************************/
  public void init() {
    setLayout(new BorderLayout());
    setBackground(Color.lightGray);
    try {
      nameOfMedia2Play = (new URL(getDocumentBase(),
          getParameter(MEDIA_NAME_PROPERTY))).toExternalForm();
      locator = new MediaLocator(nameOfMedia2Play);
      player = Manager.createPlayer(locator);
      player.addControllerListener(this);
      player.start();
    } catch (Exception e) {
      throw new Error("Couldn't initialise BBPApplet: " + e.getMessage());
    }
  }
  /***************************************************************************
   * Respond to ControllerEvents from the Player that was created. For the
   * bare bones player the only event of import is the RealizeCompleteEvent.
   * At that stage the visual component and controller for the Player can
   * finally be obtained and thus displayed.
   **************************************************************************/
  public synchronized void controllerUpdate(ControllerEvent e) {
    if (e instanceof RealizeCompleteEvent) {
      add(player.getVisualComponent(), "North");
      add(player.getControlPanelComponent(), "South");
      validate();
    }
  }
}
```

Related examples in the same category
---
1. Java Media: Find Components
2. Query the manager class about the configuration and support of JMF
3. Show the Location2Location class in action
4. Capture audio or video through devices connected to the PC
5. Choose the media they wish to play
6. Do Audio Capture
7. Statistics about the tracks that compose a media object
8. Play the media object
9. Play the media object 3
10. List all capture devices currently known to the JMF
11. Transfer media from one location to another carrying out the specified
