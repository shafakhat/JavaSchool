---
title: Cache Filter
nav: Cache Filter
description: ************************************************************************************
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20090912060206/http://www.java2s.com:80/Code/Java/Servlets/CacheFilter.htm
---
```java title=Example.java
/*
 ************************************************************************************
 * Copyright (C) 2001-2006 Openbravo S.L.
 * Licensed under the Apache Software License version 2.0
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to  in writing,  software  distributed
 * under the License is distributed  on  an  "AS IS"  BASIS,  WITHOUT  WARRANTIES  OR
 * CONDITIONS OF ANY KIND, either  express  or  implied.  See  the  License  for  the
 * specific language governing permissions and limitations under the License.
 ************************************************************************************
 */
import java.io.IOException;
import java.util.ArrayList;
import java.util.Enumeration;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletResponse;
public class CacheFilter implements Filter {
  private String[][] replyHeaders = { {} };
  public void init(FilterConfig config) {
    Enumeration<?> names = config.getInitParameterNames();
    ArrayList<String[]> tmp = new ArrayList<String[]>();
    while (names.hasMoreElements()) {
      String name = (String) names.nextElement();
      String value = config.getInitParameter(name);
      String[] pair = { name, value };
      tmp.add(pair);
    }
    replyHeaders = new String[tmp.size()][2];
    tmp.toArray(replyHeaders);
  }
  public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
      throws IOException, ServletException {
    HttpServletResponse httpResponse = (HttpServletResponse) response;
    for (int n = 0; n < replyHeaders.length; n++) {
      String name = replyHeaders[n][0];
      String value = replyHeaders[n][1];
      httpResponse.addHeader(name, value);
    }
    chain.doFilter(request, response);
  }
  public void destroy() {
  }
}
```

1.  Filtering page to UTF-8
---  ---
2.  Response Filter
3.  Servlets Post Filter Demo
4.  Servlets Logging Filter Demo
5.  Another Filter Demo
6.  Servlets CSV Filter Demo
7.  Servlets SortFilter Demo
8.  Filter Using Parameter
9.  Jsp Using Chained Filter
10.  Logging Filter
11.  Restricting Filter
12.  Filter that performs filtering based on comparing the appropriate request
13.  JNDI Filter
14.  Email JNDI Filter
15.  Send filter
16.  Log Filter
17.  IP Filter
18.  Block Filter
19.  Checker Filter
20.  Servlet : session filter
21.  Parameter Filter
22.  HTML filter utility
23.  Compression Filter
24.  Request Filter
25.  Filter message string for characters that are sensitive in HTML
26.  Filter that wraps an HttpServletRequest to override "isUserInRole".
27.  Filter the specified message string for characters that are sensitive in HTML
