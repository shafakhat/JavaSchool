---
title: Using joinfork framework in Java
nav: Using joinfork framework i...
description: long result = forkJoinPool.invoke(new SumOfSquaresTask(0, numbers.length));
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20130820174838/http://java2s.com/Code/Java/JDK-7/UsingjoinforkframeworkinJava.htm
---
Using joinfork framework in Java

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
public class Test {
  public static void main(String[] args) {
    int numbers[] = new int[100000];
    ForkJoinPool forkJoinPool = new ForkJoinPool();
    long result = forkJoinPool.invoke(new SumOfSquaresTask(0, numbers.length));
    System.out.println("forkJoinPool: " + forkJoinPool.toString());
    System.out.println("forkJoinPool: " + forkJoinPool.toString());
    System.out.println("Sum of squares: " + result);
  }
}
class SumOfSquaresTask extends RecursiveTask<Long> {
  private int numbers[] = new int[100000];
  private int threshold = 1000;
  private int from;
  private int to;
  public SumOfSquaresTask(int from, int to) {
    this.from = from;
    this.to = to;
  }
  @Override
  protected Long compute() {
    long sum = 0L;
    int mid = (to + from) >>> 1;
    if ((to - from) < threshold) {
      for (int i = from; i < to; i++) {
        sum += numbers[i] * numbers[i];
      }
      return sum;
    } else {
      List<RecursiveTask<Long>> forks = new ArrayList<>();
      SumOfSquaresTask task1 = new SumOfSquaresTask(from, mid);
      SumOfSquaresTask task2 = new SumOfSquaresTask(mid, to);
      forks.add(task1);
      task1.fork();
      forks.add(task2);
      task2.fork();
      for (RecursiveTask<Long> task : forks) {
        sum += task.join();
      }
      return sum;
    }
  }
}
```
