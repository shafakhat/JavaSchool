---
title: Java AtomicInteger extend
nav: Java AtomicInteger extend
description: System.out.printf("Main: Number of tasks: %d\n",counter.get());
section: Imported
order: 20040
source: http://www.java2s.com/ref/java/java-atomicinteger-extend.html
---
- java.util.concurrent.atomic
- java.util.concurrent.atomic AtomicInteger AtomicIntegerArray AtomicLong

## Description

Java AtomicInteger extend

```java title=Example.java
import java.util.concurrent.atomic.AtomicInteger;

class TaskCounter extendsAtomicInteger {

  privateint maxNumber;

  public TaskCounter(int maxNumber){
    super.set(0);
    this.maxNumber=maxNumber;
  }/*www.java2s.com*/publicboolean taskAdd() {
    while (true) {
      int value=super.get();
      if (value==maxNumber) {
        System.out.printf("The task pool is full.\n");
        return false;
      } else {
        int newValue=value+1;
        boolean changed=super.compareAndSet(value,newValue);
        if (changed) {
          System.out.printf("new task\n");
          return true;
        }
      }
    }
  }
  publicboolean taskComplete() {
    while (true) {
      int value=super.get();
      if (value==0) {
        System.out.printf("The task pool is empty.\n");
        return false;
      } else {
        int newValue=value-1;
        boolean changed=super.compareAndSet(value,newValue);
        if (changed) {
          System.out.printf("task finished\n");
          return true;
        }
      }
    }
  }

}
 class Tester implementsRunnable {
  private TaskCounter counter;
  public Tester(TaskCounter counter) {
    this.counter=counter;
  }
  @Overridepublicvoid run() {
    counter.taskAdd();
    counter.taskComplete();
    counter.taskComplete();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
  }

}
 class Developer implementsRunnable {
  private TaskCounter counter;
  public Developer(TaskCounter counter) {
    this.counter=counter;
  }
  @Overridepublicvoid run() {
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskComplete();
    counter.taskComplete();
    counter.taskComplete();
    counter.taskAdd();
    counter.taskAdd();
    counter.taskAdd();
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) throwsException{
    TaskCounter counter=new TaskCounter(5);
    Developer sensor1=new Developer(counter);
    Tester sensor2=new Tester(counter);

    Thread thread1=newThread(sensor1);
    Thread thread2=newThread(sensor2);

    thread1.start();
    thread2.start();
    thread1.join();
    thread2.join();
    System.out.printf("Main: Number of tasks: %d\n",counter.get());
  }
}
```

PreviousNext

## Related

- Java TimeUnit Enumeration
- Java TimeUnit convert milliseconds to hours
- Java AtomicInteger class
- Java AtomicIntegerArray class
- Java AtomicLong class
