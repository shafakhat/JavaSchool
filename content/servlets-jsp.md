---
title: Servlets and JSP
nav: Servlets & JSP
description: Java web fundamentals - servlet lifecycle, request/response handling, JSP, sessions and filters.
section: Advanced Java
order: 50
---

## The Java web stack

A quick map of the classic "Advanced Java" (Java EE / Jakarta EE) web layer:

| Technology | Role |
|---|---|
| **Servlet** | Java class handling HTTP requests (the workhorse) |
| **JSP** | HTML page with embedded Java (renders views; compiles to a servlet) |
| **Filter** | Intercept requests before/after servlets (auth, logging, gzip) |
| **Session** | Per-user state across requests (`HttpSession`) |
| **Listener** | React to app/session lifecycle events |
| Spring MVC / Boot | Modern framework built on top of these concepts |

> **Note:** Modern Jakarta EE uses the `jakarta.servlet.*` package (formerly `javax.servlet.*`). Code below shows `jakarta.*` - if your server still uses `javax`, change the imports.

## Your first servlet

```java title=HelloServlet.java
package com.example;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/hello")                       // URL mapping - no web.xml needed
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        String name = req.getParameter("name");       // /hello?name=Ada
        if (name == null || name.isBlank()) {
            name = "world";
        }

        resp.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = resp.getWriter()) {
            out.printf("<h1>Hello, %s!</h1>", name);
            out.printf("<p>Method: %s, URI: %s</p>",
                req.getMethod(), req.getRequestURI());
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        // read form data / JSON body, then redirect or render
        resp.sendRedirect("/hello");
    }
}
```

## Servlet lifecycle

```text title=life of a servlet
1. LOAD      -> container creates the servlet instance (once)
2. init()    -> one-time setup (config, pools)
3. service() -> every request -> doGet/doPost/doPut... (concurrent!)
4. destroy() -> shutdown: release resources
   (instance reused until undeployed)
```

Key implications:

- **One instance, many threads** - never store per-request data in fields (`doGet` runs concurrently). Use local variables or request attributes.
- Heavy setup (DB pools) belongs in `init()`; cleanup in `destroy()`.

## Reading requests

```java title=RequestDemo.java
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.BufferedReader;
import java.io.IOException;

public class RequestDemo extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        // query params
        String q = req.getParameter("q");
        String[] tags = req.getParameterValues("tags");   // repeated params

        // headers
        String ua = req.getHeader("User-Agent");
        String lang = req.getHeader("Accept-Language");

        // path info: /app/items/42 -> "/42"
        String path = req.getPathInfo();

        resp.getWriter().println("q=" + q + " tags=" + String.join(",", tags == null ? new String[0] : tags));
        resp.getWriter().println("ua=" + ua + " lang=" + lang + " path=" + path);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        // JSON body - read manually (or use a library)
        StringBuilder body = new StringBuilder();
        try (BufferedReader br = req.getReader()) {
            String line;
            while ((line = br.readLine()) != null) {
                body.append(line);
            }
        }
        resp.getWriter().println("got body: " + body);
    }
}
```

## Sessions (per-user state)

```java title=SessionDemo.java
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet("/cart")
public class SessionDemo extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        HttpSession session = req.getSession(true);       // create if absent
        Integer count = (Integer) session.getAttribute("count");
        count = (count == null) ? 1 : count + 1;
        session.setAttribute("count", count);

        resp.getWriter().println("visits this session: " + count);
        // session.invalidate();  // logout
    }
}
```

Under the hood sessions use cookies (`JSESSIONID`) or URL rewriting (`resp.encodeURL(...)` for cookie-less clients).

## Filters

```java title=LoggingFilter.java
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;

import java.io.IOException;
import java.time.Instant;

@WebFilter("/*")                            // every request passes through
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        long start = Instant.now().toEpochMilli();
        HttpServletRequest req = (HttpServletRequest) request;

        chain.doFilter(request, response);   // CONTINUE to the servlet - easy to forget!

        long took = Instant.now().toEpochMilli() - start;
        System.out.printf("%s %s -> %d ms%n",
            req.getMethod(), req.getRequestURI(), took);
    }
}
```

Typical uses: authentication gates, request logging, compression, CORS, encoding (`request.setCharacterEncoding("UTF-8")`).

## JSP in 30 lines

```jsp title=index.jsp (JSP)
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="java.util.List" %>
<html>
<body>
  <h1>Users</h1>
  <%
     // scriptlet - works, but modern style prefers JSTL/EL or templates
     List<String> users = (List<String>) request.getAttribute("users");
     for (String u : users) {
  %>
     <p><%= u %></p>
  <%
     }
  %>
</body>
</html>
```

The modern, preferred form uses Expression Language instead of Java blocks:

```jsp title=users.jsp (JSP + EL)
<h1>${title}</h1>
<ul>
  <c:forEach var="u" items="${users}">
    <li>${u.name} - ${u.email}</li>
  </c:forEach>
</ul>
```

> **Remember:** JSP scriptlets are legacy style. New code uses JSTL/EL, templating (Thymeleaf) or a framework (Spring MVC/Boot) - but you should still be able to *read* JSP, because tons of existing systems use it.

## Where to go next

- [JDBC](jdbc.html) - back your servlets with a database (pooled!).
- Imported section: dozens of real **Servlets / JSP / J2EE / EJB / Spring / Hibernate** code pages from the java2s archive in the sidebar.
- [Java Interview Questions](interview.html) - web-tier questions included.
