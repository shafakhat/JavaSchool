---
title: Composable Pointcut Example
nav: Composable Pointcut Example
description: //////////////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20070503114751/http://www.java2s.com:80/Code/Java/Spring/ComposablePointcutExample.htm
---
Composable Pointcut Example

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
//////////////////////////////////////////////////////////////////////////////////
import java.lang.reflect.Method;
import org.springframework.aop.MethodBeforeAdvice;
public class SimpleBeforeAdvice implements MethodBeforeAdvice {
    public void before(Method method, Object[] args, Object target)
            throws Throwable {
        System.out.println("Before method: " + method);
    }
}
//////////////////////////////////////////////////////////////////////////////////
public class SampleBean {
    public String getName() {
        return "Rob Harrop";
    }
    public void setName(String name) {
    }
    public int getAge() {
        return 100;
    }
}
//////////////////////////////////////////////////////////////////////////////////
import java.lang.reflect.Method;
import org.springframework.aop.Advisor;
import org.springframework.aop.ClassFilter;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.ComposablePointcut;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import org.springframework.aop.support.StaticMethodMatcher;
public class ComposablePointcutExample {
    public static void main(String[] args) {
        // create target
        SampleBean target = new SampleBean();
        ComposablePointcut pc = new ComposablePointcut(ClassFilter.TRUE,
                new GetterMethodMatcher());
        System.out.println("Test 1");
        SampleBean proxy = getProxy(pc, target);
        testInvoke(proxy);
        System.out.println("Test 2");
        pc.union(new SetterMethodMatcher());
        proxy = getProxy(pc, target);
        testInvoke(proxy);
        System.out.println("Test 3");
        pc.intersection(new GetAgeMethodMatcher());
        proxy = getProxy(pc, target);
        testInvoke(proxy);
    }
    private static SampleBean getProxy(ComposablePointcut pc, SampleBean target) {
        // create the advisor
        Advisor advisor = new DefaultPointcutAdvisor(pc,
                new SimpleBeforeAdvice());
        // create the proxy
        ProxyFactory pf = new ProxyFactory();
        pf.setTarget(target);
        pf.addAdvisor(advisor);
        return (SampleBean) pf.getProxy();
    }
    private static void testInvoke(SampleBean proxy) {
        proxy.getAge();
        proxy.getName();
        proxy.setName("Rob Harrop");
    }
    private static class GetterMethodMatcher extends StaticMethodMatcher {
        public boolean matches(Method method, Class cls) {
            return (method.getName().startsWith("get"));
        }
    }
    private static class GetAgeMethodMatcher extends StaticMethodMatcher {
        public boolean matches(Method method, Class cls) {
            return "getAge".equals(method.getName());
        }
    }
    private static class SetterMethodMatcher extends StaticMethodMatcher {
        public boolean matches(Method method, Class cls) {
            return (method.getName().startsWith("set"));
        }
    }
}
```

Download: ComposablePointcutExample.zip ( 1,482 K )
Related examples in the same category
