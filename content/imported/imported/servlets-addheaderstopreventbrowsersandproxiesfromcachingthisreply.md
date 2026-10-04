---
title: Add headers to prevent browsers and proxies from caching this reply.
nav: Add headers to prevent bro...
description: Add headers to prevent browsers and proxies from caching this reply.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20100212011225/http://java2s.com/Code/Java/Servlets/Addheaderstopreventbrowsersandproxiesfromcachingthisreply.htm
---
Add headers to prevent browsers and proxies from caching this reply.

```java title=Example.java
import javax.servlet.http.HttpServletResponse;
/*
 * Copyright 2005 Joe Walker
 *
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
/**
 * @author Joe Walker [joe at getahead dot ltd dot uk]
 */
public class Main {
  /**
   * Add headers to prevent browsers and proxies from caching this reply.
   * @param resp The response to add headers to
   */
  public static void addNoCacheHeaders(HttpServletResponse resp)
  {
      // Set standard HTTP/1.1 no-cache headers.
      resp.setHeader("Cache-Control", "no-store, no-cache, must-revalidate");
      // Set IE extended HTTP/1.1 no-cache headers (use addHeader).
      resp.addHeader("Cache-Control", "post-check=0, pre-check=0");
      // Set standard HTTP/1.0 no-cache header.
      resp.setHeader("Pragma", "no-cache");
      // Set to expire far in the past. Prevents caching at the proxy server
      resp.setHeader("Expires", "Sat, 6 May 1995 12:00:00 GMT");
  }
}
```

1.  Set content type to charset=ISO-8850-1
---  ---
2.  URL rewriting through HttpServletResponse
3.  Get output stream from HttpServletResponse
