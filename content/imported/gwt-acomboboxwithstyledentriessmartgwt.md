---
title: A combobox with styled entries (Smart GWT)
nav: A combobox with styled ent...
description: * SmartGWT is free software; you can redistribute it and/or modify it
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20100421083506/http://www.java2s.com:80/Code/Java/GWT/AcomboboxwithstyledentriesSmartGWT.htm
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
    SelectItem selectItem2 = new SelectItem();
    selectItem2.setTitle("Select");
    selectItem2.setHint("<nobr>A combobox with styled entries</nobr>");
    selectItem2.setValueMap("<span style='color:#FF0000;'>Red</span>",
        "<span style='color:#00FF00;'>Green</span>", "<span style='color:#0000FF;'>Blue</span>");
    form.setFields(selectItem2);
    return form;
  }
}
```

SmartGWT.zip( 9,880 k)
