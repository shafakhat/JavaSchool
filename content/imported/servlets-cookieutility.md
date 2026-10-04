---
title: Cookie Utility
nav: Cookie Utility
description: private static final List<Cookie> cookies = new LinkedList<Cookie>();
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20111125102535/http://java2s.com/Code/Java/Servlets/CookieUtility.htm
---
```java title=Example.java
/**
 * This file is distributed under the GPL
 * $Id: CookieUtility.java 1590 2008-08-27 18:24:10Z scotta $
 */
//package net.bnubot.util;
import java.util.LinkedList;
import java.util.List;
/**
 * @author scotta
 */
public class CookieUtility {
  private static class Cookie {
    private final int id;
    private final Object obj;
    public Cookie(int id, Object obj) {
      this.id = id;
      this.obj = obj;
    }
    public int getId() {
      return id;
    }
    public Object getObj() {
      return obj;
    }
  }
  private static final List<Cookie> cookies = new LinkedList<Cookie>();
  private static int currentCookieNumber = 0;
  /**
   * Creates a cookie
   * @param obj  The Object associated with the cookie
   * @return    Cookie ID
   */
  public static int createCookie(Object obj) {
    cookies.add(new Cookie(currentCookieNumber, obj));
    return currentCookieNumber++;
  }
  /**
   * Retrieve a cookie
   * @param id  Cookie ID
   * @return    The Object associated with the cookie
   */
  public static Object destroyCookie(int id) {
    for(Cookie c : cookies) {
      if(c.getId() == id) {
        cookies.remove(c);
        return c.getObj();
      }
    }
    return null;
  }
}
```

1.  Setting and Reading Cookies
---  ---
2.  Cookie Demo
3.  Cookie reader
4.  Use cookie to save session data
5.  A utility class for parsing HTTP dates as used in cookies and other headers
6.  Cookie Utilities
7.  Utilities for finding and manipulating cookies
8.  Parsing and formatting HTTP dates as used in cookies and other headers.
9.  Parse a Cookie: header into individual tokens according to RFC 2109.
10.  Cookie Util
