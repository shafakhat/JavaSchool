---
title: Android TextView set text
nav: Android TextView set text
description: @Override/*from ww w . j a v a2 s.c om*/ public void onCreate(Bundle savedInstanceState) {
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/android-textview-set-text.html
---
- android.widget
- android.widget TextView

## Description

```java title=Example.java
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;
public class Main extends Activity {
   private TextView textView;
   @Override public void onCreate(Bundle savedInstanceState) {
      String displayText = null;
      super.onCreate(savedInstanceState);
      setContentView(1);// R.layout.displayinformation
      Intent startingIntent = getIntent();
      if (startingIntent != null) {
         Bundle b = startingIntent.getBundleExtra("android.intent.extra.INTENT");
         if (b == null) {
            displayText = "No data.";
         } else {
            displayText = b.getString("name") + ",\n\n";
            displayText += "You are a " + b.getString("level") + "\n\n";
            displayText += "Android developer.\n";
         }
      } else {
         displayText = "Information Not Found.";
      }
      textView = (TextView) this.findViewById(0);// R.id.displaytext
      textView.setText(displayText);
   }
}
```

PreviousNext

## Related

- Android Color random RGB value
- Android ClipboardManager set text
- Android Base64 decode from base64 String
- Java AWTEvent mask window event
- Java AWT BasicStroke class
