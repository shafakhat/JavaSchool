---
title: Get Package Names From Dir
nav: Get Package Names From Dir
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 2137
source: https://web.archive.org/web/20140829080042/http://www.java2s.com/Tutorial/Java/0125__Reflection/GetPackageNamesFromDir.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import java.io.File;
import java.util.List;
public final class ReflectionUtil {
  private static void getPackageNamesFromDir(File base, File dir, List<String> pkgs) {
    boolean foundClass = false;
    for (File file : dir.listFiles()) {
      if (file.isDirectory()) {
        getPackageNamesFromDir(base, file, pkgs);
      } else if (!foundClass && file.getName().endsWith(".class")) {
        foundClass = true;
        String pkg = "";
        file = dir;
        while (!file.equals(base)) {
          if (!"".equals(pkg)) {
            pkg = "." + pkg;
          }
          pkg = file.getName() + pkg;
          file = file.getParentFile();
        }
        if (!pkgs.contains(pkg)) {
          pkgs.add(pkg);
        }
      }
    }
  }
  private static String getPackageName(String clzName) {
    if (clzName.indexOf("/") == -1) {
      return null;
    }
    String packageName = clzName.substring(0, clzName.lastIndexOf("/"));
    return packageName.replace("/", ".");
  }
}
```

| 7.6.1. | Demonstrate Package |
|---|---|
| 7.6.2. | Get full package name |
| 7.6.3. | Get package name of a class |
| 7.6.4. | getPackage() returns null for a class in the unnamed package |
| 7.6.5. | getPackage() returns null for a primitive type or array |
| 7.6.6. | Find the Package of an Object |
| 7.6.7. | Get the class name with or without the package |
| 7.6.8. | Detect if a package is available |
| 7.6.9. | Get the package name of the specified class. |
| 7.6.10. | Get the short name of the specified class by striping off the package name. |
| 7.6.11. | Get Package Names From Dir |
| 7.6.12. | Get non Package Qualified Name |
| 7.6.13. | Returns the package portion of the specified class |
