---
title: Check Logic In AfterReturningAdvice
nav: Check Logic In AfterReturn...
description: public void afterReturning(Object returnValue, Method method, Object[] args, Object target)
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20090130003119/http://www.java2s.com:80/Code/Java/Spring/CheckLogicInAfterReturningAdvice.htm
---
```java title=Example.java
File: Main.java
import java.lang.reflect.Method;
import org.springframework.aop.AfterReturningAdvice;
import org.springframework.aop.framework.ProxyFactory;
public class Main {
  public static void main(String[] args) {
    KeyGenerator target = new KeyGenerator();
    ProxyFactory factory = new ProxyFactory();
    factory.setTarget(target);
    factory.addAdvice(new WeakKeyCheckAdvice());
    KeyGenerator keyGen = (KeyGenerator) factory.getProxy();
    System.out.println("Key: " + keyGen.getKey());
  }
}
class KeyGenerator {
  public static final long WEAK_KEY = 1L;
  public static final long STRONG_KEY = 2L;
  public long getKey() {
    return WEAK_KEY;
    // return STRONG_KEY;
  }
}
class WeakKeyCheckAdvice implements AfterReturningAdvice {
  public void afterReturning(Object returnValue, Method method, Object[] args, Object target)
      throws Throwable {
    if ((target instanceof KeyGenerator) && ("getKey".equals(method.getName()))) {
      long key = (Long) returnValue;
      if (key == KeyGenerator.WEAK_KEY) {
        System.out.println("a weak key");
      }
    }
  }
}
```

Spring-CheckLogicInAfterReturningAdvice.zip( 4,745 k)
1.  DefaultPointcutAdvisor and AfterReturningAdvice
2.  AfterReturningAdvice Demo
3.  implements AfterReturningAdvice
