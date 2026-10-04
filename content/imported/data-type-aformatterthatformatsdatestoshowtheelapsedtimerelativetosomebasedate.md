---
title: A formatter that formats dates to show the elapsed time relative to some base date.
nav: A formatter that formats d...
description: * JFreeChart : a free chart library for the Java(tm) platform
section: Imported - java2s Archive
order: 1283
source: https://web.archive.org/web/20140810031848/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Aformatterthatformatsdatestoshowtheelapsedtimerelativetosomebasedate.htm
---
```java title=Example.java
/*
 * JFreeChart : a free chart library for the Java(tm) platform
 *
 *
 * (C) Copyright 2000-2008, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jfreechart/index.html
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or
 * (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc.
 * in the United States and other countries.]
 *
 * -----------------------
 * RelativeDateFormat.java
 * -----------------------
 * (C) Copyright 2006-2008, by Object Refinery Limited and Contributors.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   Michael Siemer;
 *
 * Changes:
 * --------
 * 01-Nov-2006 : Version 1 (DG);
 * 23-Nov-2006 : Added argument checks, updated equals(), added clone() and
 *               hashCode() (DG);
 * 15-Feb-2008 : Applied patch 1873328 by Michael Siemer, with minor
 *               modifications (DG);
 * 01-Sep-2008 : Added new fields for hour and minute formatting, based on
 *               patch 2033092 (DG);
 *
 */
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.FieldPosition;
import java.text.NumberFormat;
import java.text.ParsePosition;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
/**
 * A formatter that formats dates to show the elapsed time relative to some
 * base date.
 *
 * @since 1.0.3
 */
public class RelativeDateFormat extends DateFormat {
    /** The base milliseconds for the elapsed time calculation. */
    private long baseMillis;
    /**
     * A flag that controls whether or not a zero day count is displayed.
     */
    private boolean showZeroDays;
    /**
     * A flag that controls whether or not a zero hour count is displayed.
     *
     * @since 1.0.10
     */
    private boolean showZeroHours;
    /**
     * A formatter for the day count (most likely not critical until the
     * day count exceeds 999).
     */
    private NumberFormat dayFormatter;
    /**
     * A prefix prepended to the start of the format if the relative date is
     * positive.
     *
     * @since 1.0.10
     */
    private String positivePrefix;
    /**
     * A string appended after the day count.
     */
    private String daySuffix;
    /**
     * A formatter for the hours.
     *
     * @since 1.0.11
     */
    private NumberFormat hourFormatter;
    /**
     * A string appended after the hours.
     */
    private String hourSuffix;
    /**
     * A formatter for the minutes.
     *
     * @since 1.0.11
     */
    private NumberFormat minuteFormatter;
    /**
     * A string appended after the minutes.
     */
    private String minuteSuffix;
    /**
     * A formatter for the seconds (and milliseconds).
     */
    private NumberFormat secondFormatter;
    /**
     * A string appended after the seconds.
     */
    private String secondSuffix;
    /**
     * A constant for the number of milliseconds in one hour.
     */
    private static long MILLISECONDS_IN_ONE_HOUR = 60 * 60 * 1000L;
    /**
     * A constant for the number of milliseconds in one day.
     */
    private static long MILLISECONDS_IN_ONE_DAY = 24 * MILLISECONDS_IN_ONE_HOUR;
    /**
     * Creates a new instance with base milliseconds set to zero.
     */
    public RelativeDateFormat() {
        this(0L);
    }
    /**
     * Creates a new instance.
     *
     * @param time  the date/time (<code>null</code> not permitted).
     */
    public RelativeDateFormat(Date time) {
        this(time.getTime());
    }
    /**
     * Creates a new instance.
     *
     * @param baseMillis  the time zone (<code>null</code> not permitted).
     */
    public RelativeDateFormat(long baseMillis) {
        super();
        this.baseMillis = baseMillis;
        this.showZeroDays = false;
        this.showZeroHours = true;
        this.positivePrefix = "";
        this.dayFormatter = NumberFormat.getNumberInstance();
        this.daySuffix = "d";
        this.hourFormatter = NumberFormat.getNumberInstance();
        this.hourSuffix = "h";
        this.minuteFormatter = NumberFormat.getNumberInstance();
        this.minuteSuffix = "m";
        this.secondFormatter = NumberFormat.getNumberInstance();
        this.secondFormatter.setMaximumFractionDigits(3);
        this.secondFormatter.setMinimumFractionDigits(3);
        this.secondSuffix = "s";
        // we don't use the calendar or numberFormat fields, but equals(Object)
        // is failing without them being non-null
        this.calendar = new GregorianCalendar();
        this.numberFormat = new DecimalFormat("0");
    }
    /**
     * Returns the base date/time used to calculate the elapsed time for
     * display.
     *
     * @return The base date/time in milliseconds since 1-Jan-1970.
     *
     * @see #setBaseMillis(long)
     */
    public long getBaseMillis() {
        return this.baseMillis;
    }
    /**
     * Sets the base date/time used to calculate the elapsed time for display.
     * This should be specified in milliseconds using the same encoding as
     * <code>java.util.Date</code>.
     *
     * @param baseMillis  the base date/time in milliseconds.
     *
     * @see #getBaseMillis()
     */
    public void setBaseMillis(long baseMillis) {
        this.baseMillis = baseMillis;
    }
    /**
     * Returns the flag that controls whether or not zero day counts are
     * shown in the formatted output.
     *
     * @return The flag.
     *
     * @see #setShowZeroDays(boolean)
     */
    public boolean getShowZeroDays() {
        return this.showZeroDays;
    }
    /**
     * Sets the flag that controls whether or not zero day counts are shown
     * in the formatted output.
     *
     * @param show  the flag.
     *
     * @see #getShowZeroDays()
     */
    public void setShowZeroDays(boolean show) {
        this.showZeroDays = show;
    }
    /**
     * Returns the flag that controls whether or not zero hour counts are
     * shown in the formatted output.
     *
     * @return The flag.
     *
     * @see #setShowZeroHours(boolean)
     *
     * @since 1.0.10
     */
    public boolean getShowZeroHours() {
        return this.showZeroHours;
    }
    /**
     * Sets the flag that controls whether or not zero hour counts are shown
     * in the formatted output.
     *
     * @param show  the flag.
     *
     * @see #getShowZeroHours()
     *
     * @since 1.0.10
     */
    public void setShowZeroHours(boolean show) {
        this.showZeroHours = show;
    }
    /**
     * Returns the string that is prepended to the format if the relative time
     * is positive.
     *
     * @return The string (never <code>null</code>).
     *
     * @see #setPositivePrefix(String)
     *
     * @since 1.0.10
     */
    public String getPositivePrefix() {
        return this.positivePrefix;
    }
    /**
     * Sets the string that is prepended to the format if the relative time is
     * positive.
     *
     * @param prefix  the prefix (<code>null</code> not permitted).
     *
     * @see #getPositivePrefix()
     *
     * @since 1.0.10
     */
    public void setPositivePrefix(String prefix) {
        if (prefix == null) {
            throw new IllegalArgumentException("Null 'prefix' argument.");
        }
        this.positivePrefix = prefix;
    }
    /**
     * Sets the formatter for the days.
     *
     * @param formatter  the formatter (<code>null</code> not permitted).
     *
     * @since 1.0.11
     */
    public void setDayFormatter(NumberFormat formatter) {
        if (formatter == null) {
            throw new IllegalArgumentException("Null 'formatter' argument.");
        }
        this.dayFormatter = formatter;
    }
    /**
     * Returns the string that is appended to the day count.
     *
     * @return The string.
     *
     * @see #setDaySuffix(String)
     */
    public String getDaySuffix() {
        return this.daySuffix;
    }
    /**
     * Sets the string that is appended to the day count.
     *
     * @param suffix  the suffix (<code>null</code> not permitted).
     *
     * @see #getDaySuffix()
     */
    public void setDaySuffix(String suffix) {
        if (suffix == null) {
            throw new IllegalArgumentException("Null 'suffix' argument.");
        }
        this.daySuffix = suffix;
    }
    /**
     * Sets the formatter for the hours.
     *
     * @param formatter  the formatter (<code>null</code> not permitted).
     *
     * @since 1.0.11
     */
    public void setHourFormatter(NumberFormat formatter) {
        if (formatter == null) {
            throw new IllegalArgumentException("Null 'formatter' argument.");
        }
        this.hourFormatter = formatter;
    }
    /**
     * Returns the string that is appended to the hour count.
     *
     * @return The string.
     *
     * @see #setHourSuffix(String)
     */
    public String getHourSuffix() {
        return this.hourSuffix;
    }
    /**
     * Sets the string that is appended to the hour count.
     *
     * @param suffix  the suffix (<code>null</code> not permitted).
     *
     * @see #getHourSuffix()
     */
    public void setHourSuffix(String suffix) {
        if (suffix == null) {
            throw new IllegalArgumentException("Null 'suffix' argument.");
        }
        this.hourSuffix = suffix;
    }
    /**
     * Sets the formatter for the minutes.
     *
     * @param formatter  the formatter (<code>null</code> not permitted).
     *
     * @since 1.0.11
     */
    public void setMinuteFormatter(NumberFormat formatter) {
        if (formatter == null) {
            throw new IllegalArgumentException("Null 'formatter' argument.");
        }
        this.minuteFormatter = formatter;
    }
    /**
     * Returns the string that is appended to the minute count.
     *
     * @return The string.
     *
     * @see #setMinuteSuffix(String)
     */
    public String getMinuteSuffix() {
        return this.minuteSuffix;
    }
    /**
     * Sets the string that is appended to the minute count.
     *
     * @param suffix  the suffix (<code>null</code> not permitted).
     *
     * @see #getMinuteSuffix()
     */
    public void setMinuteSuffix(String suffix) {
        if (suffix == null) {
            throw new IllegalArgumentException("Null 'suffix' argument.");
        }
        this.minuteSuffix = suffix;
    }
    /**
     * Returns the string that is appended to the second count.
     *
     * @return The string.
     *
     * @see #setSecondSuffix(String)
     */
    public String getSecondSuffix() {
        return this.secondSuffix;
    }
    /**
     * Sets the string that is appended to the second count.
     *
     * @param suffix  the suffix (<code>null</code> not permitted).
     *
     * @see #getSecondSuffix()
     */
    public void setSecondSuffix(String suffix) {
        if (suffix == null) {
            throw new IllegalArgumentException("Null 'suffix' argument.");
        }
        this.secondSuffix = suffix;
    }
    /**
     * Sets the formatter for the seconds and milliseconds.
     *
     * @param formatter  the formatter (<code>null</code> not permitted).
     */
    public void setSecondFormatter(NumberFormat formatter) {
        if (formatter == null) {
            throw new IllegalArgumentException("Null 'formatter' argument.");
        }
        this.secondFormatter = formatter;
    }
    /**
     * Formats the given date as the amount of elapsed time (relative to the
     * base date specified in the constructor).
     *
     * @param date  the date.
     * @param toAppendTo  the string buffer.
     * @param fieldPosition  the field position.
     *
     * @return The formatted date.
     */
    public StringBuffer format(Date date, StringBuffer toAppendTo,
                               FieldPosition fieldPosition) {
        long currentMillis = date.getTime();
        long elapsed = currentMillis - this.baseMillis;
        String signPrefix;
        if (elapsed < 0) {
            elapsed *= -1L;
            signPrefix = "-";
        }
        else {
            signPrefix = this.positivePrefix;
        }
        long days = elapsed / MILLISECONDS_IN_ONE_DAY;
        elapsed = elapsed - (days * MILLISECONDS_IN_ONE_DAY);
        long hours = elapsed / MILLISECONDS_IN_ONE_HOUR;
        elapsed = elapsed - (hours * MILLISECONDS_IN_ONE_HOUR);
        long minutes = elapsed / 60000L;
        elapsed = elapsed - (minutes * 60000L);
        double seconds = elapsed / 1000.0;
        toAppendTo.append(signPrefix);
        if (days != 0 || this.showZeroDays) {
            toAppendTo.append(this.dayFormatter.format(days) + getDaySuffix());
        }
        if (hours != 0 || this.showZeroHours) {
            toAppendTo.append(this.hourFormatter.format(hours)
                    + getHourSuffix());
        }
        toAppendTo.append(this.minuteFormatter.format(minutes)
                + getMinuteSuffix());
        toAppendTo.append(this.secondFormatter.format(seconds)
                + getSecondSuffix());
        return toAppendTo;
    }
    /**
     * Parses the given string (not implemented).
     *
     * @param source  the date string.
     * @param pos  the parse position.
     *
     * @return <code>null</code>, as this method has not been implemented.
     */
    public Date parse(String source, ParsePosition pos) {
        return null;
    }
    /**
     * Tests this formatter for equality with an arbitrary object.
     *
     * @param obj  the object (<code>null</code> permitted).
     *
     * @return A boolean.
     */
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (!(obj instanceof RelativeDateFormat)) {
            return false;
        }
        if (!super.equals(obj)) {
            return false;
        }
        RelativeDateFormat that = (RelativeDateFormat) obj;
        if (this.baseMillis != that.baseMillis) {
            return false;
        }
        if (this.showZeroDays != that.showZeroDays) {
            return false;
        }
        if (this.showZeroHours != that.showZeroHours) {
            return false;
        }
        if (!this.positivePrefix.equals(that.positivePrefix)) {
            return false;
        }
        if (!this.daySuffix.equals(that.daySuffix)) {
            return false;
        }
        if (!this.hourSuffix.equals(that.hourSuffix)) {
            return false;
        }
        if (!this.minuteSuffix.equals(that.minuteSuffix)) {
            return false;
        }
        if (!this.secondSuffix.equals(that.secondSuffix)) {
            return false;
        }
        if (!this.dayFormatter.equals(that.dayFormatter)) {
            return false;
        }
        if (!this.hourFormatter.equals(that.hourFormatter)) {
            return false;
        }
        if (!this.minuteFormatter.equals(that.minuteFormatter)) {
            return false;
        }
        if (!this.secondFormatter.equals(that.secondFormatter)) {
            return false;
        }
        return true;
    }
    /**
     * Returns a hash code for this instance.
     *
     * @return A hash code.
     */
    public int hashCode() {
        int result = 193;
        result = 37 * result
                + (int) (this.baseMillis ^ (this.baseMillis >>> 32));
        result = 37 * result + this.positivePrefix.hashCode();
        result = 37 * result + this.daySuffix.hashCode();
        result = 37 * result + this.hourSuffix.hashCode();
        result = 37 * result + this.minuteSuffix.hashCode();
        result = 37 * result + this.secondSuffix.hashCode();
        result = 37 * result + this.secondFormatter.hashCode();
        return result;
    }
    /**
     * Returns a clone of this instance.
     *
     * @return A clone.
     */
    public Object clone() {
        RelativeDateFormat clone = (RelativeDateFormat) super.clone();
        clone.dayFormatter = (NumberFormat) this.dayFormatter.clone();
        clone.secondFormatter = (NumberFormat) this.secondFormatter.clone();
        return clone;
    }
    /**
     * Some test code.
     *
     * @param args  ignored.
     */
    public static void main(String[] args) {
        GregorianCalendar c0 = new GregorianCalendar(2006, 10, 1, 0, 0, 0);
        GregorianCalendar c1 = new GregorianCalendar(2006, 10, 1, 11, 37, 43);
        c1.set(Calendar.MILLISECOND, 123);
        System.out.println("Default: ");
        RelativeDateFormat rdf = new RelativeDateFormat(c0.getTime().getTime());
        System.out.println(rdf.format(c1.getTime()));
        System.out.println();
        System.out.println("Hide milliseconds: ");
        rdf.setSecondFormatter(new DecimalFormat("0"));
        System.out.println(rdf.format(c1.getTime()));
        System.out.println();
        System.out.println("Show zero day output: ");
        rdf.setShowZeroDays(true);
        System.out.println(rdf.format(c1.getTime()));
        System.out.println();
        System.out.println("Alternative suffixes: ");
        rdf.setShowZeroDays(false);
        rdf.setDaySuffix(":");
        rdf.setHourSuffix(":");
        rdf.setMinuteSuffix(":");
        rdf.setSecondSuffix("");
        System.out.println(rdf.format(c1.getTime()));
        System.out.println();
    }
}
```

