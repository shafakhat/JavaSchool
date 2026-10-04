---
title: Turn an array of ints into a printable string.
nav: Turn an array of ints into...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2326
source: https://web.archive.org/web/20140829080152/http://www.java2s.com/Tutorial/Java/0140__Collections/Turnanarrayofintsintoaprintablestring.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Properties;
/*
   Derby - Class org.apache.derby.iapi.util.PropertyUtil
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to you under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */
public class Main {
  /**
   * Turn an array of ints into a printable string. Returns what's returned
   * in Java 5 by java.util.Arrays.toString(int[]).
   */
  public  static  String  stringify( int[] raw )
  {
      if ( raw == null ) { return "null"; }
      StringBuffer    buffer = new StringBuffer();
      int                 count = raw.length;
      buffer.append( "[ " );
      for ( int i = 0; i < count; i++ )
      {
          if ( i > 0 ) { buffer.append( ", " ); }
          buffer.append( raw[ i ] );
      }
      buffer.append( " ]" );
      return buffer.toString();
  }
}
```

| 9.6.1. | Arrays of Objects |
|---|---|
| 9.6.2. | Arrays of Strings: using 'new' operator |
| 9.6.3. | Arrays of Strings: initial values determine the size of the array |
| 9.6.4. | Demonstrate String arrays. |
| 9.6.5. | Checks whether two arrays are the same length, treating null arrays as length 0. |
| 9.6.6. | Checks whether two arrays are the same type taking into account multi-dimensional arrays. |
| 9.6.7. | Turn an array of ints into a printable string. |
| 9.6.8. | Check if the given object is an array (primitve or native). |
| 9.6.9. | Reverses the order of the given long type value array. |
| 9.6.10. | Removes the first occurrence of the specified element from the specified array. |
| 9.6.11. | Removes the element at the specified position from the specified array. |
