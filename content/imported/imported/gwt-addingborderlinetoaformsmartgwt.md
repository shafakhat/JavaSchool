---
title: Adding border line to a form (Smart GWT)
nav: Adding border line to a fo...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20100511205923/http://www.java2s.com:80/Code/Java/GWT/AddingborderlinetoaformSmartGWT.htm
---
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
import com.smartgwt.client.types.TitleOrientation;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.form.DynamicForm;
import com.smartgwt.client.widgets.form.fields.TextAreaItem;
import com.smartgwt.client.widgets.form.fields.TextItem;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  TitleOrientation titleOrientation = TitleOrientation.LEFT;
  public Canvas getViewPanel() {
      final DynamicForm form = new DynamicForm();
      form.setGroupTitle("Spanning");
      form.setIsGroup(true);
      form.setWidth(300);
      form.setHeight(180);
      form.setNumCols(2);
      form.setColWidths(60, "*");
      //form.setBorder("1px solid blue");
      form.setPadding(5);
      form.setCanDragResize(true);
      form.setResizeFrom("R");
      TextItem subjectItem = new TextItem();
      subjectItem.setTitle("Subject");
      subjectItem.setWidth("*");
      TextAreaItem messageItem = new TextAreaItem();
      messageItem.setShowTitle(false);
      messageItem.setLength(5000);
      messageItem.setColSpan(2);
      messageItem.setWidth("*");
      messageItem.setHeight("*");
      form.setFields(subjectItem, messageItem);
      return form;
  }
}
```

SmartGWT.zip( 9,880 k)
2.  Form validation for splitted form (Smart GWT)
