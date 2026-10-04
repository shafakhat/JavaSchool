---
title: Apache Struts
nav: Struts
description: Struts 2 architecture for Java web apps - action classes, interceptors, OGNL value stack, result types, and how it compares to Spring MVC.
section: Advanced Java
order: 90
---

## What Struts is

**Apache Struts** was the first widely adopted MVC framework for servlet/JSP apps (2000), still found in large legacy systems (and in famous CVEs - worth knowing for security reviews). Struts 2 (2007+) merged WebWork's design: **action classes + interceptor stack + OGNL value stack**, configured in `struts.xml` or annotations.

```text title=request path (Struts 2)
HTTP → FilterDispatcher / StrutsPrepareAndExecuteFilter
     → interceptor stack (params, validation, workflow, fileUpload...)
     → Action.execute()          ← your code, plain POJO
     → Result (JSP/FreeMarker/JSON) rendered
```

vs Spring MVC: Struts centers on *one filter + actions*; Spring centers on `DispatcherServlet` + controller/POJO beans with DI. New development in 2024+ is almost always Spring Boot / Jakarta EE / Quarkus - Struts means **maintaining or migrating legacy**.

## A working action

```java title=LoginAction.java
import com.opensymphony.xwork2.ActionSupport;
import org.apache.struts2.convention.annotation.*;

@Action(value = "login", results = {
    @Result(name = "success", location = "/WEB-INF/jsp/welcome.jsp"),
    @Result(name = "error",   location = "/WEB-INF/jsp/error.jsp")
})
public class LoginAction extends ActionSupport {

    private String username;   // OGNL binds request params to these
    private String password;

    @Override
    public String execute() {
        if ("ada".equals(username) && "lovelace".equals(password)) {
            // push your own data onto the value stack for the JSP
            ActionContext.getContext().getActionMap().put("user", username);
            return SUCCESS;
        }
        return ERROR;
    }

    // getters/setters are REQUIRED - OGNL uses them
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}
```

## struts.xml (classic configuration)

```xml title=struts.xml
<struts>
  <package name="app" namespace="/app" extends="struts-default">

    <!-- default interceptor stack: params, validation, workflow... -->
    <default-interceptor-ref name="defaultStack"/>

    <action name="login" class="com.example.LoginAction">
      <result name="success">/WEB-INF/jsp/welcome.jsp</result>
      <result name="error">/WEB-INF/jsp/error.jsp</result>
    </action>

    <action name="users.json" class="com.example.UserAction"
            method="jsonResult">
      <result type="json"/>
    </action>

  </package>
</struts>
```

## The interceptor stack (the real power)

```java title=CustomInterceptor.java
import com.opensymphony.xwork2.ActionInvocation;
import com.opensymphony.xwork2.interceptor.AbstractInterceptor;

public class TimingInterceptor extends AbstractInterceptor {
    @Override
    public String intercept(ActionInvocation inv) throws Exception {
        long t0 = System.currentTimeMillis();
        try {
            return inv.invoke();                 // continue the chain
        } finally {
            System.out.println(inv.getAction().getClass().getSimpleName()
                + " took " + (System.currentTimeMillis() - t0) + " ms");
        }
    }
}
```

Built-ins you'll meet in old configs: `params` (binds request → action), `validation` (XML/annotation rules), `workflow` (short-circuits invalid), `fileUpload`, `exception`, `prepare` (`prepare()` methods), `modelDriven`. Chained like middleware - same idea as Spring's `HandlerInterceptor` or servlet Filters.

## Value stack & OGNL

The **value stack** is the page's variable scope: action + beans + maps, with **OGNL** expressions reading/writing them:

```jsp title=welcome.jsp
<h1>Welcome, <s:property value="username"/>!</h1>
<!-- OGNL: value stack lookup, expressions like user.address.city,
     static calls (allowed list), collection projections -->
<s:iterator value="users">
  <li><s:property value="name"/></li>
</s:iterator>
```

> **Warning:** OGNL's power is exactly why Struts had critical RCE vulnerabilities (dev-mode, parameter exploitation). Legacy Struts must be patched to current versions, devMode off, and (ideally) migrated.

## Validation & types

```java title=LoginAction-validation.xml (alongside the action class)
<!DOCTYPE struts PUBLIC "-//Apache//DTD Struts Configuration 2.5//EN"
  "https://struts.apache.org/dtds/struts-2.5.dtd">
<struts>
  <package name="app-default" extends="struts-default">
    <!-- validation wired automatically via filename convention -->
  </package>
</struts>
```

XML validation (`validation.xml`: `validators.xml` rules - requiredstring, regex, int range), field/error messages via `fieldErrors`, `ActionMessages` for action-level. Types: `@ParentPackage`, conversion hooks, `ModelDriven` for pushing a domain object directly onto the stack.

## When you meet Struts in the wild

1. **Inventory** - version, plugins, struts.xml, custom interceptors, OGNL in JSPs.
2. **Stabilize** - upgrade to the latest 2.5.x/6.x (security), disable devMode.
3. **Strangle** - put Spring Boot (or plain servlets) beside it behind one front door; move functionality route by route; the action → controller mapping is usually 1:1.
4. **Delete** - when the last route moves off.

Related: [Servlets & JSP](servlets-jsp.html) · [Spring Framework & Boot](spring.html) · [JSTL examples in the archive](jsp-expressionlanguageexamples.html)
