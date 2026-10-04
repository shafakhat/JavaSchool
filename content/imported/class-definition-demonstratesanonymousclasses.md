---
title: Demonstrates anonymous classes
nav: Demonstrates anonymous cla...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1110
source: https://web.archive.org/web/20140829083034/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratesanonymousclasses.htm
---
```java title=Example.java
/*
 *     file: InnerClassDemo.java
 *  package: oreilly.hcj.nested
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
 ########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class InnerClassDemo extends JDialog {
  /** Holds the logo image */
  private static final ImageIcon LOGO;
  /** Holds the location of the logo image. */
  private static final String LOGO_LOCATION = "sojm/nested/oreilly_header3.gif";
  static {
    LOGO = new ImageIcon(ClassLoader.getSystemClassLoader().getResource(LOGO_LOCATION));
  }
  /** Holds a reference to the content pane. */
  private final Container contentPane;
  /** holds a demo variable. */
  private int beepCount = 1;
  /**
   * Creates a new AnonymousDemo object.
   *
   * @param beepCount
   *          THe number of times to beep when the button is pressed.
   */
  public InnerClassDemo(final int beepCount) {
    super();
    setTitle("Anonymous Demo");
    contentPane = getContentPane();
    contentPane.setLayout(new BorderLayout());
    JLabel logoLabel = new JLabel(LOGO);
    contentPane.add(BorderLayout.NORTH, logoLabel);
    JButton btn = new BeepButton("Beep");
    contentPane.add(BorderLayout.SOUTH, btn);
    pack();
    this.beepCount = beepCount;
  }
  /**
   * Setter for the property demo.
   *
   * @param beepCount
   *          The new value for demo.
   */
  public void setBeepCount(final int beepCount) {
    this.beepCount = beepCount;
  }
  /**
   * Getter for the property demo.
   *
   * @return The current value of demo.
   */
  public int getBeepCount() {
    return beepCount;
  }
  /**
   * Run the demo
   *
   * @param args
   *          Command Line Arguments.
   */
  public static final void main(final String[] args) {
    InnerClassDemo demo = new InnerClassDemo(4);
    demo.show();
    System.out.println("Done");
  }
  /**
   * An inner class to implement an action listener.
   *
   * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
   * @version $Revision: 1.3 $
   */
  private class BeepButton extends JButton implements ActionListener {
    /**
     * Creates a new BeepButton object.
     *
     * @param text
     *          The text to use for the beep button.
     */
    public BeepButton(final String text) {
      super(text);
      addActionListener(this);
    }
    /**
     * @see java.awt.event.ActionListener
     */
    public void actionPerformed(final ActionEvent event) {
      try {
        for (int count = 0; count < beepCount; count++) {
          Toolkit.getDefaultToolkit().beep();
          Thread.sleep(100); // wait for the old beep to finish.
        }
      } catch (final InterruptedException ex) {
        throw new RuntimeException(ex);
      }
    }
  }
}
/* ########## End of File ########## */
```

| 5.15.1. | Demonstrate an inner class. |
|---|---|
| 5.15.2. | Define an inner class within a for loop. |
| 5.15.3. | Use anonymous inner classes |
| 5.15.4. | Building the anonymous inner class in-place |
| 5.15.5. | Anonymous inner class cannot have a named constructor, only an instance initializer |
| 5.15.6. | Creating a constructor for an anonymous inner class |
| 5.15.7. | Using 'instance initialization' to perform construction on an anonymous inner class |
| 5.15.8. | Argument must be final to use inside anonymous inner class |
| 5.15.9. | A method that returns an anonymous inner class |
| 5.15.10. | An anonymous inner class that calls the base-class constructor |
| 5.15.11. | An anonymous inner class that performs initialization |
| 5.15.12. | Demonstrates method-scoped inner classes |
| 5.15.13. | Demonstrates anonymous classes |
| 5.15.14. | Demonstration of some static nested classes |
| 5.15.15. | Access inner class from outside |
| 5.15.16. | Accessing its enclosing instance from an inner class |
