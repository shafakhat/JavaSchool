---
title: Button Table Example
nav: Button Table Example
description: Button Table Example : Java examples (example source code) » Swing Components » Grid Table
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20060513064955/http://www.java2s.com/Code/Java/Swing-Components/ButtonTableExample.htm
---
Button Table Example : Java examples (example source code) » Swing Components » Grid Table

Button Table Example

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.DefaultCellEditor;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.UIManager;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellRenderer;
/**
 * @version 1.0 11/09/98
 */
public class JButtonTableExample extends JFrame {
  public JButtonTableExample() {
    super("JButtonTable Example");
    DefaultTableModel dm = new DefaultTableModel();
    dm.setDataVector(new Object[][] { { "button 1", "foo" },
        { "button 2", "bar" } }, new Object[] { "Button", "String" });
    JTable table = new JTable(dm);
    table.getColumn("Button").setCellRenderer(new ButtonRenderer());
    table.getColumn("Button").setCellEditor(
        new ButtonEditor(new JCheckBox()));
    JScrollPane scroll = new JScrollPane(table);
    getContentPane().add(scroll);
    setSize(400, 100);
    setVisible(true);
  }
  public static void main(String[] args) {
    JButtonTableExample frame = new JButtonTableExample();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
  }
}
/**
 * @version 1.0 11/09/98
 */
class ButtonRenderer extends JButton implements TableCellRenderer {
  public ButtonRenderer() {
    setOpaque(true);
  }
  public Component getTableCellRendererComponent(JTable table, Object value,
      boolean isSelected, boolean hasFocus, int row, int column) {
    if (isSelected) {
      setForeground(table.getSelectionForeground());
      setBackground(table.getSelectionBackground());
    } else {
      setForeground(table.getForeground());
      setBackground(UIManager.getColor("Button.background"));
    }
    setText((value == null) ? "" : value.toString());
    return this;
  }
}
/**
 * @version 1.0 11/09/98
 */
class ButtonEditor extends DefaultCellEditor {
  protected JButton button;
  private String label;
  private boolean isPushed;
  public ButtonEditor(JCheckBox checkBox) {
    super(checkBox);
    button = new JButton();
    button.setOpaque(true);
    button.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        fireEditingStopped();
      }
    });
  }
  public Component getTableCellEditorComponent(JTable table, Object value,
      boolean isSelected, int row, int column) {
    if (isSelected) {
      button.setForeground(table.getSelectionForeground());
      button.setBackground(table.getSelectionBackground());
    } else {
      button.setForeground(table.getForeground());
      button.setBackground(table.getBackground());
    }
    label = (value == null) ? "" : value.toString();
    button.setText(label);
    isPushed = true;
    return button;
  }
  public Object getCellEditorValue() {
    if (isPushed) {
      //
      //
      JOptionPane.showMessageDialog(button, label + ": Ouch!");
      // System.out.println(label + ": Ouch!");
    }
    isPushed = false;
    return new String(label);
  }
  public boolean stopCellEditing() {
    isPushed = false;
    return super.stopCellEditing();
  }
  protected void fireEditingStopped() {
    super.fireEditingStopped();
  }
}
```

Related examples in the same category
---
1. HyperLink in Table
2. Column popup menu
3. Tree Table
4. Swing Table in ComboBox
5. Tabbable Currency Table
6. Icon Currency Table
7. MultiLine Header Table
8. ToolTip Table
9. Striped Currency Table
10. CurrencyTable
11. Calculated Column Table
12. Table Utilities
13. Fraction Currency Table
14. Highlight Currency Table
15. Highlight Currency Table 2
16. MultiLine Table
17. Updatable Highlight Currency Table
18. Editable Highlight Currency Table
19. ComboBox Table
20. Groupable(Group) Header Example
21. MultiWidth Header Example
22. MultiLine Header Example
23. Table Row Header Example
24. Fixed Table Column Example
25. Radio Button Table Example
26. RadioButton Table Example 2
27. MultiLine Cell Example
28. Each Row with different Editor Example
29. multiple Component Table: Checkbox and comobobx
30. multiple Component Table 2: checkbox
31. Union Data Table Example
32. Total(Calculate) Row Example
33. Colored Cell Table Example
34. multiple Font Cell Table Example
35. Multi Span Cell Table Example
36. Mixed Table Example
37. Pushable Table Header Example
38. Sortable Table Example
39. ToolTip Header Table Example
40. Indicator Table Example
41. Fixed Table Row Example
42. multiple Row Header Example
43. Column Border Table Example
44. Cell Border Table Example
45. Hide Column Table Example
46. Animated Icon Table Example
47. Animated Icon Header Example
48. Editable Header Table Example
49. Editable Header Table Example 2
