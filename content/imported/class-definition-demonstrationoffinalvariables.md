---
title: Demonstration of final variables
nav: Demonstration of final var...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1142
source: https://web.archive.org/web/20140829085849/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstrationoffinalvariables.htm
---
```java title=Example.java
/*
 *     file: FinalVariables.java
 *  package: oreilly.hcj.finalstory
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import javax.swing.JDialog;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class FinalVariables {
  /**
   * Test code.
   *
   * @param args Command line arguments.
   */
  public static final void main(final String[] args) {
    System.out.println("Note how the key variable is changed.");
    someMethod("JAVA_HOME");
    someMethod("ANT_HOME");
  }
  /**
   * Get an environment property.
   *
   * @param environmentKey The key to an environment property.
   *
   * @return The value of the property.
   */
  public static String someBuggedMethod(final String environmentKey) {
    final String key = "env." + environmentKey;
    System.out.println("Key is: " + key);
    // key = new String("someValue"); // <= compiler error.
    return (System.getProperty(key));
  }
  /**
   * Get an environment property.
   *
   * @param environmentKey The key to an environment property.
   *
   * @return The value of the property.
   */
  public static String someMethod(final String environmentKey) {
    final String key = "env." + environmentKey;
    System.out.println("Key is: " + key);
    return (System.getProperty(key));
  }
  /**
   * build the panel that comprises the dialog.
   *
   * @param name The name of the instance.
   */
  public void buildGUIDialog(final String name) {
    final String instanceName;
    if (name == null) {
      // no problem here.
      instanceName = getClass()
                       .getName() + hashCode();
    } else {
      // no problem here as well.
      instanceName = getClass()
                       .getName() + name;
    }
    JDialog dialog = new JDialog();
    // .. Do a bunch of layout and component building.
    dialog.setTitle(instanceName);
    // .. Do dialog assembly
    // instanceName = "hello";  // <= compiler error
  }
}
/* ########## End of File ########## */
```

| 5.27.1. | final Variables |
|---|---|
| 5.27.2. | 'Blank' final fields |
| 5.27.3. | Java Final variable: Once created and initialized, its value can not be changed |
| 5.27.4. | Using 'final' with method arguments |
| 5.27.5. | The effect of final on fields |
| 5.27.6. | You can override a private or private final method |
| 5.27.7. | Making an entire class final |
| 5.27.8. | Demonstrates how final variables are replaced at compilation time |
| 5.27.9. | Demonstration of final class members |
| 5.27.10. | Base class for demonstation of final methods |
| 5.27.11. | Demonstration of final constants |
| 5.27.12. | Demonstration of final variables |
