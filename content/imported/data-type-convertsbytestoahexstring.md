---
title: Converts bytes to a hex string
nav: Converts bytes to a hex st...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertsbytestoahexstring.htm
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
   */staticpublic String bytesToString(byte[] binaryData)
  {
      if (binaryData == null)
          return null;
      returnnew String(encode(binaryData));
  }
  /**
   * array of byte to encode
   *
   * @param binaryData
   * @return return encode binary array
   */staticpublicbyte[] encode(byte[] binaryData) {
      if (binaryData == null)
          return null;
      int lengthData   = binaryData.length;
      int lengthEncode = lengthData * 2;
      byte[] encodedData = newbyte[lengthEncode];
      for( int i = 0; i<lengthData; i++ ){
          encodedData[i*2] = lookUpHexAlphabet[(binaryData[i] >> 4) & 0xf];
          encodedData[i*2+1] = lookUpHexAlphabet[ binaryData[i] & 0xf];
      }
      return encodedData;
  }
}
```
