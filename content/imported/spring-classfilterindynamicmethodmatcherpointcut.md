---
title: ClassFilter In DynamicMethodMatcherPointcut
nav: ClassFilter In DynamicMeth...
description: import org.springframework.aop.support.DefaultPointcutAdvisor;
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20100211070041/http://java2s.com/Code/Java/Spring/ClassFilterInDynamicMethodMatcherPointcut.htm
---
```java title=Example.java
File: Main.java
import java.lang.reflect.Method;
import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;
import org.springframework.aop.Advisor;
import org.springframework.aop.ClassFilter;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import org.springframework.aop.support.DynamicMethodMatcherPointcut;
public class Main {
  public static void main(String[] args) {
    MyClass target = new MyClass();
    Advisor advisor = new DefaultPointcutAdvisor(new SimpleDynamicPointcut(), new SimpleAdvice());
    ProxyFactory pf = new ProxyFactory();
    pf.setTarget(target);
    pf.addAdvisor(advisor);
    MyClass proxy = (MyClass) pf.getProxy();
    proxy.foo(1);
    proxy.bar();
  }
}
class MyClass {
  public void foo(int x) {
    System.out.println("MyClass.foo() : " + x);
  }
  public void bar() {
    System.out.println("MyClass.bar()");
  }
}
class SimpleAdvice implements MethodInterceptor {
  public Object invoke(MethodInvocation invocation) throws Throwable {
    System.out.println("SimpleAdivce.Invoking " + invocation.getMethod().getName());
    Object retVal = invocation.proceed();
    System.out.println("SimpleAdvice.Done");
    return retVal;
  }
}
class SimpleDynamicPointcut extends DynamicMethodMatcherPointcut {
  public boolean matches(Method method, Class cls) {
    return ("foo".equals(method.getName()));
  }
  public boolean matches(Method method, Class cls, Object[] args) {
    int x = (Integer) args[0];
    return (x != 100);
  }
  public ClassFilter getClassFilter() {
    return new ClassFilter() {
      public boolean matches(Class cls) {
        return (cls == MyClass.class);
      }
    };
  }
}
```

Spring-ClassFilterInDynamicMethodMatcherPointcut.zip( 4,747 k)
