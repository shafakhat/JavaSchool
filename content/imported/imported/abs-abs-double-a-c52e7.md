---
title: Java Abs abs(double[][] A)
nav: Java Abs abs(double[][] A)
description: * This program is free software: you can redistribute it and/or modify
section: Imported
order: 20002
source: http://www.java2s.com/example/java-utility-method/abs/abs-double-a-c52e7.html
---
Here you can find the source of abs(double[][] A)

## Description

absolute value

## License

Open Source License

## Declaration

```java title=Example.java
publicstaticdouble[][] abs(double[][] A)
```

## Method Source Code

```java title=Example.java
//package com.java2s;/*/*www.java2s.com*/
 *   This program is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */publicclass Main {
    /**
     * absolute value
      */publicstaticdouble[][] abs(double[][] A) {double[][] C = newdouble[A.length][A[0].length];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
                C[i][j] = Math.abs(A[i][j]);
            }
        }
        return C;
    }
}
```

## Related

- abs(double[] array)
- abs(double[] da)
- abs(double[] in)
- abs(double[] in)
- abs(double[] v)
- abs(final byte x)
- abs(final double d)
- abs(final double value)
- abs(final double x)

[HOME](http://www.java2s.com) | Copyright © www.java2s.com 2016
