---
title: Alert MessageBox (Ext GWT)
nav: Alert MessageBox (Ext GWT)
description: final Listener<MessageBoxEvent> l = new Listener<MessageBoxEvent>() {
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20100730020522/http://www.java2s.com:80/Code/Java/GWT/AlertMessageBoxExtGWT.htm
---
Alert MessageBox (Ext GWT)

```java title=Example.java
/*
 * Ext GWT - Ext for GWT
 * Copyright(c) 2007-2009, Ext JS, LLC.
 * licensing@extjs.com
 *
 * http://extjs.com/license
 */
package com.google.gwt.sample.hello.client;
import com.extjs.gxt.ui.client.event.Listener;
import com.extjs.gxt.ui.client.event.MessageBoxEvent;
import com.extjs.gxt.ui.client.widget.Info;
import com.extjs.gxt.ui.client.widget.MessageBox;
import com.extjs.gxt.ui.client.widget.button.Button;
import com.google.gwt.core.client.EntryPoint;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    final Listener<MessageBoxEvent> l = new Listener<MessageBoxEvent>() {
      public void handleEvent(MessageBoxEvent ce) {
        Button btn = ce.getButtonClicked();
        Info.display("MessageBox", "The '{0}' button was pressed", btn.getText());
      }
    };
    MessageBox.alert("Alert", "Access Denied", l);
  }
}
```

Ext-GWT.zip( 4,297 k)
1.  Create Custom Dialog
