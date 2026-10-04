---
title: AfterReturningAdvice Demo
nav: AfterReturningAdvice Demo
description: import org.springframework.aop.aspectj.AspectJExpressionPointcut;
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20090130003114/http://www.java2s.com:80/Code/Java/Spring/AfterReturningAdviceDemo.htm
---
```java title=Example.java
File: Main.java
import org.springframework.aop.Advisor;
import org.springframework.aop.aspectj.AspectJExpressionPointcut;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.aop.support.DefaultPointcutAdvisor;
import bean.MyClass;
import bean.SimpleAfterAdvice;
public class Main {
  public static void main(String[] args) {
    MyClass target = new MyClass();
    AspectJExpressionPointcut pc = new AspectJExpressionPointcut();
    pc.setExpression("execution(* bean..*.get*(..))");
    Advisor advisor = new DefaultPointcutAdvisor(pc, new SimpleAfterAdvice());
    ProxyFactory pf = new ProxyFactory();
    pf.setTarget(target);
    pf.addAdvisor(advisor);
    MyClass proxy = (MyClass) pf.getProxy();
    System.out.println(proxy.getName());
    proxy.setName("New Name");
    System.out.println(proxy.getHeight());
  }
}
File: MyClass.java
package bean;
public class MyClass {
    public String getName() {
        return "AAA";
    }
    public void setName(String name) {
    }
    public int getHeight() {
        return 201;
    }
}
File: SimpleAfterAdvice.java
package bean;
import org.springframework.aop.AfterReturningAdvice;
import java.lang.reflect.Method;
public class SimpleAfterAdvice implements AfterReturningAdvice{
    public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
        System.out.println("After method: " + method);
    }
}
```

Spring-AfterReturningAdviceDemo.zip( 4,746 k)
1.  DefaultPointcutAdvisor and AfterReturningAdvice
2.  Check Logic In AfterReturningAdvice
3.  implements AfterReturningAdvice
