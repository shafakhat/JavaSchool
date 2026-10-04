---
title: Use anonymous inner classes
nav: Use anonymous inner classes
description: Imported from the java2s.com archive: Use anonymous inner classes
section: Imported - java2s Archive
order: 1099
source: https://web.archive.org/web/20140829083546/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Useanonymousinnerclasses.htm
---
```java title=Example.java
import java.io.File;
import java.io.FilenameFilter;
import java.util.Arrays;
import java.util.regex.Pattern;
public class MainClass {
  public static FilenameFilter filter(final String regex) {
    // Creation of anonymous inner class:
    return new FilenameFilter() {
      private Pattern pattern = Pattern.compile(regex);
      public boolean accept(File dir, String name) {
        return pattern.matcher(new File(name).getName()).matches();
      }
    }; // End of anonymous inner class
  }
  public static void main(String[] args) {
    File path = new File(".");
    String[] list;
    if (args.length == 0)
      list = path.list();
    else
      list = path.list(filter(args[0]));
    Arrays.sort(list);
    for (int i = 0; i < list.length; i++)
      System.out.println(list[i]);
  }
}
```

| 5.15.1. | Demonstrate an inner class. |
|---|---|
| 5.15.2. | Define an inner class within a for loop. |
| 5.15.3. | Use anonymous inner classes |
| 5.15.4. | Building the anonymous inner class in-place |
| 5.15.5. | Anonymous inner class cannot have a named constructor, only an instance initializer |
| 5.15.6. | Creating a constructor for an anonymous inner class |
| 5.15.7. | Using 'instance initialization' to perform construction on an anonymous inner class |
| 5.15.8. | Argument must be final to use inside anonymous inner class |
| 5.15.9. | A method that returns an anonymous inner class |
| 5.15.10. | An anonymous inner class that calls the base-class constructor |
| 5.15.11. | An anonymous inner class that performs initialization |
| 5.15.12. | Demonstrates method-scoped inner classes |
| 5.15.13. | Demonstrates anonymous classes |
| 5.15.14. | Demonstration of some static nested classes |
| 5.15.15. | Access inner class from outside |
| 5.15.16. | Accessing its enclosing instance from an inner class |
