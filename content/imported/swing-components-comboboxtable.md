---
title: ComboBox Table
nav: ComboBox Table
description: ComboBox Table : Java examples (example source code) » Swing Components » Grid Table
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20060513064838/http://www.java2s.com/Code/Java/Swing-Components/ComboBoxTable.htm
---
ComboBox Table : Java examples (example source code) » Swing Components » Grid Table

```java title=Example.java
/*
Core SWING Advanced Programming
By Kim Topley
ISBN: 0 13 083292 8
Publisher: Prentice Hall
*/
import javax.swing.*;
import javax.swing.table.*;
import java.awt.event.*;
public class ComboBoxTable {
  public static void main(String[] args) {
    try {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
    } catch (Exception evt) {}
    JFrame f = new JFrame("Combo Box Table");
    JTable tbl = new JTable(new ComboBoxTableModel());
    // Create the combo box editor
    JComboBox comboBox = new JComboBox(ComboBoxTableModel.getValidStates());
    comboBox.setEditable(true);
    DefaultCellEditor editor = new DefaultCellEditor(comboBox);
    // Assign the editor to the second column
    TableColumnModel tcm = tbl.getColumnModel();
    tcm.getColumn(1).setCellEditor(editor);
    // Set column widths
    tcm.getColumn(0).setPreferredWidth(200);
    tcm.getColumn(1).setPreferredWidth(100);
    // Set row heighht
    tbl.setRowHeight(20);
    tbl.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
    tbl.setPreferredScrollableViewportSize(tbl.getPreferredSize());
    f.getContentPane().add(new JScrollPane(tbl), "Center");
    f.pack();
    f.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent evt) {
        System.exit(0);
      }
    });
    f.setVisible(true);
  }
}
class ComboBoxTableModel extends AbstractTableModel {
  // Implementation of TableModel interface
  public int getRowCount() {
    return data.length;
  }
  public int getColumnCount() {
    return COLUMN_COUNT;
  }
  public Object getValueAt(int row, int column) {
    return data[row][column];
  }
  public Class getColumnClass(int column) {
    return (data[0][column]).getClass();
  }
  public String getColumnName(int column) {
    return columnNames[column];
  }
  public boolean isCellEditable(int row, int column) {
    return column == 1;
  }
  public void setValueAt(Object value, int row, int column) {
    if (isValidValue(value)) {
      data[row][column] = value;
      fireTableRowsUpdated(row, row);
    }
  }
  // Extra public methods
  public static String[] getValidStates() {
    return validStates;
  }
  // Protected methods
  protected boolean isValidValue(Object value) {
    if (value instanceof String) {
      String sValue = (String)value;
      for (int i = 0; i < validStates.length; i++) {
        if (sValue.equals(validStates[i])) {
          return true;
        }
      }
    }
    return false;
  }
  protected static final int COLUMN_COUNT = 2;
  protected static final String[] validStates = {
    "On order", "In stock", "Out of print"
  };
  protected Object[][] data = new Object[][] {
    { "Core Java Volume 1", validStates[0] },
    { "Core Java Volume 2", validStates[0] },
    { "Core Web Programming", validStates[0] },
    { "Core Visual Basic 5", validStates[0] },
    { "Core Java Foundation Classes", validStates[0] }
  };
  protected static final String[] columnNames = {
    "Book Name", "Status"
  };
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
19. Groupable(Group) Header Example
20. MultiWidth Header Example
21. MultiLine Header Example
22. Table Row Header Example
23. Fixed Table Column Example
24. Button Table Example
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
