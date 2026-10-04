---
title: An empty icon with arbitrary width and height.
nav: An empty icon with arbitra...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20100204224520/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Anemptyiconwitharbitrarywidthandheight.htm
---
An empty icon with arbitrary width and height.

```java title=Example.java
/**
 * @PROJECT.FULLNAME@ @VERSION@ License.
 *
 * Copyright @YEAR@ L2FProd.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.awt.Component;
import java.awt.Graphics;
import javax.swing.Icon;
/**
 * An empty icon with arbitrary width and height.
 */
public final class EmptyIcon implements Icon {
  private int width;
  private int height;
  public EmptyIcon() {
    this(0, 0);
  }
  public EmptyIcon(int width, int height) {
    this.width = width;
    this.height = height;
  }
  public int getIconHeight() {
    return height;
  }
  public int getIconWidth() {
    return width;
  }
  public void paintIcon(Component c, Graphics g, int x, int y) {
  }
}
```

1.  Create a dynamic icon
---  ---
2.  A simple application to test the functionality of the OvalIcon class
3.  Icon Displayer
4.  Implement the Icon interface
5.  Calendar Page icons with Weekday, Day and Month
6.  MemImage is an in-memory icon showing a Color gradient
7.  Example of an icon that changes form
8.  Custom Icon Demo
9.  Create Image Icon from PNG file
10.  Reading an Image or Icon from a File
11.  Draw an Icon object
12.  Plain Color Icon
13.  Color Icon
14.  Arrow Icon
15.  Icon Line
16.  Return a filled oval as an Icon
17.  Layered Icon
18.  An icon for painting a square swatch of a specified Color.
19.  Transparent icon with no content
20.  Creates a transparent icon.
21.  Icon Codec
