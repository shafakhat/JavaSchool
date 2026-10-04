---
title: Compression Filter
nav: Compression Filter
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20060904161910/http://www.java2s.com:80/Code/Java/Servlets/CompressionFilter.htm
---
Compression Filter

```java title=Example.java
/*
* Copyright 2004 The Apache Software Foundation
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
import java.io.IOException;
import java.util.Enumeration;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
/**
 * Implementation of <code>javax.servlet.Filter</code> used to compress
 * the ServletResponse if it is bigger than a threshold.
 *
 * @author Amy Roh
 * @author Dmitri Valdin
 * @version $Revision: 1.2 $, $Date: 2004/03/18 16:40:33 $
 */
public class CompressionFilter implements Filter{
    /**
     * The filter configuration object we are associated with.  If this value
     * is null, this filter instance is not currently configured.
     */
    private FilterConfig config = null;
    /**
     * Minimal reasonable threshold
     */
    private int minThreshold = 128;
    /**
     * The threshold number to compress
     */
    protected int compressionThreshold;
    /**
     * Debug level for this filter
     */
    private int debug = 0;
    /**
     * Place this filter into service.
     *
     * @param filterConfig The filter configuration object
     */
    public void init(FilterConfig filterConfig) {
        config = filterConfig;
        if (filterConfig != null) {
            String value = filterConfig.getInitParameter("debug");
            if (value!=null) {
                debug = Integer.parseInt(value);
            } else {
                debug = 0;
            }
            String str = filterConfig.getInitParameter("compressionThreshold");
            if (str!=null) {
                compressionThreshold = Integer.parseInt(str);
                if (compressionThreshold != 0 && compressionThreshold < minThreshold) {
                    if (debug > 0) {
                        System.out.println("compressionThreshold should be either 0 - no compression or >= " + minThreshold);
                        System.out.println("compressionThreshold set to " + minThreshold);
                    }
                    compressionThreshold = minThreshold;
                }
            } else {
                compressionThreshold = 0;
            }
        } else {
            compressionThreshold = 0;
        }
    }
    /**
    * Take this filter out of service.
    */
    public void destroy() {
        this.config = null;
    }
    /**
     * The <code>doFilter</code> method of the Filter is called by the container
     * each time a request/response pair is passed through the chain due
     * to a client request for a resource at the end of the chain.
     * The FilterChain passed into this method allows the Filter to pass on the
     * request and response to the next entity in the chain.<p>
     * This method first examines the request to check whether the client support
     * compression. <br>
     * It simply just pass the request and response if there is no support for
     * compression.<br>
     * If the compression support is available, it creates a
     * CompressionServletResponseWrapper object which compresses the content and
     * modifies the header if the content length is big enough.
     * It then invokes the next entity in the chain using the FilterChain object
     * (<code>chain.doFilter()</code>), <br>
     **/
    public void doFilter ( ServletRequest request, ServletResponse response,
                        FilterChain chain ) throws IOException, ServletException {
        if (debug > 0) {
            System.out.println("@doFilter");
        }
        if (compressionThreshold == 0) {
            if (debug > 0) {
                System.out.println("doFilter gets called, but compressionTreshold is set to 0 - no compression");
            }
            chain.doFilter(request, response);
            return;
        }
        boolean supportCompression = false;
        if (request instanceof HttpServletRequest) {
            if (debug > 1) {
                System.out.println("requestURI = " + ((HttpServletRequest)request).getRequestURI());
            }
            // Are we allowed to compress ?
            String s = (String) ((HttpServletRequest)request).getParameter("gzip");
            if ("false".equals(s)) {
                if (debug > 0) {
                    System.out.println("got parameter gzip=false --> don't compress, just chain filter");
                }
                chain.doFilter(request, response);
                return;
            }
            Enumeration e =
                ((HttpServletRequest)request).getHeaders("Accept-Encoding");
            while (e.hasMoreElements()) {
                String name = (String)e.nextElement();
                if (name.indexOf("gzip") != -1) {
                    if (debug > 0) {
                        System.out.println("supports compression");
                    }
                    supportCompression = true;
                } else {
                    if (debug > 0) {
                        System.out.println("no support for compresion");
                    }
                }
            }
        }
        if (!supportCompression) {
            if (debug > 0) {
                System.out.println("doFilter gets called wo compression");
            }
            chain.doFilter(request, response);
            return;
        } else {
            if (response instanceof HttpServletResponse) {
                CompressionServletResponseWrapper wrappedResponse =
                    new CompressionServletResponseWrapper((HttpServletResponse)response);
                wrappedResponse.setDebugLevel(debug);
                wrappedResponse.setCompressionThreshold(compressionThreshold);
                if (debug > 0) {
                    System.out.println("doFilter gets called with compression");
                }
                try {
                    chain.doFilter(request, wrappedResponse);
                } finally {
                    wrappedResponse.finishResponse();
                }
                return;
            }
        }
    }
    /**
     * Set filter config
     * This function is equivalent to init. Required by Weblogic 6.1
     *
     * @param filterConfig The filter configuration object
     */
    public void setFilterConfig(FilterConfig filterConfig) {
        init(filterConfig);
    }
    /**
     * Return filter config
     * Required by Weblogic 6.1
     */
    public FilterConfig getFilterConfig() {
        return config;
    }
}
/*
* Copyright 2004 The Apache Software Foundation
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
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;
import javax.servlet.*;
import javax.servlet.http.*;
/**
 * Very Simple test servlet to test compression filter
 * @author Amy Roh
 * @version $Revision: 1.2 $, $Date: 2004/03/18 16:40:33 $
 */
public class CompressionFilterTestServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        ServletOutputStream out = response.getOutputStream();
        response.setContentType("text/plain");
        Enumeration e = ((HttpServletRequest)request).getHeaders("Accept-Encoding");
        while (e.hasMoreElements()) {
            String name = (String)e.nextElement();
            out.println(name);
            if (name.indexOf("gzip") != -1) {
                out.println("gzip supported -- able to compress");
            }
            else {
                out.println("gzip not supported");
            }
        }
        out.println("Compression Filter Test Servlet");
        out.close();
    }
}
```

Related examples in the same category
---
1. Filtering page to UTF-8
2. Response Filter
3. Servlets Post Filter Demo
4. Servlets Logging Filter Demo
5. Another Filter Demo
6. Servlets CSV Filter Demo
7. Servlets SortFilter Demo
8. Filter Using Parameter
9. Jsp Using Chained Filter
10. Logging Filter
11. Restricting Filter
12. Filter that performs filtering based on comparing the appropriate request
13. JNDI Filter
14. Email JNDI Filter
15. Send filter
16. Log Filter
17. IP Filter
18. Block Filter
19. Checker Filter
20. Servlet : session filter
21. Parameter Filter
22. HTML filter utility
23. Request Filter
