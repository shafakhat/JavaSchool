---
title: Demonstrates method-scoped inner classes
nav: Demonstrates method-scoped...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1107
source: https://web.archive.org/web/20140829082933/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratesmethodscopedinnerclasses.htm
---
```java title=Example.java
/*
 *     file: MethodInnerClassDemo.java
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
import java.awt.GridLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.6 $
 */
public class MethodInnerClassDemo extends JDialog {
  /** Holds the logo image */
  private static final ImageIcon LOGO;
  /** Holds the location of the logo image. */
  private static final String LOGO_LOCATION = "oreilly/hcj/nested/oreilly_header3.gif";
  static {
    LOGO = new ImageIcon(ClassLoader.getSystemClassLoader().getResource(LOGO_LOCATION));
  }
  /** Holds a reference to the content pane. */
  private final Container contentPane;
  /** holds a demo variable. */
  private String demo;
  /**
   * Creates a new MethodInnerClassDemo object.
   *
   * @param value
   *          Some value to be used.
   */
  public MethodInnerClassDemo(final int value) {
    super();
    String title = "Inner Class Demo";
    setTitle(title);
    setModal(true);
    contentPane = getContentPane();
    contentPane.setLayout(new BorderLayout());
    JLabel logoLabel = new JLabel(LOGO);
    contentPane.add(BorderLayout.NORTH, logoLabel);
    JButton btn = new JButton("Beep");
    /**
     * An action listener class.
     *
     * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
     * @version $Revision: 1.6 $
     */
    class MyActionListener implements ActionListener {
      /**
       * {@inheritDoc}
       */
      public void actionPerformed(final ActionEvent event) {
        Toolkit.getDefaultToolkit().beep();
        System.out.println(value);
        System.out.println(MethodInnerClassDemo.LOGO_LOCATION);
        System.out.println(MethodInnerClassDemo.this.demo);
        // System.out.println(title); // <= compiler error
      }
    }
    btn.addActionListener(new MyActionListener());
    contentPane.add(BorderLayout.SOUTH, btn);
    pack();
  }
  /**
   * Creates a new MethodInnerClassDemo object.
   */
  public MethodInnerClassDemo() {
    super();
    setTitle("Inner Class Demo");
    setModal(true);
    contentPane = getContentPane();
    contentPane.setLayout(new BorderLayout());
    JLabel logoLabel = new JLabel(LOGO);
    contentPane.add(BorderLayout.NORTH, logoLabel);
    JButton btn1 = new JButton("Beep");
    JButton btn2 = new JButton("Bell");
    /**
     * An action listener class.
     *
     * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
     * @version $Revision: 1.6 $
     */
    class MyActionListener implements ActionListener {
      /**
       * {@inheritDoc}
       */
      public void actionPerformed(final ActionEvent event) {
        Toolkit.getDefaultToolkit().beep();
      }
    }
    btn1.addActionListener(new MyActionListener());
    btn2.addActionListener(new MyActionListener());
    JPanel pnl = new JPanel(new GridLayout(1, 2));
    pnl.add(btn1);
    pnl.add(btn2);
    contentPane.add(BorderLayout.SOUTH, pnl);
    pack();
  }
  /**
   * Run the demo
   *
   * @param args
   *          Command Line Arguments.
   */
  public static final void main(final String[] args) {
    MethodInnerClassDemo demo = new MethodInnerClassDemo();
    demo.show();
    System.out.println("Done");
  }
  /**
   * Setter for the property demo.
   *
   * @param demo
   *          The new value for demo.
   */
  public void setDemo(final String demo) {
    this.demo = demo;
  }
  /**
   * Getter for the property demo.
   *
   * @return The current value of demo.
   */
  public String getDemo() {
    return demo;
  }
  /**
   * Some demo method.
   */
  public void someMethod() {
    // ActionListener listener = new MyActionListener(); // <= compiler error.
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
