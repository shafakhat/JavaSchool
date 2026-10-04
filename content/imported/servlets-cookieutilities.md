---
title: Cookie Utilities
nav: Cookie Utilities
description: /**********************************************************************************
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20090926070757/http://www.java2s.com:80/Code/Java/Servlets/CookieUtilities.htm
---
```java title=Example.java
/**********************************************************************************
 *
 * Copyright (c) 2003, 2004 The Regents of the University of Michigan, Trustees of Indiana University,
 *                  Board of Trustees of the Leland Stanford, Jr., University, and The MIT Corporation
 *
 * Licensed under the Educational Community License Version 1.0 (the "License");
 * By obtaining, using and/or copying this Original Work, you agree that you have read,
 * understand, and will comply with the terms and conditions of the Educational Community License.
 * You may obtain a copy of the License at:
 *
 *      http://cvs.sakaiproject.org/licenses/license_1_0.html
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
 * AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 **********************************************************************************/
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class CookieUtils {
  private CookieUtils() {
  }
  /**
   * Get a new (empty) CookieData list return An empty ArrayList
   */
  public static List newCookieList() {
    return new ArrayList();
  }
  /**
   * Parse an HTTP cookie
   *
   * @param value
   *          Cookie value
   * @return A CookieData object representing this cookie
   */
  public static CookieData parseCookie(URL url, String value) {
    String[] cookieFields;
    CookieData cookie;
    cookieFields = value.split(";\\s*");
    cookie = makeCookieData(url, cookieFields[0]);
    for (int j = 1; j < cookieFields.length; j++) {
      if ("secure".equalsIgnoreCase(cookieFields[j])) {
        cookie.setSecure(true);
        continue;
      }
      if (cookieFields[j].indexOf('=') > 0) {
        String[] field = cookieFields[j].split("=");
        if ("expires".equalsIgnoreCase(field[0])) {
          cookie.setExpires(field[1]);
        } else if ("domain".equalsIgnoreCase(field[0])) {
          cookie.setDomain(field[1]);
        } else if ("path".equalsIgnoreCase(field[0])) {
          cookie.setPath(field[1]);
        } else if ("version".equalsIgnoreCase(field[0])) {
          cookie.setVersion(field[1]);
        } else if ("max-age".equalsIgnoreCase(field[0])) {
          cookie.setMaxAge(field[1]);
        }
      }
    }
    return cookie;
  }
  /**
   * Build a CookieData object from cookieName=cookieValue text
   *
   * @param url
   *          URL this cookie belongs to
   * @param cookieText
   *          cookieName[=cookieValue] text
   * @return A new CookieData object
   */
  private static CookieData makeCookieData(URL url, String cookieText) {
    for (int i = 0; i < cookieText.length(); i++) {
      if (cookieText.charAt(i) == '=') {
        String name = cookieText.substring(0, i);
        String value = "";
        if (i + 1 <= cookieText.length()) {
          value = cookieText.substring(i + 1);
        }
        return new CookieData(url, name, value);
      }
    }
    return new CookieData(url, cookieText, "");
  }
  /**
   * Maintain a list of CookieData objects (add, replace, or delete a cookie)
   *
   * @param cookieList
   *          CookieData list
   * @param cookie
   *          A CookieData object
   */
  public static void storeCookie(List cookieList, CookieData cookie) {
    int size = cookieList.size();
    for (int i = 0; i < size; i++) {
      CookieData cd = (CookieData) cookieList.get(i);
      if (cookie.equals(cd)) {
        if (cookie.getMaxAge() == 0) {
          cookieList.remove(i);
          return;
        }
        cookieList.set(i, cookie);
        return;
      }
    }
    if (cookie.getMaxAge() != 0) {
      cookieList.add(cookie);
    }
  }
  /**
   * Does the cookie domain match the URL?
   *
   * @param urlString
   *          URL String to match
   * @param cookie
   *          CookieData object (the cookie)
   * @return true if the cookie domain matches the URL
   */
  public static boolean inDomain(String urlString, CookieData cookie) {
    URL url;
    try {
      url = new URL(urlString);
    } catch (MalformedURLException exception) {
      return false;
    }
    return inDomain(url, cookie);
  }
  /**
   * Does the cookie domain match the URL?
   *
   * @param url
   *          URL to match
   * @param cookie
   *          CookieData object (the cookie)
   * @return true if the cookie domain matches the URL
   */
  public static boolean inDomain(URL url, CookieData cookie) {
    String domain = cookie.getDomain();
    return url.getHost().toLowerCase().endsWith(domain.toLowerCase());
  }
  /**
   * Does the cookie path match the URL "file"?
   *
   * @param urlString
   *          String URL to match
   * @param cookie
   *          CookieData object (the cookie)
   * @return true if the cookie domain matches the URL
   */
  public static boolean inPath(String urlString, CookieData cookie) {
    URL url;
    try {
      url = new URL(urlString);
    } catch (MalformedURLException exception) {
      return false;
    }
    return inPath(url, cookie);
  }
  /**
   * Does the cookie path match the URL "file"?
   *
   * @param url
   *          URL to match
   * @param cookie
   *          CookieData object (the cookie)
   * @return true if the cookie domain matches the URL
   */
  public static boolean inPath(URL url, CookieData cookie) {
    return url.getFile().startsWith(cookie.getPath());
  }
  /**
   * Find all stored cookies which associated with this server
   *
   * @param cookieList
   *          List of stored cookies (CookieData objects)
   * @param url
   *          URL representing the request to lookup (server)
   * @return A List of associated cookies
   */
  public static List findCookiesForServer(List cookieList, URL url) {
    Iterator iterator = cookieList.iterator();
    ArrayList list = new ArrayList();
    while (iterator.hasNext()) {
      CookieData cookie = (CookieData) iterator.next();
      if ((inDomain(url, cookie)) && (inPath(url, cookie))) {
        list.add(cookie);
      }
    }
    return list;
  }
  /**
   * Find cookies associated with this server (by name)
   *
   * @param cookieList
   *          List of stored cookies (CookieData objects)
   * @param url
   *          URL representing the request to lookup (server)
   * @param name
   *          Cookie name
   * @param exact
   *          true for exact name match, false to match on name prefix
   * @return A List of associated cookies
   */
  public static List getCookies(List cookieList, URL url, String name, boolean exact) {
    List serverCookies = findCookiesForServer(cookieList, url);
    Iterator iterator = serverCookies.iterator();
    ArrayList list = new ArrayList();
    while (iterator.hasNext()) {
      CookieData cookie = (CookieData) iterator.next();
      if (exact) {
        if (cookie.getName().equals(name)) {
          list.add(cookie);
        }
        continue;
      }
      if (cookie.getName().startsWith(name)) {
        list.add(cookie);
      }
    }
    return list;
  }
  /**
   * Find cookies associated with this server (exact name match)
   *
   * @param cookieList
   *          List of stored cookies (CookieData objects)
   * @param url
   *          URL representing the request to lookup (server)
   * @param name
   *          Cookie name
   * @return A List of associated cookies
   */
  public static List getCookiesByName(List cookieList, URL url, String name) {
    return getCookies(cookieList, url, name, true);
  }
  /**
   * Find cookies associated with this server (match on name "prefix")
   *
   * @param cookieList
   *          List of stored cookies (CookieData objects)
   * @param url
   *          URL representing the request to lookup (server)
   * @param name
   *          Cookie name
   * @return A List of associated cookies
   */
  public static List getCookiesByPrefix(List cookieList, URL url, String name) {
    return getCookies(cookieList, url, name, false);
  }
}
/*******************************************************************************
 *
 * Copyright (c) 2003, 2004 The Regents of the University of Michigan, Trustees
 * of Indiana University, Board of Trustees of the Leland Stanford, Jr.,
 * University, and The MIT Corporation
 *
 * Licensed under the Educational Community License Version 1.0 (the "License");
 * By obtaining, using and/or copying this Original Work, you agree that you
 * have read, understand, and will comply with the terms and conditions of the
 * Educational Community License. You may obtain a copy of the License at:
 *
 * http://cvs.sakaiproject.org/licenses/license_1_0.html
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 ******************************************************************************/
/**
 * Represent a single cookie
 */
