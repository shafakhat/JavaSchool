---
title: Demonstration of final class members
nav: Demonstration of final cla...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1141
source: https://web.archive.org/web/20140829085608/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstrationoffinalclassmembers.htm
---
```java title=Example.java
/*
 *     file: FinalMembers.java
 *  package: oreilly.hcj.finalstory
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class FinalMembers {
  /** Holds the creation date-time of the instance. */
  private Date creationDate =
    Calendar.getInstance(TimeZone.getTimeZone("GMT"))
            .getTime();
  /** Holds the modification date-time of the instance. */
  public Date modificationDate = creationDate;
  /**
   * Holds the creation date-time of the instance.  A protected version of createDate.
   */
  private final Date creationDate2 =
    Calendar.getInstance(TimeZone.getTimeZone("GMT"))
            .getTime();
  /** Holds the creation date-time of the instance. */
  private final Date creationDate3;
  /**
   * Constructor
   *
   * @param creationDate The creation date.
   * @param modificationDate The last modification date.
   *
   * @throws IllegalArgumentException if modificationDate is less than creationDate.
   */
  public FinalMembers(final Date creationDate, final Date modificationDate) {
    if (modificationDate.compareTo(creationDate) < 0) {
      throw new IllegalArgumentException("modificationDate");
    }
    this.creationDate3 = creationDate;
    // do a bunch of date calculations.
    // this.creationDate3 = modificationDate;  // <= compiler error
  }
  /**
   * Second constructor.  Use current date for creation date.
   *
   * @param modificationDate The last modification date.
   */
  public FinalMembers(final Date modificationDate) {
    this.modificationDate = modificationDate;
    // <= compiler error: ?reationDate may not have been initialized?
    creationDate3 = null;  // comment this out to get the compiler error.
  }
  /**
   * Get the Date-Time when the object was created.
   *
   * @return The creation date of the object.
   */
  public Date getCreationDate() {
    return this.creationDate;
  }
  /**
   * Get the Date-Time when the object was created. A protected version of createDate.
   *
   * @return The creation date of the object.
   */
  public Date getCreationDate2() {
    return this.creationDate2;
  }
  /**
   * Set the modification date of the object.
   *
   * @param modificationDate The new modification date.
   */
  public void setModificationDate(Date modificationDate) {
    this.creationDate = modificationDate;
  }
  /**
   * Get the modification date.
   *
   * @return The current modification date.
   */
  public Date getModificationDate() {
    return this.modificationDate;
  }
  /**
   * Set the modification date of the object.
   *
   * @param modificationDate The new modification date.
   *
   * @throws NullPointerException If the modification date is null.
   */
  public void setModificationDate2(Date modificationDate) {
    if (modificationDate == null) {
      throw new NullPointerException();
    }
    // this.creationDate2 = modificationDate; // <= Compiler error.
  }
  /**
   * Used just to supress eclipse warnings on unused variables; irrelevant to the
   * example.
   */
  protected void supress() {
    System.out.println(this.creationDate3);
  }
}
/* ########## End of File ########## */
```

| 5.27.1. | final Variables |
|---|---|
| 5.27.2. | 'Blank' final fields |
| 5.27.3. | Java Final variable: Once created and initialized, its value can not be changed |
| 5.27.4. | Using 'final' with method arguments |
| 5.27.5. | The effect of final on fields |
| 5.27.6. | You can override a private or private final method |
| 5.27.7. | Making an entire class final |
| 5.27.8. | Demonstrates how final variables are replaced at compilation time |
| 5.27.9. | Demonstration of final class members |
| 5.27.10. | Base class for demonstation of final methods |
| 5.27.11. | Demonstration of final constants |
| 5.27.12. | Demonstration of final variables |
