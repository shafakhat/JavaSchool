---
title: Java array check if an array of primitive chars is empty or null.
nav: Java array check if an arr...
description: Java array check if an array of primitive chars is empty or null.
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20210102113253/http://www.java2s.com/ref/java/java-array-check-if-an-array-of-primitive-chars-is-empty-or-null.html
---
## Description

```java title=Example.java
//package com.demo2s;publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        char[] array = newchar[] { 'd', 'e', 'm', 'o', '2', 's', '.', 'c', 'o', 'm', 'a', '1', };
        System.out.println(isArrayEmpty(array));
    }//fromwww.java2s.com/**
    * <p>Checks if an array of primitive chars is empty or <code>null</code>.</p>
    *
    * @param array  the array to test
    * @return <code>true</code> if the array is empty or <code>null</code>
    * @since 2.1
    */publicstaticboolean isArrayEmpty(char[] array) {
        if (array == null || array.length == 0) {
            return true;
        }
        return false;
    }
}

/*
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
 */
```

PreviousNext

## Related

- Java Array multidimensional Arrays pass to methods
- Java Array multidimensional Arrays reference element
- Java Array search unsorted array for a value using for each loop
- Java Array append a char to char array
- Java Array append String to String array
