---
title: Java Utililty Methods Age Calculate
nav: Java Utililty Methods Age ...
description: The list of methods to do Age Calculate are organized into topic(s).
section: Imported - java2s Archive
order: 50016
source: https://www.java2s.com/example/java-utility-method/age-calculate-index-0.html
---
List of utility methods to do Age Calculate

## Description

The list of methods to do Age Calculate are organized into topic(s).

## Method

int[]age(Date birthdate, Date asOf) Compute the age returning an array of integers, for year, month, and day respectively.

```java title=Example.java
Calendar from = Calendar.getInstance();
Calendar to = Calendar.getInstance();
from.setTime(birthdate);
to.setTime(asOf);
int birthYYYY = from.get(Calendar.YEAR);
int birthMM = from.get(Calendar.MONTH);
int birthDD = from.get(Calendar.DAY_OF_MONTH);
int asofYYYY = to.get(Calendar.YEAR);
...
```

intage(Date dob) age

```java title=Example.java
Calendar from = Calendar.getInstance();
Calendar to = Calendar.getInstance();
from.setTime(dob);
to.setTime(newDate());
int birthYYYY = from.get(Calendar.YEAR);
int curYYYY = to.get(Calendar.YEAR);
int ageInYears = curYYYY - birthYYYY;
if (ageInYears < 0)
...
```

intage(int year, int month, int date) This method returns the age on the basis of parameter passed to the method.

```java title=Example.java
Calendar cal = newGregorianCalendar(year, month, date);
Calendar now = newGregorianCalendar();
int age = now.get(Calendar.YEAR) - cal.get(Calendar.YEAR);
if ((cal.get(Calendar.MONTH) > now.get(Calendar.MONTH))
        || (cal.get(Calendar.MONTH) == now.get(Calendar.MONTH)
                && cal.get(Calendar.DAY_OF_MONTH) > now.get(Calendar.DAY_OF_MONTH))) {
    age--;
return age;
```

booleanageAcceptable(final Date doB, final Date now, final int acceptedAge) age Acceptable

```java title=Example.java
Calendar dateOfBirth = Calendar.getInstance();
dateOfBirth.setTime(doB);
Calendar today = Calendar.getInstance();
if (now != null)
    today.setTime(now);
int age = today.get(Calendar.YEAR) - dateOfBirth.get(Calendar.YEAR);
if (dateOfBirth.get(Calendar.MONTH) > today.get(Calendar.MONTH)) {
    age--;
...
```

intageInYears(java.util.Date dateUtil) age In Years

```java title=Example.java
Calendar calend = newGregorianCalendar();
java.util.Date now = new java.util.Date();
calend.set(Calendar.HOUR_OF_DAY, 0);
calend.set(Calendar.MINUTE, 0);
calend.set(Calendar.SECOND, 0);
calend.set(Calendar.MILLISECOND, 0);
calend.setTimeInMillis(now.getTime() - dateUtil.getTime());
float result = 0;
...
```

intcalculateAge(Date aBirthdate) FILLIN

```java title=Example.java
Calendar myAge = Calendar.getInstance(Locale.getDefault());
myAge.setTimeInMillis(Math.abs(aBirthdate.getTime() - System.currentTimeMillis()));
return myAge.get(Calendar.YEAR) - 1970;
```

intcalculateAge(Date aDateFrom, Date aDateTo) calculate Age

```java title=Example.java
int result;
Calendar myDateFrom = newGregorianCalendar();
Calendar myDateTo = newGregorianCalendar();
myDateFrom.setTime(aDateFrom);
myDateTo.setTime(aDateTo);
result = myDateTo.get(Calendar.YEAR) - myDateFrom.get(Calendar.YEAR);
myDateFrom.set(Calendar.YEAR, myDateTo.get(Calendar.YEAR));
if (myDateFrom.after(myDateTo)) {
...
```

intcalculateAge(Date birthDate) This method is used to calculate Age.

```java title=Example.java
int age = 0;
Calendar c = Calendar.getInstance();
c.setTime(birthDate);
age = Calendar.getInstance().get(Calendar.YEAR) - c.get(Calendar.YEAR);
if (Calendar.getInstance().get(Calendar.MONTH) < c.get(Calendar.MONTH)) {
    age--;
} elseif (Calendar.getInstance().get(Calendar.MONTH) == c.get(Calendar.MONTH)
        && Calendar.getInstance().get(Calendar.DAY_OF_MONTH) < c.get(Calendar.DAY_OF_MONTH)) {
...
```

intcalculateAge(Date birthday) calculate Age

```java title=Example.java
Calendar today = Calendar.getInstance();
Calendar birth = Calendar.getInstance();
birth.setTime(birthday);
int todayYear = today.get(Calendar.YEAR);
int birthYear = birth.get(Calendar.YEAR);
return todayYear - birthYear;
```

intcalculateAge(Date dateOfBirth) calculate Age

```java title=Example.java
Calendar dob = Calendar.getInstance();
dob.setTime(dateOfBirth);
Calendar today = Calendar.getInstance();
int age = today.get(Calendar.YEAR) - dob.get(Calendar.YEAR);
if (today.get(Calendar.DAY_OF_YEAR) < dob.get(Calendar.DAY_OF_YEAR)) {
    age--;
return age;
...
```
