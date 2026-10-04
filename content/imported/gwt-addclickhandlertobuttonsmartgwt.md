---
title: Add click handler to button (Smart GWT)
nav: Add click handler to butto...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20100419013257/http://www.java2s.com:80/Code/Java/GWT/AddclickhandlertobuttonSmartGWT.htm
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
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.IButton;
import com.smartgwt.client.widgets.events.ClickEvent;
import com.smartgwt.client.widgets.events.ClickHandler;
import com.smartgwt.client.widgets.layout.HLayout;
import com.smartgwt.client.widgets.layout.VLayout;
public class Showcase implements EntryPoint{
    public void onModuleLoad() {
       RootPanel.get().add(getViewPanel());
    }
    public Canvas getViewPanel() {
      final IButton findButton = new IButton("Find Related");
      findButton.setWidth(120);
      findButton.setIcon("icons/16/find.png");
      final IButton saveButton = new IButton("Save");
      saveButton.setShowRollOver(true);
      saveButton.setIcon("icons/16/icon_add_files.png");
      saveButton.setIconOrientation("right");
      saveButton.setShowDownIcon(true);
      final IButton button = new IButton("Disable Save");
      button.setWidth(120);
      button.setLeft(60);
      button.setTop(45);
      button.addClickHandler(new ClickHandler() {
          public void onClick(ClickEvent event) {
              if (saveButton.isDisabled()) {
                  saveButton.enable();
                  button.setTitle("Disable Save");
              } else {
                  saveButton.disable();
                  button.setTitle("Enable Save");
              }
          }
      });
      HLayout hLayout = new HLayout();
      hLayout.setMembersMargin(20);
      hLayout.addMember(findButton);
      hLayout.addMember(saveButton);
      VLayout layout = new VLayout();
      layout.setAutoHeight();
      layout.setMembersMargin(30);
      layout.addMember(hLayout);
      layout.addMember(button);
      return layout;
  }
}
```

SmartGWT.zip( 9,880 k)
1.  Button with ClickListener
