---
title: Add item to ListBox
nav: Add item to ListBox
description: Imported from the java2s.com archive: Add item to ListBox
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20081208042345/http://www.java2s.com:80/Code/Java/GWT/AdditemtoListBox.htm
---
```java title=Example.java
package com.java2s.gwt.client;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.Widget;
import com.google.gwt.user.client.ui.ListBox;
public class GWTClient implements EntryPoint {
  public void onModuleLoad() {
    ListBox list = new ListBox();
    list.setVisibleItemCount(1);
    for (int i = 0; i < 10; ++i) {
      list.addItem("list item " + i);
    }
    RootPanel.get().add(list);
  }
}
```

GWT-addItemToListBox.zip( 2 k)
1.  ListBox with multiple selection
