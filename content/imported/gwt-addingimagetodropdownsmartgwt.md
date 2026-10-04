---
title: Adding image to dropdown (Smart GWT)
nav: Adding image to dropdown (...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20100421083511/http://www.java2s.com:80/Code/Java/GWT/AddingimagetodropdownSmartGWT.htm
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
import java.util.LinkedHashMap;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.ui.RootPanel;
import com.smartgwt.client.util.SC;
import com.smartgwt.client.widgets.Canvas;
import com.smartgwt.client.widgets.form.DynamicForm;
import com.smartgwt.client.widgets.form.fields.CheckboxItem;
import com.smartgwt.client.widgets.form.fields.ColorPickerItem;
import com.smartgwt.client.widgets.form.fields.ComboBoxItem;
import com.smartgwt.client.widgets.form.fields.DateItem;
import com.smartgwt.client.widgets.form.fields.LinkItem;
import com.smartgwt.client.widgets.form.fields.RadioGroupItem;
import com.smartgwt.client.widgets.form.fields.SelectItem;
import com.smartgwt.client.widgets.form.fields.SliderItem;
import com.smartgwt.client.widgets.form.fields.SpinnerItem;
import com.smartgwt.client.widgets.form.fields.TextAreaItem;
import com.smartgwt.client.widgets.form.fields.TextItem;
import com.smartgwt.client.widgets.form.fields.TimeItem;
import com.smartgwt.client.widgets.form.fields.events.ClickHandler;
import com.smartgwt.client.widgets.form.fields.events.ClickEvent;
public class Showcase implements EntryPoint {
  public void onModuleLoad() {
    RootPanel.get().add(getViewPanel());
  }
  public Canvas getViewPanel() {
    DynamicForm form = new DynamicForm();
    SelectItem selectItem = new SelectItem();
    selectItem.setTitle("Select");
    selectItem.setHint("<nobr>A combobox with icons</nobr>");
    LinkedHashMap<String, String> valueMap = new LinkedHashMap<String, String>();
    valueMap.put("US", "<b>United States</b>");
    valueMap.put("CH", "China");
    valueMap.put("JA", "<b>Japan</b>");
    valueMap.put("IN", "India");
    valueMap.put("GM", "Germany");
    valueMap.put("FR", "France");
    valueMap.put("IT", "Italy");
    valueMap.put("RS", "Russia");
    valueMap.put("BR", "<b>Brazil</b>");
    valueMap.put("CA", "Canada");
    valueMap.put("MX", "Mexico");
    valueMap.put("SP", "Spain");
    selectItem.setValueMap(valueMap);
    selectItem.setImageURLPrefix("flags/16/");
    selectItem.setImageURLSuffix(".png");
    LinkedHashMap<String, String> valueIcons = new LinkedHashMap<String, String>();
    valueIcons.put("US", "US");
    valueIcons.put("CH", "CH");
    valueIcons.put("JA", "JA");
    valueIcons.put("IN", "IN");
    valueIcons.put("GM", "GM");
    valueIcons.put("FR", "FR");
    valueIcons.put("IT", "IT");
    valueIcons.put("RS", "RS");
    valueIcons.put("BR", "BR");
    valueIcons.put("CA", "CA");
    valueIcons.put("MX", "MX");
    valueIcons.put("SP", "SP");
    selectItem.setValueIcons(valueIcons);
    form.setFields(selectItem);
    return form;
  }
}
```

SmartGWT.zip( 9,880 k)
