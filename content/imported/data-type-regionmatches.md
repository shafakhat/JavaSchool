---
title: Region Matches
nav: Region Matches
description: * Copyright (c) 1995 - 2008 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 1274
source: https://web.archive.org/web/20140829085536/http://www.java2s.com/Tutorial/Java/0040__Data-Type/RegionMatches.htm
---
```java title=Example.java
/*
 * Copyright (c) 1995 - 2008 Sun Microsystems, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 *   - Neither the name of Sun Microsystems nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
public class RegionMatchesDemo {
  public static void main(String[] args) {
    String searchMe = "Green Eggs and Ham";
    String findMe = "Eggs";
    int searchMeLength = searchMe.length();
    int findMeLength = findMe.length();
    boolean foundIt = false;
    for (int i = 0; i <= (searchMeLength - findMeLength); i++) {
      if (searchMe.regionMatches(i, findMe, 0, findMeLength)) {
        foundIt = true;
        System.out.println(searchMe.substring(i, i + findMeLength));
        break;
      }
    }
    if (!foundIt)
      System.out.println("No match found.");
  }
}
```

| 2.23.1. | Comparing Strings for Equality |
|---|---|
| 2.23.2. | To check for equality between two strings ignoring the case |
| 2.23.3. | Sequencing Strings |
| 2.23.4. | String length, charAt, equals |
| 2.23.5. | equals() and equalsIgnoreCase(). |
| 2.23.6. | equals() vs == |
| 2.23.7. | Region Matches |
| 2.23.8. | Compares all Strings in an array and returns the index at which the Strings begin to differ. |
| 2.23.9. | Compares all Strings in an array and returns the initial sequence of characters that is common to all of them. |
| 2.23.10. | Compares two Strings, and returns the index at which the Strings begin to differ. |
| 2.23.11. | Compares two Strings, and returns the portion where they differ. |
| 2.23.12. | Compress 2 adjacent (single or double) quotes into a single (s or d) quote when found in the middle of a String. |
