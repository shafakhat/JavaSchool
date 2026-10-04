---
title: Adding Selection listener to ListGrid (Smart GWT)
nav: Adding Selection listener ...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20100529232609/http://www.java2s.com:80/Code/Java/GWT/AddingSelectionlistenertoListGridSmartGWT.htm
---
Adding Selection listener to ListGrid (Smart GWT)

```java title=Example.java
/*
 * SmartGWT (GWT for SmartClient)
 * Copyright 2008 and beyond, Isomorphic Software, Inc.
 *
 * SmartGWT is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License version 3
 * as published by the Free Software Foundation.  SmartGWT is also
 * available under typical commercial license terms - see
 * http://smartclient.com/license
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 */
package com.smartgwt.sample.showcase.client;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.types.ListGridFieldType;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.ImgProperties;
import com.smartgwt.client.widgets.grid.ListGrid;
import com.smartgwt.client.widgets.grid.ListGridField;
import com.smartgwt.client.widgets.grid.ListGridRecord;
import com.smartgwt.client.widgets.grid.events.SelectionChangedHandler;
import com.smartgwt.client.widgets.grid.events.SelectionEvent;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    Canvas canvas = new Canvas();
    final PartsListGrid mirrorSelectionList = new PartsListGrid();
    mirrorSelectionList.setHeight(160);
    mirrorSelectionList.setEmptyMessage("<br><br>Nothing selected");
    mirrorSelectionList.setLeft(200);
    final PartsListGrid myList1 = new PartsListGrid();
    myList1.setHeight(160);
    myList1.setCanDragSelect(true);
    myList1.setData(getRecords());
    myList1.addSelectionChangedHandler(new SelectionChangedHandler() {
        public void onSelectionChanged(SelectionEvent event) {
            mirrorSelectionList.setData(myList1.getSelection());
        }
    });
    canvas.addChild(myList1);
    canvas.addChild(mirrorSelectionList);
    return canvas;
  }
  public PartRecord[] getRecords() {
    return new PartRecord[]{
            new PartRecord("Blue", "cube_blue.png", 1),
            new PartRecord("Yellow", "cube_yellow.png", 2),
            new PartRecord("Green", "cube_green.png", 3),
            new PartRecord("Blue", "cube_blue.png", 4),
            new PartRecord("Yellow", "cube_yellow.png", 5),
            new PartRecord("Green", "cube_green.png", 6),
            new PartRecord("Blue", "cube_blue.png", 7),
            new PartRecord("Yellow", "cube_yellow.png", 8),
            new PartRecord("Green", "cube_green.png", 9),
    };
}
}
class PartRecord extends ListGridRecord {
  public PartRecord() {
  }
  public PartRecord(String partName, String partSrc, int partNum) {
      setPartName(partName);
      setPartSrc(partSrc);
      setPartNum(partNum);
  }
  public void setPartName(String partName) {
      setAttribute("partName", partName);
  }
  public void setPartSrc(String partSrc) {
      setAttribute("partSrc", partSrc);
  }
  public void setPartNum(int partNum) {
      setAttribute("partNum", partNum);
  }
}
class PartsListGrid extends ListGrid {
  PartsListGrid() {
      setWidth(150);
      setCellHeight(24);
      setImageSize(16);
      setShowEdges(true);
      setBorder("0px");
      setBodyStyleName("normal");
      setAlternateRecordStyles(true);
      setShowHeader(false);
      setLeaveScrollbarGap(false);
      setEmptyMessage("<br><br>Drag &amp; drop parts here");
      ListGridField partSrcField = new ListGridField("partSrc", 24);
      partSrcField.setType(ListGridFieldType.IMAGE);
      partSrcField.setImgDir("pieces/16/");
      ListGridField partNameField = new ListGridField("partName");
      ListGridField partNumField = new ListGridField("partNum", 20);
      setFields(partSrcField, partNameField, partNumField);
      setTrackerImage(new ImgProperties("pieces/24/cubes_all.png", 24, 24));
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Absolute Table
2.  SortableTable Widget for GWT
3.  Dynamic Table
