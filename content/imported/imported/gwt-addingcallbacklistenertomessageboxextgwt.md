---
title: Adding callback listener to MessageBox (Ext GWT)
nav: Adding callback listener t...
description: final MessageBox box = MessageBox.prompt("Name", "Please enter your name:");
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20100523193814/http://www.java2s.com:80/Code/Java/GWT/AddingcallbacklistenertoMessageBoxExtGWT.htm
---
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
import com.extjs.gxt.ui.client.util.Params;
import com.extjs.gxt.ui.client.widget.Info;
import com.extjs.gxt.ui.client.widget.MessageBox;
import com.google.gwt.core.client.EntryPoint;
public class Hello implements EntryPoint {
  public void onModuleLoad() {
    final MessageBox box = MessageBox.prompt("Name", "Please enter your name:");
    box.addCallback(new Listener<MessageBoxEvent>() {
      public void handleEvent(MessageBoxEvent be) {
        Info.display("MessageBox", "You entered '{0}'", new Params(be.getValue()));
      }
    });
  }
}
```

Ext-GWT.zip( 4,297 k)
1.  Create Custom Dialog
