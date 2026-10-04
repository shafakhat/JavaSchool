---
title: Console Log System
nav: Console Log System
description: Console Log System : Java examples (example source code) » Velocity » Velocity Log
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20060513091837/http://www.java2s.com/Code/Java/Velocity/ConsoleLogSystem.htm
---
Console Log System : Java examples (example source code) » Velocity » Velocity Log

Console Log System

```java title=Example.java
import org.apache.velocity.runtime.RuntimeServices;
import org.apache.velocity.runtime.log.LogSystem;
public class ConsoleLogSystem implements LogSystem {
  private RuntimeServices rs;
  private int maxLevel = LogSystem.INFO_ID;
  private static final String[] LEVEL_NAMES = new String[] { "ERROR", "WARN",
      "INFO", "DEBUG" };
  private static final int[] LEVELS = new int[] { LogSystem.ERROR_ID,
      LogSystem.WARN_ID, LogSystem.INFO_ID, LogSystem.DEBUG_ID };
  public void init(RuntimeServices rs) throws Exception {
    System.out.println("ConsoleLogSystem.init() called");
    this.rs = rs;
    configure();
  }
  public void logVelocityMessage(int level, String message) {
    if (level >= maxLevel) {
      System.out.println("[" + getLevelName(level) + "] " + message);
    }
  }
  private void configure() {
    String maxLevelName = rs.getString("console.logsystem.max.level");
    int level = getLevelFromString(maxLevelName);
    if (level > -1) {
      System.out.println("Using log level: " + maxLevelName);
      maxLevel = level;
    }
  }
  private int getLevelFromString(String levelName) {
    for (int x = 0; x < LEVEL_NAMES.length; x++) {
      if (LEVEL_NAMES[x].equals(levelName)) {
        return LEVELS[x];
      }
    }
    // should not arrive here, couldn't find the level
    return -1;
  }
  private String getLevelName(int level) {
    for (int x = 0; x < LEVELS.length; x++) {
      if (LEVELS[x] == level) {
        return LEVEL_NAMES[x];
      }
    }
    return "UNKNOWN";
  }
}
```

Download: velocity-ConsoleLogSystem.zip (2190 K)
---
Related examples in the same category
1. This is a toy demonstration of how Velocity can use an externally configured logger
2. Custom log for Velocity
3. How to use an existing Log4j Categeory as the Velocity logging target
