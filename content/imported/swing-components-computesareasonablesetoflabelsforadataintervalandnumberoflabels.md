---
title: Computes a reasonable set of labels for a data interval and number of labels.
nav: Computes a reasonable set ...
description: Computes a reasonable set of labels for a data interval and number of labels.
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20111125074732/http://java2s.com/Code/Java/Swing-Components/Computesareasonablesetoflabelsforadataintervalandnumberoflabels.htm
---
Computes a reasonable set of labels for a data interval and number of labels.

```java title=Example.java
/**
 * Copyright (C) 2009, 2010 SC 4ViewSoft SRL
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//package org.achartengine.util;
import java.text.NumberFormat;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;
public class Util {
    /** A value that is used a null value. */
    public static final double NULL_VALUE = Double.MAX_VALUE;
    /**
     * A number formatter to be used to make sure we have a maximum number of
     * fraction digits in the labels.
     */
    private static final NumberFormat FORMAT = NumberFormat.getNumberInstance();
    /**
     * Computes a reasonable set of labels for a data interval and number of
     * labels.
     *
     * @param start start value
     * @param end final value
     * @param approxNumLabels desired number of labels
     * @return collection containing {start value, end value, increment}
     */
    public static List<Double> getLabels(final double start, final double end,
        final int approxNumLabels) {
      FORMAT.setMaximumFractionDigits(5);
      List<Double> labels = new ArrayList<Double>();
      double[] labelParams = computeLabels(start, end, approxNumLabels);
      // when the start > end the inc will be negative so it will still work
      int numLabels = 1 + (int) ((labelParams[1] - labelParams[0]) / labelParams[2]);
      // we want the range to be inclusive but we don't want to blow up when
      // looping for the case where the min and max are the same. So we loop
      // on
      // numLabels not on the values.
      for (int i = 0; i < numLabels; i++) {
        double z = labelParams[0] + i * labelParams[2];
        try {
          // this way, we avoid a label value like 0.4000000000000000001 instead
          // of 0.4
          z = FORMAT.parse(FORMAT.format(z)).doubleValue();
        } catch (ParseException e) {
          // do nothing here
        }
        labels.add(z);
      }
      return labels;
    }
    /**
     * Computes a reasonable number of labels for a data range.
     *
     * @param start start value
     * @param end final value
     * @param approxNumLabels desired number of labels
     * @return double[] array containing {start value, end value, increment}
     */
    private static double[] computeLabels(final double start, final double end,
        final int approxNumLabels) {
      if (Math.abs(start - end) < 0.0000001f) {
        return new double[] { start, start, 0 };
      }
      double s = start;
      double e = end;
      boolean switched = false;
      if (s > e) {
        switched = true;
        double tmp = s;
        s = e;
        e = tmp;
      }
      double xStep = roundUp(Math.abs(s - e) / approxNumLabels);
      // Compute x starting point so it is a multiple of xStep.
      double xStart = xStep * Math.ceil(s / xStep);
      double xEnd = xStep * Math.floor(e / xStep);
      if (switched) {
        return new double[] { xEnd, xStart, -1.0 * xStep };
      }
      return new double[] { xStart, xEnd, xStep };
    }
    /**
     * Given a number, round up to the nearest power of ten times 1, 2, or 5. The
     * argument must be strictly positive.
     */
    private static double roundUp(final double val) {
      int exponent = (int) Math.floor(Math.log10(val));
      double rval = val * Math.pow(10, -exponent);
      if (rval > 5.0) {
        rval = 10.0;
      } else if (rval > 2.0) {
        rval = 5.0;
      } else if (rval > 1.0) {
        rval = 2.0;
      }
      rval *= Math.pow(10, exponent);
      return rval;
    }
}
```

1.  MultiLine Label
---  ---
2.  Multi Line Label extends JComponent
3.  Multi Line Label extends JPanel
4.  Link Label
5.  Vertical Label UI
6.  Label with large font and ANTIALIAS paint
7.  Label 3D
8.  URL Label
9.  Hyperlink Label
10.  Bevel Text
11.  A JLabel that can be underlined, implements Scrollable
12.  Gradient Label
13.  Hyperlink Label 2
14.  Multi-label Label
15.  Shadow Label
16.  Button Label
