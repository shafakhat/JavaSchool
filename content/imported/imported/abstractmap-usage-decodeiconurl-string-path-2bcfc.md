---
title: Java AbstractMap Usage decodeIconUrl(String path)
nav: Java AbstractMap Usage dec...
description: Decodes an URL path to extract a name and a potential qualifier.
section: Imported
order: 20009
source: http://www.java2s.com:80/example/java-utility-method/abstractmap-usage/decodeiconurl-string-path-2bcfc.html
---
Here you can find the source of decodeIconUrl(String path)

## Description

Decodes an URL path to extract a name and a potential qualifier.

## License

Apache License

## Parameter

Parameter  Description
path  an URL path

## Return

a non-null map entry (key = name, value = qualifier)

## Declaration

```java title=Example.java
publicstaticMap.Entry<String, String> decodeIconUrl(String path)
```

## Method Source Code

```java title=Example.java
//package com.java2s;/**/*fromwww.java2s.com*/
 * Copyright 2015-2017 Linagora, Universit? Joseph Fourier, Floralis
 *
 * The present code is developed in the scope of the joint LINAGORA -
 * Universit? Joseph Fourier - Floralis research program and is designated
 * as a "Result" pursuant to the terms and conditions of the LINAGORA
 * - Universit? Joseph Fourier - Floralis research program. Each copyright
 * holder of Results enumerated here above fully & independently holds complete
 * ownership of the complete Intellectual Property rights applicable to the whole
 * of said Results, and may freely exploit it in any manner which does not infringe
 * the moral rights of the other copyright holders.
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
 */import java.util.AbstractMap;
import java.util.Map;

publicclass Main {
    /**
     * Decodes an URL path to extract a name and a potential qualifier.
     * @param path an URL path
     * @return a non-null map entry (key = name, value = qualifier)
     */publicstaticMap.Entry<String, String> decodeIconUrl(String path) {if (path.startsWith("/"))
            path = path.substring(1);

        String name = null, qualifier = null;
        String[] parts = path.split("/");
        switch (parts.length) {
        case 2:
            name = parts[0];
            break;

        case 3:
            name = parts[0];
            qualifier = parts[1];
            break;

        default:
            break;
        }

        returnnewAbstractMap.SimpleEntry<>(name, qualifier);
    }
}
```

## Related

- buildClause(String key, String... values)
- countLinesColumns(String text, int initialLinesCnt, int initialColumnsCnt)
- getClassType(Object obj)
- getSymmetricPropertyValueDifference( Properties propertyFileOne, Properties propertyFileTwo)
- parseEntityURI(final String uri)
- parseExportedVariable(String exportedVariable)

[HOME](http://www.java2s.com) | Copyright © www.java2s.com 2016
