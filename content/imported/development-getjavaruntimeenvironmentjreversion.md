---
title: Get Java Runtime Environment (JRE) version
nav: Get Java Runtime Environme...
description: Imported from the java2s.com archive: Get Java Runtime Environment (JRE) version
section: Imported - java2s Archive
order: 1188
source: https://web.archive.org/web/20140829091137/http://www.java2s.com/Tutorial/Java/0120__Development/GetJavaRuntimeEnvironmentJREversion.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String version = System.getProperty("java.version");
    System.out.println("JRE Version = " + version);
  }
}
```

| 6.2.1. | Java system properties |
|---|---|
| 6.2.2. | Using System.getProperty(String key) to retrieve system properties |
| 6.2.3. | Accessing a single System Properties: user.dir |
| 6.2.4. | Getting the Default System Properties |
| 6.2.5. | Setting System Properties |
| 6.2.6. | Create a user-defined property or change the value of the current property |
| 6.2.7. | Determine operating system using System class |
| 6.2.8. | Get Java specification version using System class |
| 6.2.9. | Get system properties using System class |
| 6.2.10. | Loading Native Code |
| 6.2.11. | Set a system property |
| 6.2.12. | Setting the Value of a System Property from the Command Line: add -D option to the java command when running your program. |
| 6.2.13. | Get Java Runtime Environment (JRE) version |
| 6.2.14. | Get user home directory name |
| 6.2.15. | Get operating system name and version |
| 6.2.16. | Get file separator symbol |
| 6.2.17. | Get path / classpath separator |
| 6.2.18. | Get Java Home directory |
| 6.2.19. | Get username of system current user |
| 6.2.20. | Clear system property: The System.clearProperty() method available in Java 1.5 |
| 6.2.21. | Get operating system temporary directory / folder |
| 6.2.22. | Get Environment Variables |
| 6.2.23. | Terminate a Java application |
| 6.2.24. | System.setProperty("apple.laf.useScreenMenuBar", "true") |
| 6.2.25. | Emit a beep by printing the ASCII Bell character to the console |
| 6.2.26. | Returns a default value if the specified property does not exist |
