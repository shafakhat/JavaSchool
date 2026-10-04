---
title: Java Abs abs(final double d)
nav: Java Abs abs(final double d)
description: * Copyright (C) 2013 by Idylwood Technologies, LLC. All rights reserved.
section: Imported
order: 20007
source: http://www.java2s.com/example/java-utility-method/abs/abs-final-double-d-80c6d.html
---
Here you can find the source of abs(final double d)

## Description

Returns the absolute value of d (without branching).

## License

Open Source License

## Parameter

Parameter  Description
d  a parameter

## Declaration

```java title=Example.java
publicstaticfinaldouble abs(finaldouble d)
```

## Method Source Code

```java title=Example.java
//package com.java2s;/*/*fromwww.java2s.com*/
 * ====================================================
 * Copyright (C) 2013 by Idylwood Technologies, LLC. All rights reserved.
 *
 * Developed at Idylwood Technologies, LLC.
 * Permission to use, copy, modify, and distribute this
 * software is freely granted, provided that this notice
 * is preserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * The License should have been distributed to you with the source tree.
 * If not, it can be found at
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Author: Charles Cooper
 * Date: 2013
 * ====================================================
 */publicclass Main {
    /**
     * Returns the absolute value of d (without branching).
     * Faster than OpenJDK implementation.
     * @param d
     * @return
     */publicstaticfinaldouble abs(finaldouble d) {returnDouble.longBitsToDouble(Long.MAX_VALUE & Double.doubleToRawLongBits(d));
    }

    /**
     * Returns the absolute value of f (without branching).
     * Faster than OpenJDK implementation.
     * @param f
     * @return
     */publicstaticfinalfloat abs(finalfloat f) {
        returnFloat.intBitsToFloat(Integer.MAX_VALUE & Float.floatToRawIntBits(f));
    }

    /**
     * Returns the absolute value of l (without branching).
     * Faster than OpenJDK implementation.
     * @param l
     * @return
     */publicstaticfinallong abs(finallong l) {
        finallong sign = l >>> 63;
        return (l ^ (~sign + 1)) + sign;
    }

    /**
     * Returns the absolute value of i (without branching).
     * Faster than OpenJDK implementation.
     * @param d
     * @return
     */publicstaticfinalint abs(finalint i) {
        finalint sign = i >>> 31;
        return (i ^ (~sign + 1)) + sign;
    }
}
```

## Related

- abs(double[] in)
- abs(double[] in)
- abs(double[] v)
- abs(double[][] A)
- abs(final byte x)
- abs(final double value)
- abs(final double x)
- abs(final int pNumber)
- abs(float f)

[HOME](http://www.java2s.com) | Copyright © www.java2s.com 2016
