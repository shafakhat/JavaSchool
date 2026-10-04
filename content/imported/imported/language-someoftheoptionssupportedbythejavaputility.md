---
title: Some of the Options Supported by the javap Utility
nav: Some of the Options Suppor...
description: Imported from the java2s.com archive: Some of the Options Supported by the javap Utility
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/SomeoftheOptionsSupportedbythejavapUtility.htm
---
```java title=Example.java
Option          Description

-b              This command ensures backward compatibility with earlier versions of javap.

-bootclasspath  This command, followed by a path, specifies the path from which to load the bootstrap classes. Normally these would be classes contained in the /lib/rt.jar archive.

-c              This command prints the JVM instructions for the execution of each method. This tells you what the bytecode for each method actually does.

-classpath      This command, followed by a user-specified class path, overrides the system CLASSPATH environment variable.

-extdirs        This command, followed by a directory, overrides the location the system searches for installed extensions. The default location is /lib/ext.

-help           This command prints information about the javap utility.

-Jflag          This command passes the specified flag directly to the runtime system.

-l              This command displays line and local variables.

-package        This command shows only package, protected, and public classes and members. This is the default.

-private        This command shows information about all classes and members.

-protected      This command displays information about protected and public classes and members only.

-public         This command shows information only about public classes and members.

-s              This command prints internal type signatures.

-verbose        This command prints additional information for each method including stack size, local variable information, and arguments.
```
