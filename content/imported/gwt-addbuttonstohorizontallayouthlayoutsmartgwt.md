---
title: Add buttons to HorizontalLayout (HLayout) (Smart GWT)
nav: Add buttons to HorizontalL...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20100419013505/http://www.java2s.com:80/Code/Java/GWT/AddbuttonstoHorizontalLayoutHLayoutSmartGWT.htm
---
Add buttons to HorizontalLayout (HLayout) (Smart GWT)

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
import com.google.gwt.user.client.ui.FlowPanel;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.widgets.Button;
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.ImgButton;
import com.smartgwt.client.widgets.layout.HLayout;
import com.smartgwt.client.widgets.layout.VLayout;
public class Showcase implements EntryPoint{
    public void onModuleLoad() {
       RootPanel.get().add(new ButtonAppearanceSample());
    }
}
class ButtonAppearanceSample extends FlowPanel {
  public ButtonAppearanceSample() {
      final IButton stretchButton = new IButton("Stretch Button");
      stretchButton.setWidth(150);
      stretchButton.setShowRollOver(true);
      stretchButton.setShowDisabled(true);
      stretchButton.setShowDown(true);
      stretchButton.setTitleStyle("stretchTitle");
      stretchButton.setIcon("icons/16/find.png");
      final Button cssButton = new Button("CSS Button");
      cssButton.setShowRollOver(true);
      cssButton.setShowDisabled(true);
      cssButton.setShowDown(true);
      cssButton.setIcon("icons/16/icon_add_files.png");
      final ImgButton imgButton = new ImgButton();
      imgButton.setWidth(18);
      imgButton.setHeight(18);
      imgButton.setShowRollOver(true);
      imgButton.setShowDown(true);
      imgButton.setSrc("[SKIN]/ImgButton/button.png");
      HLayout hLayout = new HLayout();
      hLayout.setMembersMargin(20);
      hLayout.addMember(stretchButton);
      hLayout.addMember(cssButton);
      hLayout.addMember(imgButton);
      VLayout layout = new VLayout();
      layout.setAutoHeight();
      layout.setMembersMargin(30);
      layout.addMember(hLayout);
      super.add(layout);
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Button with ClickListener
