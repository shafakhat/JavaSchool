---
title: Runs a jar application from any url
nav: Runs a jar application fro...
description: return attr != null ? attr.getValue(Attributes.Name.MAIN_CLASS) : null;
section: Imported - java2s Archive
order: 2139
source: https://web.archive.org/web/20140829075843/http://www.java2s.com/Tutorial/Java/0125__Reflection/Runsajarapplicationfromanyurl.htm
---
```java title=Example.java
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.net.JarURLConnection;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.jar.Attributes;
class JarClassLoader extends URLClassLoader {
  private URL url;
  public JarClassLoader(URL url) {
    super(new URL[] { url });
    this.url = url;
  }
  public String getMainClassName() throws IOException {
    URL u = new URL("jar", "", url + "!/");
    JarURLConnection uc = (JarURLConnection) u.openConnection();
    Attributes attr = uc.getMainAttributes();
    return attr != null ? attr.getValue(Attributes.Name.MAIN_CLASS) : null;
  }
  public void invokeClass(String name, String[] args) throws ClassNotFoundException,
      NoSuchMethodException, InvocationTargetException {
    Class c = loadClass(name);
    Method m = c.getMethod("main", new Class[] { args.getClass() });
    m.setAccessible(true);
    int mods = m.getModifiers();
    if (m.getReturnType() != void.class || !Modifier.isStatic(mods) || !Modifier.isPublic(mods)) {
      throw new NoSuchMethodException("main");
    }
    try {
      m.invoke(null, new Object[] { args });
    } catch (IllegalAccessException e) {
    }
  }
}
public class JarRunner {
    public static void main(String[] args) throws Exception {
        URL url = new URL(args[0]);
        JarClassLoader cl = new JarClassLoader(url);
        String name = null;
            name = cl.getMainClassName();
        if (name == null) {
            fatal("Specified jar file does not contain a 'Main-Class'" +
                  " manifest attribute");
        }
        String[] newArgs = new String[args.length - 1];
        System.arraycopy(args, 1, newArgs, 0, newArgs.length);
            cl.invokeClass(name, newArgs);
    }
    private static void fatal(String s) {
        System.err.println(s);
    }
}
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
