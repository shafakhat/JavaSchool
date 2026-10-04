---
title: Decode byte array
nav: Decode byte array
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20100706224208/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Decodebytearray.htm
---
```java title=Example.java
/*   Copyright 2004 The Apache Software Foundation
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *  limitations under the License.
 */
//xmlbeans
import java.io.UnsupportedEncodingException;
/**
 * format validation
 *
 * This class encodes/decodes hexadecimal data
 * @author Jeffrey Rodriguez
 * @version $Id: HexBin.java 125124 2005-01-14 00:23:54Z kkrouse $
 */
public class Main {
  static private final int  BASELENGTH   = 255;
  static private final int  LOOKUPLENGTH = 16;
  static private byte [] hexNumberTable    = new byte[BASELENGTH];
  static private byte [] lookUpHexAlphabet = new byte[LOOKUPLENGTH];
  static {
      for (int i = 0; i<BASELENGTH; i++ ) {
          hexNumberTable[i] = -1;
      }
      for ( int i = '9'; i >= '0'; i--) {
          hexNumberTable[i] = (byte) (i-'0');
      }
      for ( int i = 'F'; i>= 'A'; i--) {
          hexNumberTable[i] = (byte) ( i-'A' + 10 );
      }
      for ( int i = 'f'; i>= 'a'; i--) {
         hexNumberTable[i] = (byte) ( i-'a' + 10 );
      }
      for(int i = 0; i<10; i++ )
          lookUpHexAlphabet[i] = (byte) ('0'+i );
      for(int i = 10; i<=15; i++ )
          lookUpHexAlphabet[i] = (byte) ('A'+i -10);
  }
  static public byte[] decode(byte[] binaryData) {
      if (binaryData == null)
          return null;
      int lengthData   = binaryData.length;
      if (lengthData % 2 != 0)
          return null;
      int lengthDecode = lengthData / 2;
      byte[] decodedData = new byte[lengthDecode];
      for( int i = 0; i<lengthDecode; i++ ){
          if (!isHex(binaryData[i*2]) || !isHex(binaryData[i*2+1])) {
              return null;
          }
          decodedData[i] = (byte)((hexNumberTable[binaryData[i*2]] << 4) | hexNumberTable[binaryData[i*2+1]]);
      }
      return decodedData;
  }
  /**
   * byte to be tested if it is Base64 alphabet
   *
   * @param octect
   * @return
   */
  static boolean isHex(byte octect) {
      return (hexNumberTable[octect] != -1);
  }
}
```
