---
title: Java AbstractAction create action for JButton
nav: Java AbstractAction create...
description: JButton closeButton1;/*www.java2s.com*/Action closeAction = new CloseAction();
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20210102122120/http://www.java2s.com/ref/java/java-abstractaction-create-action-for-jbutton.html
---
- javax.swing
- javax.swing AbstractAction Action ActionMap BorderFactory BoundedRangeModel Box BoxLayout ButtonGroup DefaultComboBoxModel DefaultListCellRenderer DefaultListModel GroupLayout Icon ImageIcon InputMap InputVerifier JButton JCheckBox JCheckBoxMenuItem JColorChooser JComboBox JComponent JDesktopPane JDialog JEditorPane JFileChooser JFormattedTextField JFrame JInternalFrame JLabel JLayer JList JMenu JMenuItem JOptionPane JPanel JPasswordField JPopupMenu JProgressBar JRadioButton JRadioButtonMenuItem JRootPane JScrollBar JScrollPane JSlider JSpinner JTabbedPane JTable JTextArea JTextField JTextPane JToggleButton JToolBar JTree KeyStroke ListSelectionModel SpinnerDateModel SpinnerListModel SpinnerModel SpinnerNumberModel SpringLayout SwingUtilities SwingWorker Timer ToolTipManager UIManager

## Description

Java AbstractAction create action for JButton

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  public Main() {
    super("Action object with JButton");

    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setLayout(newFlowLayout());

    JButton closeButton1;/*www.java2s.com*/Action closeAction = new CloseAction();

    closeButton1 = newJButton(closeAction);

    getContentPane().add(closeButton1);
  }

  publicstaticvoid main(String[] args) {
    Main frame = new Main();
    frame.pack();
    frame.setVisible(true);
  }
}

class CloseAction extendsAbstractAction {
  public CloseAction() {
    super("Close");
  }

  @Overridepublicvoid actionPerformed(ActionEvent event) {
    System.exit(0);
  }
}
```

PreviousNext

## Related

- Java AWT PrinterJob set print dialog box type
- Java AWT PrinterJob print custom component
- Java AWT Printable implement
- Java AbstractAction set mnemonic key
- Java AbstractAction set tool tip text
