---
title: Converts a hex string to a byte array.
nav: Converts a hex string to a...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertsahexstringtoabytearray.htm
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
 *///xmlbeans
import java.io.UnsupportedEncodingException;
/**
 * format validation
 *
 * This class encodes/decodes hexadecimal data
 * @author Jeffrey Rodriguez
 * @version $Id: HexBin.java 125124 2005-01-14 00:23:54Z kkrouse $
 */publicclass Main {
  staticprivatefinalint  BASELENGTH   = 255;
  staticprivatefinalint  LOOKUPLENGTH = 16;
  staticprivatebyte [] hexNumberTable    = newbyte[BASELENGTH];
  staticprivatebyte [] lookUpHexAlphabet = newbyte[LOOKUPLENGTH];

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

  /**
   * Converts a hex string to a byte array.
   */staticpublicbyte[] stringToBytes(String hexEncoded)
  {
      return decode(hexEncoded.getBytes());
  }
  staticpublicbyte[] decode(byte[] binaryData) {
      if (binaryData == null)
          return null;
      int lengthData   = binaryData.length;
      if (lengthData % 2 != 0)
          return null;

      int lengthDecode = lengthData / 2;
      byte[] decodedData = newbyte[lengthDecode];
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
   */staticboolean isHex(byte octect) {
      return (hexNumberTable[octect] != -1);
  }
}
```
