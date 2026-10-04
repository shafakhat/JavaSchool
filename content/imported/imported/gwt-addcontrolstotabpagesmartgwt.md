---
title: Add controls to Tab page (Smart GWT)
nav: Add controls to Tab page (...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20100807023003/http://www.java2s.com:80/Code/Java/GWT/AddcontrolstoTabpageSmartGWT.htm
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
import com.smartgwt.client.types.Side;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.form.DynamicForm;
import com.smartgwt.client.widgets.form.fields.CheckboxItem;
import com.smartgwt.client.widgets.form.fields.TextItem;
import com.smartgwt.client.widgets.form.fields.events.ChangedEvent;
import com.smartgwt.client.widgets.form.fields.events.ChangedHandler;
import com.smartgwt.client.widgets.layout.VLayout;
import com.smartgwt.client.widgets.tab.Tab;
import com.smartgwt.client.widgets.tab.TabSet;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    final TabSet topTabSet = new TabSet();
    topTabSet.setTabBarPosition(Side.TOP);
    topTabSet.setTabBarAlign(Side.LEFT);
    topTabSet.setWidth(400);
    topTabSet.setHeight(200);
    final Tab preferencesTab = new Tab("Preferences");
    DynamicForm preferencesForm = new DynamicForm();
    CheckboxItem useTabsCheckbox = new CheckboxItem();
    useTabsCheckbox.setTitle("Use SmartGWT tabs");
    preferencesForm.setFields(useTabsCheckbox);
    preferencesTab.setPane(preferencesForm);
    Tab profileTab = new Tab("Profile");
    DynamicForm profileForm = new DynamicForm();
    TextItem nameTextItem = new TextItem();
    nameTextItem.setTitle("Your Name");
    nameTextItem.addChangedHandler(new ChangedHandler() {
        public void onChanged(ChangedEvent event) {
            String newTitle = (event.getValue() == null ? "" : event.getValue() + "'s ") + "Preferences";
            topTabSet.setTabTitle(preferencesTab, newTitle);
        }
    });
    profileForm.setFields(nameTextItem);
    profileTab.setPane(profileForm);
    topTabSet.addTab(profileTab);
    topTabSet.addTab(preferencesTab);
    VLayout vLayout = new VLayout();
    vLayout.setMembersMargin(15);
    vLayout.addMember(topTabSet);
    vLayout.setHeight("auto");
    return vLayout;
  }
}
```

SmartGWT.zip( 9,880 k)
