---
title: Java AbstractAction transfer focus
nav: Java AbstractAction transf...
description: component.getInputMap(JComponent.WHEN_FOCUSED).put(KeyStroke.getKeyStroke("shift F2"),
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20210102122120/http://www.java2s.com/ref/java/java-abstractaction-transfer-focus.html
---
- javax.swing
- javax.swing AbstractAction Action ActionMap BorderFactory BoundedRangeModel Box BoxLayout ButtonGroup DefaultComboBoxModel DefaultListCellRenderer DefaultListModel GroupLayout Icon ImageIcon InputMap InputVerifier JButton JCheckBox JCheckBoxMenuItem JColorChooser JComboBox JComponent JDesktopPane JDialog JEditorPane JFileChooser JFormattedTextField JFrame JInternalFrame JLabel JLayer JList JMenu JMenuItem JOptionPane JPanel JPasswordField JPopupMenu JProgressBar JRadioButton JRadioButtonMenuItem JRootPane JScrollBar JScrollPane JSlider JSpinner JTabbedPane JTable JTextArea JTextField JTextPane JToggleButton JToolBar JTree KeyStroke ListSelectionModel SpinnerDateModel SpinnerListModel SpinnerModel SpinnerNumberModel SpringLayout SwingUtilities SwingWorker Timer ToolTipManager UIManager

## Description

Java AbstractAction transfer focus

```java title=Example.java
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.KeyStroke;

publicclass Main {
   publicstaticvoid main(String[] args) {
      JFrame f = newJFrame();

      JButton component = newJButton("OK");
      PrevFocusAction prevFocusAction = new PrevFocusAction();
      component.getInputMap(JComponent.WHEN_FOCUSED).put(KeyStroke.getKeyStroke("shift F2"),
          prevFocusAction.getValue(Action.NAME));
      /*fromwww.java2s.com*/
      component.getInputMap(JComponent.WHEN_FOCUSED).put(KeyStroke.getKeyStroke("shift SPACE"),
          prevFocusAction.getValue(Action.NAME));

      component.getActionMap().put(prevFocusAction.getValue(Action.NAME), prevFocusAction);

      f.getContentPane().setLayout(newFlowLayout());
      f.add(newJTextField(10));
      f.add(component);
      f.add(newJTextField(10));

      f.setSize(310, 200);
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setVisible(true);
   }
}

class PrevFocusAction extendsAbstractAction {
   PrevFocusAction() {
     super("Move Focus Backwards");
   }

   publicvoid actionPerformed(ActionEvent evt) {
     ((Component) evt.getSource()).transferFocusBackward();
   }
}
```

PreviousNext

## Related

- Java AbstractAction create action for JButton
- Java AbstractAction set mnemonic key
- Java AbstractAction set tool tip text
- Java Action attribute
- Java Action create