class CookieData {
  /**
   * Null (unset) cookie age
   */
  public static final int NULL_AGE = -1;
  /**
   * Expired cookie
   */
  public static final int EXPIRED_AGE = 0;
  private String key;
  private String value;
  private String path;
  private String domain;
  private String version;
  private String expires;
  private int maxAge;
  private boolean secure;
  private CookieData() {
  }
  /**
   * Constructor
   *
   * @param url
   *          URL associated with this cookie
   * @param key
   *          Cookie name
   * @param value
   *          Cookie value
   */
  public CookieData(URL url, String key, String value) {
    int slash = url.getFile().lastIndexOf("/");
    /*
     * Save cookie name and content
     */
    this.key = key;
    this.value = value;
    /*
     * Domain defaults to hostname, path to the "directory" portion of the
     * request, minus all text from the rightmost "/" character to the end of
     * the string...
     */
    this.path = slash < 1 ? "" : url.getFile().substring(0, slash);
    this.domain = url.getHost();
    this.version = null;
    this.expires = null;
    this.maxAge = NULL_AGE;
    this.secure = false;
  }
  /**
   * Get cookie name
   *
   * @return The cooke name
   */
  public String getName() {
    return this.key;
  }
  /**
   * Get cookie value (the cookie "text")
   *
   * @return The value
   */
  public String getValue() {
    return this.value;
  }
  /**
   * Save the path
   */
  public void setPath(String path) {
    this.path = path;
  }
  /**
   * Get the path
   *
   * @return The cooke path attribute value (null if none)
   */
  public String getPath() {
    return this.path;
  }
  /**
   * Save the expiration date
   */
  public void setExpires(String expires) {
    this.expires = expires;
  }
  /**
   * Get the expiration date
   *
   * @return The expires attribute value (null if none)
   */
  public String getExpires() {
    return this.expires;
  }
  /**
   * Save the domain
   */
  public void setDomain(String domain) {
    this.domain = domain;
  }
  /**
   * Get the domain
   *
   * @return The domain attribute value (null if none)
   */
  public String getDomain() {
    return this.domain;
  }
  /**
   * Save the version
   */
  public void setVersion(String version) {
    this.version = version;
  }
  /**
   * Get the cookie version
   *
   * @return The version (null if none)
   */
  public String getVersion() {
    return this.version;
  }
  /**
   * Set the maximum age for this cookie
   */
  public void setMaxAge(String maxAge) {
    try {
      this.maxAge = Integer.parseInt(maxAge);
    } catch (NumberFormatException ignore) {
    }
  }
  /**
   * Get the maximum age for this cookie
   */
  public int getMaxAge() {
    return this.maxAge;
  }
  /**
   * Save security setting (true if cookie to be sent only via HTTPS)
   */
  public void setSecure(boolean secure) {
    this.secure = secure;
  }
  public boolean getSecure() {
    return this.secure;
  }
  /**
   * Equal strings?
   *
   * @param a
   *          String one
   * @param b
   *          Stringtwo
   * @return true if both are null, or String "equals" is true
   */
  private boolean stringEquals(String a, String b) {
    if ((a == null) && (b == null)) {
      return true;
    }
    if ((a == null) || (b == null)) {
      return false;
    }
    return a.equals(b);
  }
  /**
   * Equal cookies?
   *
   * @param cookie
   *          for comparison
   * @return true if cookie name, path, and domain are all equal
   */
  public boolean equals(CookieData cookie) {
    if (!key.equals(cookie.getName())) {
      return false;
    }
    return stringEquals(path, cookie.getPath()) && stringEquals(domain, cookie.getDomain());
  }
}
```

1.  Setting and Reading Cookies
---  ---
2.  Cookie Demo
3.  Cookie reader
4.  Use cookie to save session data
5.  A utility class for parsing HTTP dates as used in cookies and other headers
6.  Utilities for finding and manipulating cookies
7.  Parsing and formatting HTTP dates as used in cookies and other headers.
8.  Parse a Cookie: header into individual tokens according to RFC 2109.
