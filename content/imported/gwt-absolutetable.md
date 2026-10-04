---
title: Absolute Table
nav: Absolute Table
description: * Licensed under the Apache License, Version 2.0 (the "License"); you may not
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20081204100429/http://www.java2s.com:80/Code/Java/GWT/AbsoluteTable.htm
---
Absolute Table

```java title=Example.java
/*
 * Copyright 2007 Sfeir, www.sfeir.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package com.java2s.gwt.client;
import com.google.gwt.user.client.ui.HasHorizontalAlignment.HorizontalAlignmentConstant;
import java.util.*;
import com.google.gwt.user.client.*;
import com.google.gwt.user.client.ui.*;
import com.google.gwt.core.client.*;
public class GWTClient implements EntryPoint{
  private RootPanel rootPanel = RootPanel.get();
  private SimpleTable table;
  private ArrayList arrayRows;
  private Column firstNameColumn;
  private Column lastNameColumn;
  private Column nameColumn;
  private Column birthdayColumn;
  private Column phoneNumberColumn;
  private Column emailColumn;
  public ArrayList generateArrayRows(int nbOfRows) {
    ArrayList arrayRows = new ArrayList();
    for (int i = 0; i < nbOfRows; i++) {
      PersonRow person = new PersonRow();
      person.setFirstName("first name " + i);
      person.setLastName("last name " + i);
      person.setBirthday(new Date(12345678l + i));
      person.setPhoneNumber("012 345 67" + i);
      person.setEmail("firstname" + i + ".lastname" + i + "@gmail.com");
      arrayRows.add(person);
    }
    System.out.println("row generation finished");
    return arrayRows;
  }
  public void initialiseColumns() {
    System.out.println("beginning column initialisation");
    firstNameColumn = new Column();
    firstNameColumn.setAlignment(HasHorizontalAlignment.ALIGN_LEFT);
    firstNameColumn.setProperty(PersonRow.FIRSTNAME_PROPERTY);
    firstNameColumn.setSortable(false);
    firstNameColumn.setText("First Name");
    firstNameColumn.setVisible(false);
    firstNameColumn.setWidth(100);
    lastNameColumn = new Column();
    lastNameColumn.setAlignment(HasHorizontalAlignment.ALIGN_LEFT);
    lastNameColumn.setProperty(PersonRow.LASTNAME_PROPERTY);
    lastNameColumn.setSortable(false);
    lastNameColumn.setText("Last Name");
    lastNameColumn.setVisible(false);
    lastNameColumn.setWidth(100);
    nameColumn = new Column();
    nameColumn.setAlignment(HasHorizontalAlignment.ALIGN_LEFT);
    nameColumn.setProperty(PersonRow.NAME_PROPERTY);
    nameColumn.setSortable(false);
    nameColumn.setText("Name");
    nameColumn.setVisible(true);
    nameColumn.setWidth(100);
    birthdayColumn = new Column();
    birthdayColumn.setAlignment(HasHorizontalAlignment.ALIGN_CENTER);
    birthdayColumn.setProperty(PersonRow.BIRTHDAY_PROPERTY);
    birthdayColumn.setSortable(false);
    birthdayColumn.setText("Birthday");
    birthdayColumn.setVisible(true);
    birthdayColumn.setWidth(100);
    phoneNumberColumn = new Column();
    phoneNumberColumn.setAlignment(HasHorizontalAlignment.ALIGN_CENTER);
    phoneNumberColumn.setProperty(PersonRow.PHONENUMBER_PROPERTY);
    phoneNumberColumn.setSortable(false);
    phoneNumberColumn.setText("Phone");
    phoneNumberColumn.setVisible(true);
    phoneNumberColumn.setWidth(100);
    emailColumn = new Column();
    emailColumn.setAlignment(HasHorizontalAlignment.ALIGN_LEFT);
    emailColumn.setProperty(PersonRow.EMAIL_PROPERTY);
    emailColumn.setSortable(false);
    emailColumn.setText("E-mail");
    emailColumn.setVisible(true);
    emailColumn.setWidth(100);
    System.out.println("column initialisation finished");
  }
  public void initialiseTable() {
    table = new SimpleTable();
    Table.setCHARACTER_SIZE(8);
    Table.setROWS_HEIGHT(20);
    initialiseColumns();
    table.add(firstNameColumn);
    table.add(lastNameColumn);
    table.add(nameColumn);
    table.add(birthdayColumn);
    table.add(phoneNumberColumn);
    table.add(emailColumn);
    arrayRows = generateArrayRows(10);
    table.setArrayRows(arrayRows);
    rootPanel.add(table);
  }
  public void onModuleLoad() {
    initialiseTable();
    System.out.println("beginning table drawing");
    table.draw();
    System.out.println("table drawing finished");
  }
}
class PersonRow implements Row {
  public static final String FIRSTNAME_PROPERTY = "first name";
  public static final String LASTNAME_PROPERTY = "last name";
  public static final String NAME_PROPERTY = "name";
  public static final String BIRTHDAY_PROPERTY = "birthday";
  public static final String PHONENUMBER_PROPERTY = "phone number";
  public static final String EMAIL_PROPERTY = "e-mail";
  private String firstName;
  private String lastName;
  private Date birthday;
  private String phoneNumber;
  private String email;
  public PersonRow() {
  }
  public Object getProperty(String property) {
    Object result = null;
    if (FIRSTNAME_PROPERTY.equals(property)) {
      result = firstName;
    }
    else if (LASTNAME_PROPERTY.equals(property)) {
      result = lastName;
    }
    else if (NAME_PROPERTY.equals(property)) {
      result = firstName + " " + lastName;
    }
    else if (BIRTHDAY_PROPERTY.equals(property)) {
      result = birthday.toString();
    }
    else if (PHONENUMBER_PROPERTY.equals(property)) {
      result = phoneNumber;
    }
    else if (EMAIL_PROPERTY.equals(property)) {
      result = email;
    }
    return result;
  }
  public Date getBirthday() {
    return birthday;
  }
  public String getEmail() {
    return email;
  }
  public String getFirstName() {
    return firstName;
  }
  public String getLastName() {
    return lastName;
  }
  public String getPhoneNumber() {
    return phoneNumber;
  }
  public void setBirthday(Date birthday) {
    this.birthday = birthday;
  }
  public void setEmail(String email) {
    this.email = email;
  }
  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }
  public void setLastName(String lastName) {
    this.lastName = lastName;
  }
  public void setPhoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
  }
}
/**
 * SimpleTable is the basic implementation of Table.
 * This table should be used with small amount of data only.
 *
 * @author pierre.mage@gmail.com
 */
class SimpleTable extends Table {
  /**
   * AbsolutePanel defining an invisible layer preventing user from selecting text from this table.
   */
  private AbsolutePanel layer;
  public SimpleTable() {
    super();
    layer = new AbsolutePanel();
    layer.setStyleName("transparent");
  }
  public void draw() {
    if (arrayColumns != null && arrayRows != null) {
      headersContainer.clear();
      rowsContainer.clear();
      tableWidth = 0;
      this.add(headersContainer, 0, 0);
      this.add(rowsContainer, 0, ROWS_HEIGHT);
      this.add(layer, 0, ROWS_HEIGHT);
      Column column;
      for (Iterator it = arrayColumns.iterator(); it.hasNext();) {
        column = (Column) it.next();
        drawColumn(column);
      }
      headersContainer.setPixelSize(tableWidth, ROWS_HEIGHT);
      rowsContainer.setPixelSize(tableWidth, arrayRows.size() * ROWS_HEIGHT);
      layer.setPixelSize(tableWidth, arrayRows.size() * ROWS_HEIGHT);
      this.setPixelSize(tableWidth, (1 + arrayRows.size()) * ROWS_HEIGHT);
    }
  }
  protected void drawColumn(Column column) {
    // The column is not drawn if not visible.
    if (column.isVisible()) {
      // Useful variables for drawing.
      HorizontalAlignmentConstant alignment = column.getAlignment();
      String property = column.getProperty();
//    int width = column.getWidth();
      int width = calculateWidth(column);
      int top = 0;
      int left = tableWidth;
      // Drawing the header.
      Label header = new Label(column.getText(), false);
      header.setHorizontalAlignment(HasHorizontalAlignment.ALIGN_CENTER);
      header.setPixelSize(width, ROWS_HEIGHT);
      header.setStyleName("header");
      headersContainer.add(header, left, 0);
      // Drawing the rows.
      Row row;
      Object data;
        for (int rowIndex = 0; rowIndex < arrayRows.size(); rowIndex++) {
          row = (Row) arrayRows.get(rowIndex);
          data = row.getProperty(property);
          Label cell = new Label("", false);
          if (data != null) {
            cell.setText(data.toString());
          }
          cell.setHorizontalAlignment(alignment);
          cell.setPixelSize(width, ROWS_HEIGHT);
          cell.setStyleName("cell");
          if (rowIndex%2 == 0) {
            cell.addStyleName("evenRow");
          } else {
            cell.addStyleName("oddRow");
          }
          rowsContainer.add(cell, left, top);
          top += ROWS_HEIGHT;
      }
      tableWidth += width;
    }
  }
}
/*
 * Copyright 2007 Sfeir, www.sfeir.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
/**
 * Table defines a table based on GWT's AbsolutePanel.
 *
 * @author pierre.mage@gmail.com and didier.girard@gmail.com
 */
abstract class Table extends AbsolutePanel {
  /**
   * int defining an average size for characters.
   */
  public static int CHARACTER_SIZE;
  /**
   * int defining the height of rows in this table (every row has the same height)
   */
  public static int ROWS_HEIGHT;
  public static void setCHARACTER_SIZE(int character_size) {
    CHARACTER_SIZE = character_size;
  }
  /**
   * ArrayList defining the columns of this table.
   */
  protected ArrayList arrayColumns;
  /**
   * ArrayList defining the content of this table.
   */
  protected ArrayList arrayRows;
  // headers and rows are separated for scrolling purpose.
  /**
   * AbsolutePanel containing the headers.
   */
  protected AbsolutePanel headersContainer;
  /**
   * AbsolutePanel containing the rows.
   */
  protected AbsolutePanel rowsContainer;
  /**
   * int defining the width of this table
   */
  protected int tableWidth;
  /**
   * Creates an empty Table.
   */
  public Table() {
    super();
    CHARACTER_SIZE = 10;
    ROWS_HEIGHT = CHARACTER_SIZE * 3;
    headersContainer = new AbsolutePanel();
    rowsContainer = new AbsolutePanel();
    arrayColumns = new ArrayList();
    setStyleName("table");
  }
  public void add(Column column) {
    arrayColumns.add(column);
  }
  /**
   * Calculates the optimal width of this table.
   */
  public int calculateWidth() {
    int width = 0;
    Column column;
    for (Iterator c = arrayColumns.iterator(); c.hasNext();) {
      column = (Column) c.next();
      if (column.isVisible()) {
        width += calculateWidth(column);
      }
    }
    return width;
  }
  /**
   * Draws the table.
   */
  public abstract void draw();
  public void setArrayRows(ArrayList arrayRows) {
    this.arrayRows = arrayRows;
  }
  public static void setROWS_HEIGHT(int rows_height) {
    ROWS_HEIGHT = rows_height;
  }
  /**
   * Calculates the optimal width of the specified column considering an average CHARACTER_SIZE;
   */
  protected int calculateWidth(Column column) {
    int width = column.getText().length();
    String property = column.getProperty();
    Row row;
    Object data;
    for (Iterator r = arrayRows.iterator(); r.hasNext();) {
      row = (Row) r.next();
      data = row.getProperty(property);
      if (data != null && data.toString().length() > width) {
        width = data.toString().length();
      }
    }
    return width * CHARACTER_SIZE;
  }
  /**
   * Draws the specified column of this table.
   */
  protected abstract void drawColumn(Column column);
}
/*
 * Copyright 2007 Sfeir, www.sfeir.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
/**
 * Column defines a column in Table.
 *
 * @author pierre.mage@gmail.com
 */
class Column {
  /**
   * String defining the alignment of this column.
   */
  private HorizontalAlignmentConstant alignment;
  /**
   * boolean defining if this column is sortable.
   */
  private boolean isSortable;
  /**
   * boolean defining if this column is visible.
   */
  private boolean isVisible;
  /**
   * String defining the property of this column.
   */
  private String property;
  /**
   * String defining the text of this column's header.
   */
  private String text;
  /**
   * int defining the width of this column.
   */
  private int width;
  /**
   * Creates an empty Column.
   */
  public Column() {
    alignment = HasHorizontalAlignment.ALIGN_CENTER;
    isSortable = false;
    isVisible = true;
    text = "column";
    width = 100;
  }
  public HorizontalAlignmentConstant getAlignment() {
    return alignment;
  }
  public String getProperty() {
    return property;
  }
  public String getText() {
    return text;
  }
  public int getWidth() {
    return width;
  }
  public boolean isSortable() {
    return isSortable;
  }
  public boolean isVisible() {
    return isVisible;
  }
  public void setAlignment(HorizontalAlignmentConstant horizontalAlignement) {
    this.alignment = horizontalAlignement;
  }
  public void setProperty(String property) {
    this.property = property;
  }
  public void setSortable(boolean isSortable) {
    this.isSortable = isSortable;
  }
  public void setText(String text) {
    this.text = text;
  }
  public void setVisible(boolean isVisible) {
    this.isVisible = isVisible;
  }
  public void setWidth(int width) {
    this.width = width;
  }
}
/*
 * Copyright 2007 Sfeir, www.sfeir.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
/**
 * Row defines a row in Table
 *
 * @author pierre.mage@gmail.com and didier.girard@gmail.com
 */
interface Row {
  /**
   * Gets Row's element associated with property.
   *
   * @param property the property whose associated object is to be retrieved
   * @return the object associated with property
   */
  public abstract Object getProperty(String property);
}
```

GWT-tableAboslute.zip( 6 k)
1.  SortableTable Widget for GWT
2.  Dynamic Table
