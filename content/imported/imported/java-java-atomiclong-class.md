---
title: Java AtomicLong class
nav: Java AtomicLong class
description: System.out.printf("Account : Initial Balance: %d\n",account.getBalance());
section: Imported
order: 20039
source: http://www.java2s.com/ref/java/java-atomiclong-class.html
---
- java.util.concurrent.atomic
- java.util.concurrent.atomic AtomicInteger AtomicIntegerArray AtomicLong

## Description

Java AtomicLong class

```java title=Example.java
import java.util.concurrent.atomic.AtomicLong;
class Account {/*www.java2s.com*/privateAtomicLong balance;

  public Account(){
    balance=newAtomicLong();
  }
  publiclong getBalance() {
    return balance.get();
  }
  publicvoid setBalance(long balance) {
    this.balance.set(balance);
  }
  publicvoid addAmount(long amount) {
    this.balance.getAndAdd(amount);
  }

  publicvoid subtractAmount(long amount) {
    this.balance.getAndAdd(-amount);
  }

}
class Bank implementsRunnable {

  private Account account;

  public Bank(Account account) {
    this.account=account;
  }

  @Overridepublicvoid run() {
    for (int i=0; i<10; i++){
      account.subtractAmount(1000);
    }
  }

}
 class Company implementsRunnable {
  private Account account;
  public Company(Account account) {
    this.account=account;
  }
  @Overridepublicvoid run() {
    for (int i=0; i<10; i++){
      account.addAmount(1000);
    }
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Account account=new Account();
    account.setBalance(1000);

    Company company=new Company(account);
    Thread companyThread=newThread(company);
    Bank bank=new Bank(account);
    Thread bankThread=newThread(bank);

    System.out.printf("Account : Initial Balance: %d\n",account.getBalance());

    // Starts the Threads
    companyThread.start();
    bankThread.start();

    try {
      companyThread.join();
      bankThread.join();
      System.out.printf("Account : Final Balance: %d\n",account.getBalance());
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}
```

PreviousNext

## Related

- Java AtomicInteger class
- Java AtomicInteger extend
- Java AtomicIntegerArray class
- Java AtomicLong generate id for threads
- Java Lock implement
