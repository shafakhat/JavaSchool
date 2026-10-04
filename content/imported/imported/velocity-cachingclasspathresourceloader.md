---
title: Caching Class path Resource Loader
nav: Caching Class path Resourc...
description: Caching Class path Resource Loader : Java examples (example source code) » Velocity » Resource Loader
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20060513085548/http://www.java2s.com/Code/Java/Velocity/CachingClasspathResourceLoader.htm
---
Caching Class path Resource Loader : Java examples (example source code) » Velocity » Resource Loader

Caching Class path Resource Loader

```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.collections.ExtendedProperties;
import org.apache.velocity.exception.ResourceNotFoundException;
import org.apache.velocity.runtime.resource.Resource;
import org.apache.velocity.runtime.resource.loader.ResourceLoader;
public class CachingClasspathResourceLoader extends ResourceLoader {
  private Map urlMap = new HashMap();
  public void init(ExtendedProperties configuration) {
  }
  public synchronized InputStream getResourceStream(String resourceName)
      throws ResourceNotFoundException {
    try {
      URL url = getURL(resourceName);
      if (url == null) {
        throw new ResourceNotFoundException("Can not find resource: "
            + resourceName);
      }
      return url.openStream();
    } catch (IOException e) {
      throw new ResourceNotFoundException("Can not find resource: "
          + resourceName + " - Reason: " + e.getMessage());
    }
  }
  public long getLastModified(Resource res) {
    try {
      URL url = getURL(res.getName());
      long lm = url.openConnection().getLastModified();
      return lm;
    } catch (Exception e) {
      rsvc.error(e);
      return 0;
    }
  }
  public boolean isSourceModified(Resource res) {
    long lastModified = getLastModified(res);
    return (lastModified != res.getLastModified());
  }
  private URL getURL(String rn) {
    if (urlMap.containsKey(rn)) {
      return (URL) urlMap.get(rn);
    }
    ClassLoader cl = this.getClass().getClassLoader();
    URL url = cl.getResource(rn);
    if (url != null) {
      urlMap.put(rn, url);
    }
    return url;
  }
}
```

Download: velocity-CachingClasspathResourceLoader.zip (2193 K)
---
Related examples in the same category
1. Resource Loader Demo
