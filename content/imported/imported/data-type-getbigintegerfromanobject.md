---
title: Get BigInteger from an object
nav: Get BigInteger from an obj...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20111105121846/http://java2s.com/Tutorial/Java/0040__Data-Type/GetBigIntegerfromanobject.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Operations on <code>Object</code>.
 *
 * This class tries to handle <code>null</code> input gracefully.
 * An exception will generally not be thrown for a <code>null</code> input.
 * Each method documents its behaviour in more detail.
 *
 * @author <a href="mailto:nissim@nksystems.com">Nissim Karpenstein</a>
 * @author <a href="mailto:janekdb@yahoo.co.uk">Janek Bogucki</a>
 * @author Daniel L. Rall
 * @author Stephen Colebourne
 * @author Gary Gregory
 * @author Mario Winterer
 * @author <a href="mailto:david@davidkarlsen.com">David J. M. Karlsen</a>
 * @since 1.0
 * @version $Id: ObjectUtils.java 594336 2007-11-12 22:54:02Z bayard $
 */
public class Main {
  public static BigInteger getBigInteger(Object value) {
    BigInteger ret = null;
    if ( value != null ) {
        if ( value instanceof BigInteger ) {
            ret = (BigInteger) value;
        } else if ( value instanceof String ) {
            ret = new BigInteger( (String) value );
        } else if ( value instanceof BigDecimal ) {
            ret = ((BigDecimal) value).toBigInteger();
        } else if ( value instanceof Number ) {
            ret = BigInteger.valueOf( ((Number) value).longValue() );
        } else {
            throw new ClassCastException( "Not possible to coerce [" + value + "] from class " + value.getClass() + " into a BigInteger." );
        }
    }
    return ret;
}
}
```