| 2.41.1. | Date Parsing and Formatting with DateFormat |
|---|---|
| 2.41.2. | Parsing the Time Using a Custom Format |
| 2.41.3. | Parse with a custom format |
| 2.41.4. | Parse with a default format |
| 2.41.5. | Parse string date value input with SimpleDateFormat('dd-MMM-yy') |
| 2.41.6. | Parse a date and time |
| 2.41.7. | Parse string date value input with SimpleDateFormat('E, dd MMM yyyy HH:mm:ss Z') |
| 2.41.8. | Parse string date value with default format: DateFormat.getDateInstance(DateFormat.DEFAULT) |
| 2.41.9. | Leniency |
| 2.41.10. | Formatting String Symbols for SimpleDateFormat |
| 2.41.11. | SimpleDateFormat: hh:mm:ss, dd MMM yyyy hh:mm:ss zzz, E MMM dd yyyy |
| 2.41.12. | Simply format a date as YYYYMMDD |
| 2.41.13. | Express a duration in term of HH:MM:SS |
| 2.41.14. | Date Format with SimpleDateFormat |
| 2.41.15. | Demonstrate date formats with different DateFormat constants |
| 2.41.16. | Demonstrate time formats. |
| 2.41.17. | DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM) |
| 2.41.18. | print out the current date and time |
| 2.41.19. | Date Era change |
| 2.41.20. | Format Date with System.out.format |
| 2.41.21. | SimpleDateFormat |
| 2.41.22. | Formatting Dates and Times |
| 2.41.23. | Four different date formats for four countries: US, UK, GERMANY, FRANCE |
| 2.41.24. | Various Date format |
| 2.41.25. | Display date with day name in a short format |
| 2.41.26. | Display date with a short day and month name |
| 2.41.27. | Format a date into dd/mm/yyyy |
| 2.41.28. | Format current date and time with the SimpleDateFormat: dd/MM/yyyy |
| 2.41.29. | Format current date and time with the SimpleDateFormat: HH:mm:ss |
| 2.41.30. | Formatting Symbols for SimpleDateFormat |
| 2.41.31. | Formatting the Time Using a Custom Format |
| 2.41.32. | Change date formatting symbols |
| 2.41.33. | Get a List of Short Month Names |
| 2.41.34. | Get a List of Weekday Names |
| 2.41.35. | Get a List of Short Weekday Names |
| 2.41.36. | Time in 12-hour format |
| 2.41.37. | Time in 24-hour format |
| 2.41.38. | Date and time with month |
| 2.41.39. | Date and time with day and month fully spelled-out |
| 2.41.40. | Output current time: %tc |
| 2.41.41. | Formatter that caches formatted date information |
| 2.41.42. | RFC date format |
| 2.41.43. | A formatter that formats dates to show the elapsed time relative to some base date. |
