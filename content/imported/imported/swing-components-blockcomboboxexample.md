---
title: Block ComboBox Example
nav: Block ComboBox Example
description: Block ComboBox Example : Java examples (example source code) » Swing Components » ComboBox
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20060702070456/http://www.java2s.com:80/Code/Java/Swing-Components/BlockComboBoxExample.htm
---
Block ComboBox Example : Java examples (example source code) » Swing Components » ComboBox

Block ComboBox Example

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
/* (swing1.1) */
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Vector;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JSeparator;
import javax.swing.ListCellRenderer;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;
/**
 * @version 1.0 12/25/98
 */
public class BlockComboBoxExample extends JFrame {
  final String SEPARATOR = "SEPARATOR";
  public BlockComboBoxExample() {
    super("Block ComboBox Example");
    String[][] str = { { "A", "B", "C" }, { "1", "2", "3" },
        { "abc", "def", "ghi" } };
    JComboBox combo = new JComboBox(makeVectorData(str));
    combo.setRenderer(new ComboBoxRenderer());
    combo.addActionListener(new BlockComboListener(combo));
    getContentPane().setLayout(new FlowLayout());
    getContentPane().add(combo);
    setSize(300, 100);
    setVisible(true);
  }
  private Vector makeVectorData(String[][] str) {
    boolean needSeparator = false;
    Vector data = new Vector();
    for (int i = 0; i < str.length; i++) {
      if (needSeparator) {
        data.addElement(SEPARATOR);
      }
      for (int j = 0; j < str[i].length; j++) {
        data.addElement(str[i][j]);
        needSeparator = true;
      }
    }
    return data;
  }
  public static void main(String args[]) {
    try {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
    } catch (Exception evt) {}
    BlockComboBoxExample frame = new BlockComboBoxExample();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
  }
  class ComboBoxRenderer extends JLabel implements ListCellRenderer {
    JSeparator separator;
    public ComboBoxRenderer() {
      setOpaque(true);
      setBorder(new EmptyBorder(1, 1, 1, 1));
      separator = new JSeparator(JSeparator.HORIZONTAL);
    }
    public Component getListCellRendererComponent(JList list, Object value,
        int index, boolean isSelected, boolean cellHasFocus) {
      String str = (value == null) ? "" : value.toString();
      if (SEPARATOR.equals(str)) {
        return separator;
      }
      if (isSelected) {
        setBackground(list.getSelectionBackground());
        setForeground(list.getSelectionForeground());
      } else {
        setBackground(list.getBackground());
        setForeground(list.getForeground());
      }
      setFont(list.getFont());
      setText(str);
      return this;
    }
  }
  class BlockComboListener implements ActionListener {
    JComboBox combo;
    Object currentItem;
    BlockComboListener(JComboBox combo) {
      this.combo = combo;
      combo.setSelectedIndex(0);
      currentItem = combo.getSelectedItem();
    }
    public void actionPerformed(ActionEvent e) {
      String tempItem = (String) combo.getSelectedItem();
      if (SEPARATOR.equals(tempItem)) {
        combo.setSelectedItem(currentItem);
      } else {
        currentItem = tempItem;
      }
    }
  }
}
```

Related examples in the same category
---
1. Swing Table in ComboBox
2. ComboBox color chooser (Windows Color Chooser)
3. MSN like Swing ComboBox
4. Swing Auto Complete ComboBox
5. Auto complete ComboBox
6. Stepped ComboBox Example
7. Disabled ComboBox Example
8. ToolTip ComboBox Example
9. ComboBox Menu Example
10. Small Cell Combobox Example
11. JComboBox: adding automatic completion-Catching user input
12. JComboBox: adding automatic completion-Adding automatic selection
13. JComboBox: adding automatic completion-Adding automatic completion
14. JComboBox: adding automatic completion-Fixed Auto Selection
15. JComboBox: adding automatic completion-Case insensitive matching
16. JComboBox: adding automatic completion-Prefer the currently selected item
17. JComboBox: adding automatic completion-Ignore input that does not match
18. JComboBox: adding automatic completion-Highlight complete text
19. JComboBox: adding automatic completion-Popup the item list
20. JComboBox: adding automatic completion-Cursor position
21. JComboBox: adding automatic completion-Handling the initial selection
22. JComboBox: adding automatic completion-Handling focus loss
23. JComboBox: adding automatic completion-Backspace
24. JComboBox: adding automatic completion-Backspace 2
25. JComboBox: adding automatic completion-Pressing backspace at the beginning
26. JComboBox: adding automatic completion-Maximum Match
27. JComboBox: adding automatic completion-Non-strict matching
28. JComboBox: adding automatic completion-Non-strict matching 2
29. JComboBox: adding automatic completion-Binary Lookup and Performance
30. JComboBox: adding automatic completion-Binay Lookup 2
