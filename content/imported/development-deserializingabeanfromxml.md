---
title: Deserializing a Bean from XML
nav: Deserializing a Bean from ...
description: Imported from the java2s.com archive: Deserializing a Bean from XML
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20100624051704/http://www.java2s.com:80/Tutorial/Java/0120__Development/DeserializingaBeanfromXML.htm
---
```java title=Example.java
import java.beans.XMLDecoder;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
public class Main {
  public static void main(String[] argv) throws Exception {
    XMLDecoder decoder = new XMLDecoder(new BufferedInputStream(
        new FileInputStream("infilename.xml")));
    MyClass o = (MyClass) decoder.readObject();
    decoder.close();
    int prop = o.getProp(); // 1
    int[] props = o.getProps(); // [1, 2, 3]
  }
}
class MyClass {
  // The prop property
  int i;
  public int getProp() {
    return i;
  }
  public void setProp(int i) {
    this.i = i;
  }
  // The props property
  int[] iarray = new int[0];
  public int[] getProps() {
    return iarray;
  }
  public void setProps(int[] iarray) {
    this.iarray = iarray;
  }
}
/*
    <?xml version="1.0" encoding="UTF-8"?>
    <java version="1.4.0" class="java.beans.XMLDecoder">
        <object class="MyClass">
            <void property="prop">
                <int>1</int>
            </void>
            <void property="props">
                <array class="int" length="3">
                    <void index="0">
                        <int>1</int>
                    </void>
                    <void index="1">
                        <int>2</int>
                    </void>
                    <void index="2">
                        <int>3</int>
                    </void>
                </array>
            </void>
        </object>
    </java>
*/
```
