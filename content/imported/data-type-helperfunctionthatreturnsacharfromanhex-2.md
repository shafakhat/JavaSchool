---
title: Helper function that returns a char from an hex
nav: Helper function that retur...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Helperfunctionthatreturnsacharfromanhex.htm
---
```java title=Example.java
import java.io.File;
import java.io.FileFilter;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 *//**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */publicclass Main {
  /** Hex chars */privatestaticfinalbyte[] HEX_CHAR = newbyte[]
      { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
  /**
   *
   * @param hex The hex to dump
   * @return A char representation of the hex
   */publicstaticfinalchar dumpHex( byte hex )
  {
      return ( char ) HEX_CHAR[hex & 0x000F];
  }
}
```
