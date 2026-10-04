---
title: Calculated Column Table
nav: Calculated Column Table
description: Calculated Column Table : Java examples (example source code) » Swing Components » Grid Table
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20060513064752/http://www.java2s.com/Code/Java/Swing-Components/CalculatedColumnTable.htm
---
Calculated Column Table : Java examples (example source code) » Swing Components » Grid Table

```java title=Example.java
/*
Core SWING Advanced Programming
By Kim Topley
ISBN: 0 13 083292 8
Publisher: Prentice Hall
*/
import java.awt.Component;
import java.awt.Insets;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.text.NumberFormat;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.TableCellRenderer;
import javax.swing.table.TableColumn;
import javax.swing.table.TableColumnModel;
public class CalculatedColumnTable {
  public static void main(String[] args) {
    try {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
    } catch (Exception evt) {}
    JFrame f = new JFrame("Calculated Column Table");
    JTable tbl = new JTable(new CurrencyTableModel());
    tbl.setDefaultRenderer(java.lang.Number.class,
        new FractionCellRenderer(10, 3, SwingConstants.RIGHT));
    TableColumnModel tcm = tbl.getColumnModel();
    TextWithIconCellRenderer renderer = new TextWithIconCellRenderer();
    tcm.getColumn(0).setCellRenderer(renderer);
    // Automatically configure the column widths
    TableUtilities
        .setColumnWidths(tbl, new Insets(0, 4, 0, 4), true, false);
    tbl.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
    tbl.setPreferredScrollableViewportSize(tbl.getPreferredSize());
    // Diagnostics: display the chosen column widths
    for (int i = 0; i < tcm.getColumnCount(); i++) {
      System.out.println("Column " + i + ": width is "
          + tcm.getColumn(i).getPreferredWidth());
    }
    JScrollPane sp = new JScrollPane(tbl);
    f.getContentPane().add(sp, "Center");
    f.pack();
    f.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent evt) {
        System.exit(0);
      }
    });
    f.setVisible(true);
  }
}
class DataWithIcon {
  public DataWithIcon(Object data, Icon icon) {
    this.data = data;
    this.icon = icon;
  }
  public Icon getIcon() {
    return icon;
  }
  public Object getData() {
    return data;
  }
  public String toString() {
    return data.toString();
  }
  protected Icon icon;
  protected Object data;
}
class CurrencyTableModel extends AbstractTableModel {
  protected String[] columnNames = { "Currency", "Yesterday", "Today",
      "Change" };
  // Constructor: calculate currency change to create the last column
  public CurrencyTableModel() {
    for (int i = 0; i < data.length; i++) {
      data[i][DIFF_COLUMN] = new Double(
          ((Double) data[i][NEW_RATE_COLUMN]).doubleValue()
              - ((Double) data[i][OLD_RATE_COLUMN]).doubleValue());
    }
  }
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
  protected static final int OLD_RATE_COLUMN = 1;
  protected static final int NEW_RATE_COLUMN = 2;
  protected static final int DIFF_COLUMN = 3;
  protected static final int COLUMN_COUNT = 4;
  protected static final Class thisClass = CurrencyTableModel.class;
  protected Object[][] data = new Object[][] {
      {
          new DataWithIcon("Belgian Franc", new ImageIcon(thisClass
              .getResource("belgium.gif"))),
          new Double(37.6460110), new Double(37.6508921), null },
      {
          new DataWithIcon("British Pound", new ImageIcon(thisClass
              .getResource("gb.gif"))), new Double(0.6213051),
          new Double(0.6104102), null },
      {
          new DataWithIcon("Canadian Dollar", new ImageIcon(thisClass
              .getResource("canada.gif"))),
          new Double(1.4651209), new Double(1.5011104), null },
      {
          new DataWithIcon("French Franc", new ImageIcon(thisClass
              .getResource("france.gif"))),
          new Double(6.1060001), new Double(6.0100101), null },
      {
          new DataWithIcon("Italian Lire", new ImageIcon(thisClass
              .getResource("italy.gif"))),
          new Double(1181.3668977), new Double(1182.104), null },
      {
          new DataWithIcon("German Mark", new ImageIcon(thisClass
              .getResource("germany.gif"))),
          new Double(1.8191804), new Double(1.8223421), null },
      {
          new DataWithIcon("Japanese Yen", new ImageIcon(thisClass
              .getResource("japan.gif"))),
          new Double(141.0815412), new Double(121.0040432), null } };
}
class FractionCellRenderer extends DefaultTableCellRenderer {
  public FractionCellRenderer(int integer, int fraction, int align) {
    this.integer = integer; // maximum integer digits
    this.fraction = fraction; // exact number of fraction digits
    this.align = align; // alignment (LEFT, CENTER, RIGHT)
  }
  protected void setValue(Object value) {
    if (value != null && value instanceof Number) {
      formatter.setMaximumIntegerDigits(integer);
      formatter.setMaximumFractionDigits(fraction);
      formatter.setMinimumFractionDigits(fraction);
      setText(formatter.format(((Number) value).doubleValue()));
    } else {
      super.setValue(value);
    }
    setHorizontalAlignment(align);
  }
  protected int integer;
  protected int fraction;
  protected int align;
  protected static NumberFormat formatter = NumberFormat.getInstance();
}
class TextWithIconCellRenderer extends DefaultTableCellRenderer {
  protected void setValue(Object value) {
    if (value instanceof DataWithIcon) {
      if (value != null) {
        DataWithIcon d = (DataWithIcon) value;
        Object dataValue = d.getData();
        setText(dataValue == null ? "" : dataValue.toString());
        setIcon(d.getIcon());
        setHorizontalTextPosition(SwingConstants.RIGHT);
        setVerticalTextPosition(SwingConstants.CENTER);
        setHorizontalAlignment(SwingConstants.LEFT);
        setVerticalAlignment(SwingConstants.CENTER);
      } else {
        setText("");
        setIcon(null);
      }
    } else {
      super.setValue(value);
    }
  }
}
class TableUtilities {
  // Calculate the required width of a table column
  public static int calculateColumnWidth(JTable table, int columnIndex) {
    int width = 0; // The return value
    int rowCount = table.getRowCount();
    for (int i = 0; i < rowCount; i++) {
      TableCellRenderer renderer = table.getCellRenderer(i, columnIndex);
      Component comp = renderer.getTableCellRendererComponent(table,
          table.getValueAt(i, columnIndex), false, false, i,
          columnIndex);
      int thisWidth = comp.getPreferredSize().width;
      if (thisWidth > width) {
        width = thisWidth;
      }
    }
    return width;
  }
  // Set the widths of every column in a table
  public static void setColumnWidths(JTable table, Insets insets,
      boolean setMinimum, boolean setMaximum) {
    int columnCount = table.getColumnCount();
    TableColumnModel tcm = table.getColumnModel();
    int spare = (insets == null ? 0 : insets.left + insets.right);
    for (int i = 0; i < columnCount; i++) {
      int width = calculateColumnWidth(table, i);
      width += spare;
      TableColumn column = tcm.getColumn(i);
      column.setPreferredWidth(width);
      if (setMinimum == true) {
        column.setMinWidth(width);
      }
      if (setMaximum == true) {
        column.setMaxWidth(width);
      }
    }
  }
  // Sort an array of integers in place
  public static void sort(int[] values) {
    int length = values.length;
    if (length > 1) {
      for (int i = 0; i < length - 1; i++) {
        for (int j = i + 1; j < length; j++) {
          if (values[j] < values[i]) {
            int temp = values[i];
            values[i] = values[j];
            values[j] = temp;
          }
        }
      }
    }
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
11. Table Utilities
12. Fraction Currency Table
13. Highlight Currency Table
14. Highlight Currency Table 2
15. MultiLine Table
16. Updatable Highlight Currency Table
17. Editable Highlight Currency Table
18. ComboBox Table
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
