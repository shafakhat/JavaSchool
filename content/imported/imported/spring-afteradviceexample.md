---
title: After Advice Example
nav: After Advice Example
description: public class WeakKeyCheckAdvice implements AfterReturningAdvice {
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20070504160703/http://www.java2s.com:80/Code/Java/Spring/AfterAdviceExample.htm
---
After Advice Example

```java title=Example.java
/*
Pro Spring
By Rob Harrop
Jan Machacek
ISBN: 1-59059-461-4
Publisher: Apress
*/
////////////////////////////////////////////////////////
import java.util.Random;
public class KeyGenerator {
    public static final long WEAK_KEY = 0xFFFFFFF0000000L;
    public static final long STRONG_KEY = 0xACDF03F590AE56L;
    public long getKey() {
        Random rand = new Random();
        int x = rand.nextInt(3);
        if(x == 1) {
            return WEAK_KEY;
        } else {
            return STRONG_KEY;
        }
    }
}
////////////////////////////////////////////////////////
import java.lang.reflect.Method;
import org.springframework.aop.AfterReturningAdvice;
public class WeakKeyCheckAdvice implements AfterReturningAdvice {
    public void afterReturning(Object returnValue, Method method,
            Object[] args, Object target) throws Throwable {
        if ((target instanceof KeyGenerator)
                && ("getKey".equals(method.getName()))) {
            long key = ((Long) returnValue).longValue();
            if (key == KeyGenerator.WEAK_KEY) {
                throw new SecurityException(
                        "Key Generator generated a weak key. Try again");
            }
        }
    }
}
////////////////////////////////////////////////////////
import org.springframework.aop.framework.ProxyFactory;
public class AfterAdviceExample {
    public static void main(String[] args) {
        KeyGenerator keyGen = getKeyGenerator();
        for(int x = 0; x < 10; x++) {
            try {
                long key = keyGen.getKey();
                System.out.println("Key: " + key);
            } catch(SecurityException ex) {
                System.out.println("Weak Key Generated!");
            }
        }
    }
    private static KeyGenerator getKeyGenerator() {
        KeyGenerator target = new KeyGenerator();
        ProxyFactory factory = new ProxyFactory();
        factory.setTarget(target);
        factory.addAdvice(new WeakKeyCheckAdvice());
        return (KeyGenerator)factory.getProxy();
    }
}
```

Download: AfterAdviceExample.zip ( 1,479 K )
Related examples in the same category
