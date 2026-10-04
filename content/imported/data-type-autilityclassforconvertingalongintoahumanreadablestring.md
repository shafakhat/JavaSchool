---
title: A utility class for converting a long into a human readable string.
nav: A utility class for conver...
description: * Copyright 2008, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autilityclassforconvertingalongintoahumanreadablestring.htm
---
```java title=Example.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2008, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */import java.io.Serializable;
/**
 * TimeFormat is a utility class for converting a long into a human readable
 * string.
 *
 *
 *
 * Example usage:
 *
 * <CODE> System.out.println("You have been online for:
 * "+TimeFormat.valueOf(milliseconds)); </CODE>
 *
 * FIXME: expanded features need documentation. JGH
 *
 * @author <a href="mailto:jhaynie@vocalocity.net">Jeff Haynie</a>
 * @date $Date: 2008-11-14 07:45:28 -0500 (Fri, 14 Nov 2008) $
 * @version $Revision: 81022 $
 */publicfinalclass TimeFormat implements Serializable {
  publicstaticfinalboolean DEBUG = false;
  publicstaticfinallong ONE_MILLISECOND = (1);
  publicstaticfinallong ONE_SECOND = (ONE_MILLISECOND * 1000);
  publicstaticfinallong ONE_MINUTE = (ONE_SECOND * 60);
  publicstaticfinallong ONE_HOUR = (ONE_MINUTE * 60);
  publicstaticfinallong ONE_DAY = (ONE_HOUR * 24);
  publicstaticfinalint ROUND_TO_MILLISECOND = 5;
  publicstaticfinalint ROUND_TO_SECOND = 4;
  publicstaticfinalint ROUND_TO_MINUTE = 3;
  publicstaticfinalint ROUND_TO_HOUR = 2;
  publicstaticfinalint ROUND_TO_DAY = 1;
  privatelong original = 0;
  privatelong time = 0;
  privatelong remainder = 0;
  privatelong days = 0;
  privatelong hours = 0;
  privatelong minutes = 0;
  privatelong seconds = 0;
  privatelong milliseconds = 0;
  privateboolean micro = false;
  privateint rounding = ROUND_TO_SECOND;
  /**
   * construct a time format
   *
   *
   * @param milliseconds
   */private TimeFormat(long milliseconds, int round) {
    this.rounding = round;
    this.original = milliseconds;
    if (milliseconds >= ONE_SECOND) {
      this.remainder = milliseconds;
      getTime();
    } else {
      micro = true;
      // if less than second, we'll just
// display
      time = milliseconds;
    }
  }
  /**
   * construct a time format
   *
   *
   * @param milliseconds
   */private TimeFormat(long milliseconds) {
    this(milliseconds, TimeFormat.ROUND_TO_MILLISECOND);
  }
  /**
   * get days
   *
   * @return days
   */publiclong getDays() {
    return days;
  }
  /**
   * get minutes
   *
   * @return minutes
   */publiclong getMinutes() {
    return minutes;
  }
  /**
   * get hours
   *
   * @return hours
   */publiclong getHours() {
    return hours;
  }
  /**
   * get seconds
   *
   * @return seconds
   */publiclong getSeconds() {
    return seconds;
  }
  /**
   * add a timeformat
   *
   *
   * @param t
   */publicvoid add(TimeFormat t) {
    days += t.days;
    hours += t.hours;
    minutes += t.minutes;
    seconds += t.seconds;
  }
  /**
   * get days from a time format
   *
   *
   * @param t
   */publicvoid getDays(TimeFormat t) {
    if (t.remainder >= ONE_DAY) {
      t.days = (t.remainder / ONE_DAY);
      t.remainder -= (t.days * ONE_DAY);
    }
  }
  /**
   * get hours from a time format
   *
   *
   * @param t
   */publicvoid getHours(TimeFormat t) {
    if (t.remainder >= ONE_HOUR && t.remainder < ONE_DAY) {
      t.hours = (t.remainder / ONE_HOUR);
      t.remainder -= (t.hours * ONE_HOUR);
    }
  }
  /**
   * get minutes from a time format
   *
   *
   * @param t
   */publicvoid getMinutes(TimeFormat t) {
    if (t.remainder >= ONE_MINUTE && t.remainder < ONE_HOUR) {
      t.minutes = (t.remainder / ONE_MINUTE);
      t.remainder -= (t.minutes * ONE_MINUTE);
    }
  }
  /**
   * get seconds from a time format
   *
   *
   * @param t
   */publicvoid getSeconds(TimeFormat t) {
    if (t.remainder >= ONE_SECOND && t.remainder < ONE_MINUTE) {
      t.seconds = (t.remainder / ONE_SECOND);
      t.milliseconds = t.remainder -= (t.seconds * ONE_SECOND);
    } else {
      t.seconds = 0;
      t.milliseconds = t.remainder;
    }
  }
  /**
   * update time
   *
   *
   * @param t
   */publicvoid getTime(TimeFormat t) {
    t.getTime();
  }
  /**
   * update
   *
   */privatevoid getTime() {
    getDays(this);
    getHours(this);
    getMinutes(this);
    getSeconds(this);
  }
  /**
   * get the milliseconds
   */publiclong getMilliseconds() {
    return (micro ? time : milliseconds);
  }
  /**
   * print out the time format in a string representation
   */public String toString() {
    return format(rounding);
  }
  /**
   * set rounding - one of ROUND_TO_MILLISECONDS, etc.
   */publicvoid setRounding(int r) {
    rounding = r;
  }
  /**
   * return the rounding
   */publicint getRouding() {
    return rounding;
  }
  /**
   * format string based on rouding
   */public String format(int round) {
    if (DEBUG) {
      System.err.println("-->time: " + time + ", round: " + round + ", micro: " + micro
          + ",remainder:" + remainder);
      System.err.println("-->days: " + days);
      System.err.println("-->hours: " + hours);
      System.err.println("-->minutes: " + minutes);
      System.err.println("-->hours: " + hours);
      System.err.println("-->seconds: " + seconds);
      System.err.println("-->milliseconds: " + milliseconds);
      System.err.flush();
    }
    switch (round) {
    case ROUND_TO_DAY: {
      return formatDays(false);
    }
    case ROUND_TO_HOUR: {
      return formatDays(true) + formatHours(false);
    }
    case ROUND_TO_MINUTE: {
      return formatDays(true) + formatHours(true) + formatMinutes(false);
    }
    case ROUND_TO_SECOND: {
      return formatDays(true) + formatHours(true) + formatMinutes(true) + formatSeconds(false);
    }
    case ROUND_TO_MILLISECOND: {
      return formatDays(true) + formatHours(true) + formatMinutes(true) + formatSeconds(true)
          + (micro ? time : milliseconds) + " ms";
    }
    }
    return original + " ms";
  }
  /**
   * FIXME: Missing Method declaration
   *
   *
   * @param empty
   * @return
   */private String formatDays(boolean empty) {
    if (days <= 0) {
      return empty ? "" : "0 days";
    }
    return format("day", "days", days);
  }
  /**
   * FIXME: Missing Method declaration
   *
   *
   * @param empty
   * @return
   */private String formatHours(boolean empty) {
    if (hours <= 0) {
      return empty ? "" : "0 hours";
    }
    return format("hour", "hours", hours);
  }
  /**
   * FIXME: Missing Method declaration
   *
   *
   * @param empty
   * @return
   */private String formatMinutes(boolean empty) {
    if (minutes <= 0) {
      return empty ? "" : "0 minutes";
    }
    return format("minute", "minutes", minutes);
  }
  /**
   * FIXME: Missing Method declaration
   *
   *
   * @param empty
   * @return
   */private String formatSeconds(boolean empty) {
    if (seconds <= 0) {
      return empty ? "" : "0 seconds";
    }
    return format("second", "seconds", seconds);
  }
  /**
   * handle amt formatting
   */private String format(String single, String plural, long amt) {
    if (amt > 0) {
      return amt + " " + (amt > 1 ? plural : single) + " ";
    }
    return"";
  }
  /**
   * return a string formatted version of time <code>t</code> rounding to
   * <code>round</code>
   *
   * @param t
   * @param round
   * @return String value
   */publicstatic String valueOf(long t, int round) {
    TimeFormat f = new TimeFormat(t, round);
    return f.toString();
  }
  /**
   * return a string formatted version of time <code>t</code> rounding to
   * <code>round</code>
   *
   * @param t
   * @param round
   * @return String value
   */publicstatic String valueOf(long t) {
    return valueOf(t, TimeFormat.ROUND_TO_MILLISECOND);
  }
  /**
   * format with a date time
   */publicstatic String format(String format, long time) {
    TimeFormat f = new TimeFormat(time);
    return f.parse(format, f.getDays(), f.getHours(), f.getMinutes(), f.getSeconds(), f
        .getMilliseconds());
  }
  /**
   * parse
   */private String parse(String format, long day, long hour, long minute, long second, long millis) {
    String s = "";
    int start = 0;
    int len = format.length();
    for (int c = 0; c < len; c++) {
      char tc = format.charAt(c);
      int sc = c;
      int l = 0;
      switch (tc) {
      case' ': {
        s += " ";
        break;
      }
      case'\'': {
        while (++c < len && format.charAt(c) != '\'')
          ;
        s += format.substring(sc + 1, c);
        break;
      }
      case'D': // days
case'd':
        while (++c < len && (format.charAt(c) == 'd' || format.charAt(c) == 'D'))
          ;
        l = c - sc;
        s += sc <= 0 || start < 0 ? "" : format.substring(start, sc);
        s += zeroPad(day, l - 1);
        --c;
        break;
      case'h': // hours
case'H':
        while (++c < len && (format.charAt(c) == 'h' || format.charAt(c) == 'H'))
          ;
        l = c - sc;
        s += sc <= 0 || start < 0 ? "" : format.substring(start, sc);
        s += zeroPad(hour, l - 1);
        --c;
        break;
      case'm': // minutes
case'M':
        while (++c < len && (format.charAt(c) == 'm' || format.charAt(c) == 'M'))
          ;
        l = c - sc;
        s += sc <= 0 || start < 0 ? "" : format.substring(start, sc);
        s += zeroPad(minute, l - 1);
        --c;
        break;
      case's': // seconds
case'S':
        while (++c < len && (format.charAt(c) == 's' || format.charAt(c) == 'S'))
          ;
        l = c - sc;
        s += sc <= 0 || start < 0 ? "" : format.substring(start, sc);
        s += zeroPad(second, l - 1);
        --c;
        break;
      case'z': // milliseconds
case'Z':
        while (++c < len && (format.charAt(c) == 'z' || format.charAt(c) == 'Z'))
          ;
        l = c - sc;
        s += sc <= 0 || start < 0 ? "" : format.substring(start, sc);
        s += zeroPad(millis, l - 1);
        --c;
        break;
      }
      start = c + 1;
    }
    return s;
  }
  /**
   * zero pad a number to len
   */private String zeroPad(long value, int len) {
    String s = String.valueOf(value);
    int l = s.length();
    String r = "";
    for (int c = l; c <= len; c++) {
      r += "0";
    }
    return r + s;
  }
  /**
   * test
   *
   *
   * @param args
   */publicstaticvoid main(String args[]) {
    String FORMAT = "D 'days,' HH 'hours,' mm 'minutes and ' ss 'seconds, 'zz 'milliseconds'";
    System.out.println(TimeFormat.format(FORMAT, 1000));
    System.out.println("ONE SECOND: " + TimeFormat.ONE_SECOND);
    System.out.println("ONE MINUTE: " + TimeFormat.ONE_MINUTE);
    System.out.println("ONE HOUR:   " + TimeFormat.ONE_HOUR);
    System.out.println("ONE DAY:    " + TimeFormat.ONE_DAY);
    for (int c = 0; c <= 5; c++) {
      System.out.println("Round to: " + c);
      System.out.println("Time: " + TimeFormat.valueOf(Long.MAX_VALUE, c));
      System.out.println("Time: " + TimeFormat.valueOf(1236371400, c));
      System.out.println("Time: " + TimeFormat.format(FORMAT, 1236371400));
      System.out.println("Time: " + TimeFormat.valueOf(123613700, c));
      System.out.println("Time: " + TimeFormat.valueOf(700, c));
      System.out.println("Time: " + TimeFormat.valueOf(2001, c));
      System.out.println("Time: " + TimeFormat.valueOf(2101, c));
      System.out.println("Time: " + TimeFormat.valueOf(15, c));
      System.out.println("Time: " + TimeFormat.valueOf(999, c));
      System.out.println("Time: " + TimeFormat.valueOf(10000, c));
      System.out.println("Time: " + TimeFormat.valueOf(ONE_MINUTE * 10, c));
      System.out.println("Time: " + TimeFormat.valueOf(ONE_DAY * 10 + 101, c));
      System.out.println("Time: " + TimeFormat.valueOf(ONE_HOUR * 10, c));
      System.out.println("Time: " + TimeFormat.valueOf(ONE_HOUR + ONE_DAY + (ONE_MINUTE * 2), c));
      System.out.println("Time: "
          + TimeFormat.format(FORMAT, ONE_HOUR + ONE_DAY + (ONE_MINUTE * 2)));
    }
  }
}
/**
 * $Log: 1 Head - DO NOT USE1.0 12/3/01 2:51:16 PM jhaynie $ Revision 1.2
 * 2001/08/31 22:04:24 jhaynie added parsing and formatting features
 *
 * Revision 1.1 2001/08/29 19:47:53 jhaynie initial checkin
 *
 */
```
