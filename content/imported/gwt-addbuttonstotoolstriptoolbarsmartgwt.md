---
title: Add buttons to ToolStrip(ToolBar) (Smart GWT)
nav: Add buttons to ToolStrip(T...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100914170651/http://www.java2s.com:80/Code/Java/GWT/AddbuttonstoToolStripToolBarSmartGWT.htm
---
Add buttons to ToolStrip(ToolBar) (Smart GWT)

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
import com.smartgwt.client.types.SelectionType;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.ImgButton;
import com.smartgwt.client.widgets.layout.VLayout;
import com.smartgwt.client.widgets.toolbar.ToolStrip;
public class Showcase implements EntryPoint{
    public void onModuleLoad() {
       RootPanel.get().add(getViewPanel());
    }
    public Canvas getViewPanel() {
      ToolStrip toolStrip = new ToolStrip();
      toolStrip.setWidth(200);
      toolStrip.setHeight(24);
      ImgButton boldButton = new ImgButton();
      boldButton.setSize(24);
      boldButton.setShowRollOver(false);
      boldButton.setSrc("icons/24/text_bold.png");
      boldButton.setActionType(SelectionType.CHECKBOX);
      toolStrip.addMember(boldButton);
      ImgButton italicsButton = new ImgButton();
      italicsButton.setSize(24);
      italicsButton.setShowRollOver(false);
      italicsButton.setSrc("icons/24/text_italics.png");
      italicsButton.setActionType(SelectionType.CHECKBOX);
      toolStrip.addMember(italicsButton);
      ImgButton underlineButton = new ImgButton();
      underlineButton.setSize(24);
      underlineButton.setShowRollOver(false);
      underlineButton.setSrc("icons/24/text_underlined.png");
      underlineButton.setActionType(SelectionType.CHECKBOX);
      toolStrip.addMember(underlineButton);
      ImgButton alignLeftButton = new ImgButton();
      alignLeftButton.setSize(24);
      alignLeftButton.setShowRollOver(false);
      alignLeftButton.setSrc("icons/24/text_align_left.png");
      alignLeftButton.setActionType(SelectionType.RADIO);
      alignLeftButton.setRadioGroup("textAlign");
      toolStrip.addMember(alignLeftButton);
      ImgButton alignRightButton = new ImgButton();
      alignRightButton.setSize(24);
      alignRightButton.setShowRollOver(false);
      alignRightButton.setSrc("icons/24/text_align_right.png");
      alignRightButton.setActionType(SelectionType.RADIO);
      alignRightButton.setRadioGroup("textAlign");
      toolStrip.addMember(alignRightButton);
      ImgButton alignCenterButton = new ImgButton();
      alignCenterButton.setSize(24);
      alignCenterButton.setShowRollOver(false);
      alignCenterButton.setSrc("icons/24/text_align_center.png");
      alignCenterButton.setActionType(SelectionType.RADIO);
      alignCenterButton.setRadioGroup("textAlign");
      toolStrip.addMember(alignCenterButton);
      VLayout layout = new VLayout();
      layout.setAutoHeight();
      layout.addMember(toolStrip);
      return layout;
  }
}
```

1.  Tooltip component for GWT
