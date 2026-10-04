---
title: Uses the JNLP API to open and save files
nav: Uses the JNLP API to open ...
description: * Copyright (c) 1998 Sun Microsystems, Inc. All Rights Reserved.
section: Imported - java2s Archive
order: 1818
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0120__Development/UsestheJNLPAPItoopenandsavefiles.htm
---
```java title=Example.java
/*
 *
 * Copyright (c) 1998 Sun Microsystems, Inc. All Rights Reserved.
 *
 * Sun grants you ("Licensee") a non-exclusive, royalty free, license to use,
 * modify and redistribute this software in source and binary code form,
 * provided that i) this copyright notice and license appear on all copies of
 * the software; and ii) Licensee does not utilize the software in a manner
 * which is disparaging to Sun.
 *
 * This software is provided "AS IS," without a warranty of any kind. ALL
 * EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY
 * IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR
 * NON-INFRINGEMENT, ARE HEREBY EXCLUDED. SUN AND ITS LICENSORS SHALL NOT BE
 * LIABLE FOR ANY DAMAGES SUFFERED BY LICENSEE AS A RESULT OF USING, MODIFYING
 * OR DISTRIBUTING THE SOFTWARE OR ITS DERIVATIVES. IN NO EVENT WILL SUN OR ITS
 * LICENSORS BE LIABLE FOR ANY LOST REVENUE, PROFIT OR DATA, OR FOR DIRECT,
 * INDIRECT, SPECIAL, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER
 * CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF THE USE OF
 * OR INABILITY TO USE SOFTWARE, EVEN IF SUN HAS BEEN ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGES.
 *
 * This software is not designed or intended for use in on-line control of
 * aircraft, air traffic, aircraft navigation or aircraft communications; or in
 * the design, construction, operation or maintenance of any nuclear
 * facility. Licensee represents and warrants that it will not use or
 * redistribute the Software for such purposes.
 */import java.io.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.filechooser.*;
import javax.jnlp.*;
public class JWSFileChooserDemo extends JPanel
                                implements ActionListener {
    static private final String newline = "\n";
    JButton openButton, saveButton;
    JTextArea log;
    public JWSFileChooserDemo() {
        super(new BorderLayout());
        //Create the log first, because the action listeners
 //need to refer to it.
        log = new JTextArea(5,20);
        log.setMargin(new Insets(5,5,5,5));
        log.setEditable(false);
        JScrollPane logScrollPane = new JScrollPane(log);
        //Create the open button.  We use the image from the JLF
 //Graphics Repository (but we extracted it from the jar).
        openButton = new JButton("Open a File...",
                                 createImageIcon("images/Open16.gif"));
        openButton.addActionListener(this);
        //Create the save button.  We use the image from the JLF
 //Graphics Repository (but we extracted it from the jar).
        saveButton = new JButton("Save a File...",
                                 createImageIcon("images/Save16.gif"));
        //PENDING: removed the Save button action listener
 //so that people won't overwrite existing files.
 //See bug 4761577.
 //saveButton.addActionListener(this);
        saveButton.setEnabled(false);
        //For layout purposes, put the buttons in a separate panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(openButton);
        buttonPanel.add(saveButton);
        //Add the buttons and the log to this panel.
        add(buttonPanel, BorderLayout.PAGE_START);
        add(logScrollPane, BorderLayout.CENTER);
    }
    public void actionPerformed(ActionEvent e) {
        //Handle open button action.
 if (e.getSource() == openButton) {
            FileOpenService fos = null;
            FileContents fileContents = null;
            try {
                fos = (FileOpenService)ServiceManager.
                          lookup("javax.jnlp.FileOpenService");
            } catch (UnavailableServiceException exc) { }
            if (fos != null) {
                try {
                    fileContents = fos.openFileDialog(null, null);
                } catch (Exception exc) {
                    log.append("Open command failed: "
                               + exc.getLocalizedMessage()
                               + newline);
                    log.setCaretPosition(log.getDocument().getLength());
                }
            }
            if (fileContents != null) {
                try {
                    //This is where a real application would do something
 //with the file.
                    log.append("Opened file: " + fileContents.getName()
                               + "." + newline);
                } catch (IOException exc) {
                    log.append("Problem opening file: "
                               + exc.getLocalizedMessage()
                               + newline);
                }
            } else {
                log.append("User canceled open request." + newline);
            }
            log.setCaretPosition(log.getDocument().getLength());
        }
        //Handle save button action.
 if (e.getSource() == saveButton) {
            FileSaveService fss = null;
            FileContents fileContents = null;
            ByteArrayInputStream is = new ByteArrayInputStream(
                    (new String("Saved by JWSFileChooserDemo").getBytes()));
                                             //XXX YIKES! If they select an
 //XXX existing file, this will
 //XXX overwrite that file.
 try {
                fss = (FileSaveService)ServiceManager.
                          lookup("javax.jnlp.FileSaveService");
            } catch (UnavailableServiceException exc) { }
            if (fss != null) {
                try {
                    fileContents = fss.saveFileDialog(null,
                                                      null,
                                                      is,
                                                      "JWSFileChooserDemo.txt");
                } catch (Exception exc) {
                    log.append("Save command failed: "
                               + exc.getLocalizedMessage()
                               + newline);
                    log.setCaretPosition(log.getDocument().getLength());
                }
            }
            if (fileContents != null) {
                try {
                    log.append("Saved file: " + fileContents.getName()
                               + "." + newline);
                } catch (IOException exc) {
                    log.append("Problem saving file: "
                               + exc.getLocalizedMessage()
                               + newline);
                }
            } else {
                log.append("User canceled save request." + newline);
            }
            log.setCaretPosition(log.getDocument().getLength());
        }
    }
    /** Returns an ImageIcon, or null if the path was invalid. */ protected static ImageIcon createImageIcon(String path) {
        java.net.URL imgURL = JWSFileChooserDemo.class.getResource(path);
        if (imgURL != null) {
            return new ImageIcon(imgURL);
        } else {
            System.err.println("Couldn't find file: " + path);
            return null;
        }
    }
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */ private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("JWSFileChooserDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //Create and set up the content pane.
        JComponent newContentPane = new JWSFileChooserDemo();
        newContentPane.setOpaque(true); //content panes must be opaque
        frame.setContentPane(newContentPane);
        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }
    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
 //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
```
