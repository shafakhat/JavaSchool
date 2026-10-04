---
title: Java Abs abs(double n)
nav: Java Abs abs(double n)
description: * Licensed under the Apache License, Version 2.0 (the "License"); you may not
section: Imported
order: 20004
source: http://www.java2s.com:80/example/java-utility-method/abs/abs-double-n-b58c3.html
---
Here you can find the source of abs(double n)

## Description

abs

## License

Apache License

## Declaration

```java title=Example.java
staticpublicfinaldouble abs(double n)
```

## Method Source Code

```java title=Example.java
//package com.java2s;/**/*fromwww.java2s.com*/
 * Copyright 2008 - 2012
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 *
 * @project loon
 * @author cping
 * @email?javachenpeng@yahoo.com
 * @version 0.3.3
 */publicclass Main {
staticpublicfinaldouble abs(double n) {returnMath.abs(n);
    }

    staticpublicfinalfloat abs(float n) {
        return (n < 0) ? -n : n;
    }

    staticpublicfinalint abs(int n) {
        return (n < 0) ? -n : n;
    }
}
```

## Related

- abs(Double a)
- abs(double d)
- abs(Double d)
- abs(double d1)
- abs(double number)
- abs(double number)
- abs(double self)
- abs(double value)

[HOME](http://www.java2s.com) | Copyright © www.java2s.com 2016
