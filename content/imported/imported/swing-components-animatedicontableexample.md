---
title: Animated Icon Table Example
nav: Animated Icon Table Example
description: // Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20070129131744/http://www.java2s.com:80/Code/Java/Swing-Components/AnimatedIconTableExample.htm
---
Animated Icon Table Example

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
/* (swing1.1.1beta2) */
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.image.ImageObserver;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.UIManager;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.TableModel;
/**
 * @version 1.0 06/19/99
 */
public class AnimatedIconTableExample extends JFrame {
  public AnimatedIconTableExample() {
    super("AnimatedIconTable Example");
    final Object[][] data = new Object[][] {
        { new ImageIcon("Java2sAnimation.gif"),
            new ImageIcon("Java2sAnimation.gif") },
        { new ImageIcon("Java2sAnimation.gif"),
            new ImageIcon("Java2sAnimation.gif") } };
    final Object[] column = new Object[] { "Boy and Girl", "Dog and Cat" };
    AbstractTableModel model = new AbstractTableModel() {
      public int getColumnCount() {
        return column.length;
      }
      public int getRowCount() {
        return data.length;
      }
      public String getColumnName(int col) {
        return (String) column[col];
      }
      public Object getValueAt(int row, int col) {
        return data[row][col];
      }
      public Class getColumnClass(int col) {
        return ImageIcon.class;
      }
    };
    JTable table = new JTable(model);
    table.setRowHeight(50);
    setImageObserver(table);
    JScrollPane pane = new JScrollPane(table);
    getContentPane().add(pane);
  }
  private void setImageObserver(JTable table) {
    TableModel model = table.getModel();
    int colCount = model.getColumnCount();
    int rowCount = model.getRowCount();
    for (int col = 0; col < colCount; col++) {
      if (ImageIcon.class == model.getColumnClass(col)) {
        for (int row = 0; row < rowCount; row++) {
          ImageIcon icon = (ImageIcon) model.getValueAt(row, col);
          if (icon != null) {
            icon.setImageObserver(new CellImageObserver(table, row,
                col));
          }
        }
      }
    }
  }
  class CellImageObserver implements ImageObserver {
    JTable table;
    int row;
    int col;
    CellImageObserver(JTable table, int row, int col) {
      this.table = table;
      this.row = row;
      this.col = col;
    }
    public boolean imageUpdate(Image img, int flags, int x, int y, int w,
        int h) {
      if ((flags & (FRAMEBITS | ALLBITS)) != 0) {
        Rectangle rect = table.getCellRect(row, col, false);
        table.repaint(rect);
      }
      return (flags & (ALLBITS | ABORT)) == 0;
    }
  }
  public static void main(String[] args) {
    AnimatedIconTableExample frame = new AnimatedIconTableExample();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    frame.setSize(300, 150);
    frame.setVisible(true);
  }
}
```

Related examples in the same category
---
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
25. Button Table Example
26. Radio Button Table Example
27. RadioButton Table Example 2
28. MultiLine Cell Example
29. Each Row with different Editor Example
30. multiple Component Table: Checkbox and comobobx
31. multiple Component Table 2: checkbox
32. Union Data Table Example
33. Total(Calculate) Row Example
34. Colored Cell Table Example
35. multiple Font Cell Table Example
36. Multi Span Cell Table Example
37. Mixed Table Example
38. Pushable Table Header Example
39. Sortable Table Example
40. ToolTip Header Table Example
41. Indicator Table Example
42. Fixed Table Row Example
43. multiple Row Header Example
44. Column Border Table Example
45. Cell Border Table Example
46. Hide Column Table Example
47. Animated Icon Header Example
48. Editable Header Table Example
49. Editable Header Table Example 2
