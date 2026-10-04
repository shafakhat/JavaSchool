---
title: A class representing a cubic path segment
nav: A class representing a cub...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20100206135209/http://java2s.com/Code/Java/2D-Graphics-GUI/Aclassrepresentingacubicpathsegment.htm
---
```java title=Example.java
/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */
import java.awt.geom.CubicCurve2D;
import java.awt.geom.Point2D;
import java.awt.geom.QuadCurve2D;
import java.awt.geom.Rectangle2D;
import java.util.Arrays;
/**
 *
 * @version $Id: Cubic.java 478249 2006-11-22 17:29:37Z dvholten $
 */
public class Cubic extends AbstractSegment {
    public Point2D.Double p1, p2, p3, p4;
    public Cubic() {
        p1 = new Point2D.Double();
        p2 = new Point2D.Double();
        p3 = new Point2D.Double();
        p4 = new Point2D.Double();
    }
    public Cubic(double x1, double y1,  double x2, double y2,
                 double x3, double y3,  double x4, double y4) {
        p1 = new Point2D.Double(x1, y1);
        p2 = new Point2D.Double(x2, y2);
        p3 = new Point2D.Double(x3, y3);
        p4 = new Point2D.Double(x4, y4);
    }
    public Cubic(Point2D.Double p1, Point2D.Double p2,
                 Point2D.Double p3, Point2D.Double p4) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
        this.p4 = p4;
    }
    public Object clone() {
        return new Cubic(new Point2D.Double(p1.x, p1.y),
                         new Point2D.Double(p2.x, p2.y),
                         new Point2D.Double(p3.x, p3.y),
                         new Point2D.Double(p4.x, p4.y));
    }
    public Segment reverse() {
        return new Cubic(new Point2D.Double(p4.x, p4.y),
                         new Point2D.Double(p3.x, p3.y),
                         new Point2D.Double(p2.x, p2.y),
                         new Point2D.Double(p1.x, p1.y));
    }
    private void getMinMax(double p1, double p2,
                           double p3, double p4,
                           double [] minMax) {
        if (p4 > p1){
            minMax[0] = p1; minMax[1] = p4;
        } else {
            minMax[0] = p4; minMax[1] = p1;
        }
        double c0 = 3*(p2-p1);
        double c1 = 6*(p3-p2);
        double c2 = 3*(p4-p3);
        double [] eqn = { c0, c1-2*c0, c2-c1+c0 };
        int roots = QuadCurve2D.solveQuadratic(eqn);
        for (int r=0; r<roots; r++) {
            double tv = eqn[r];
            if ((tv <= 0) || (tv >= 1)) continue;
            tv = ((1-tv)*(1-tv)*(1-tv)*p1 +
                    3*tv*(1-tv)*(1-tv)*p2 +
                    3*tv*tv*(1-tv)*p3 +
                    tv*tv*tv*p4);
            if      (tv < minMax[0]) minMax[0] = tv;
            else if (tv > minMax[1]) minMax[1] = tv;
        }
    }
    public double minX() {
        double [] minMax = {0, 0};
        getMinMax(p1.x, p2.x, p3.x, p4.x, minMax);
        return minMax[0];
    }
    public double maxX() {
        double [] minMax = {0, 0};
        getMinMax(p1.x, p2.x, p3.x, p4.x, minMax);
        return minMax[1];
    }
    public double minY() {
        double [] minMax = {0, 0};
        getMinMax(p1.y, p2.y, p3.y, p4.y, minMax);
        return minMax[0];
    }
    public double maxY() {
        double [] minMax = {0, 0};
        getMinMax(p1.y, p2.y, p3.y, p4.y, minMax);
        return minMax[1];
    }
    public Rectangle2D getBounds2D() {
        double [] minMaxX = {0, 0};
        getMinMax(p1.x, p2.x, p3.x, p4.x, minMaxX);
        double [] minMaxY = {0, 0};
        getMinMax(p1.y, p2.y, p3.y, p4.y, minMaxY);
        return new Rectangle2D.Double
            (minMaxX[0], minMaxY[0],
             minMaxX[1]-minMaxX[0], minMaxY[1]-minMaxY[0]);
    }
    protected int findRoots(double y, double [] roots) {
        double [] eqn = { p1.y-y, 3*(p2.y-p1.y), 3*(p1.y-2*p2.y+p3.y),
                          3*p2.y-p1.y+p4.y-3*p3.y };
        return CubicCurve2D.solveCubic(eqn, roots);
        // return solveCubic(eqn[3], eqn[2], eqn[1], eqn[0], roots);
    }
    public Point2D.Double evalDt(double t) {
        double x = 3*(  (p2.x-p1.x)*(1-t)*(1-t) +
                      2*(p3.x-p2.x)*(1-t)*t +
                        (p4.x-p3.x)*t*t);
        double y = 3*(  (p2.y-p1.y)*(1-t)*(1-t) +
                      2*(p3.y-p2.y)*(1-t)*t +
                        (p4.y-p3.y)*t*t);
        return new Point2D.Double(x, y);
    }
    public Point2D.Double eval(double t) {
        double x = ((1-t)*(1-t)*(1-t)*p1.x +
                    3*(t* (1-t)*(1-t)*p2.x +
                       t* t*    (1-t)*p3.x) +
                    t*t*t            *p4.x);
        double y = ((1-t)*(1-t)*(1-t)*p1.y +
                    3*(t* (1-t)*(1-t)*p2.y +
                       t* t*    (1-t)*p3.y) +
                    t*t*t            *p4.y);
        return new Point2D.Double(x, y);
    }
    /**
     * Subdivides this Cubic curve into two curves at t = 0.5.
     * can be done with getSegment but this is more efficent.
     * @param s0 if non-null contains portion of curve from  0->.5
     * @param s1 if non-null contains portion of curve from .5->1
     */
    public void subdivide(Segment s0, Segment s1) {
        Cubic c0=null, c1=null;
        if (s0 instanceof Cubic) c0 = (Cubic)s0;
        if (s1 instanceof Cubic) c1 = (Cubic)s1;
        subdivide(c0, c1);
    }
    /**
     * Subdivides this Cubic curve into two curves at given t.
     * @param s0 if non-null contains portion of curve from 0->t.
     * @param s1 if non-null contains portion of curve from t->1.
     */
    public void subdivide(double t, Segment s0, Segment s1) {
        Cubic c0=null, c1=null;
        if (s0 instanceof Cubic) c0 = (Cubic)s0;
        if (s1 instanceof Cubic) c1 = (Cubic)s1;
        subdivide(t, c0, c1);
    }
    /**
     * Subdivides this Cubic curve into two curves at t = 0.5.
     * can be done with getSegment but this is more efficent.
     * @param c0 if non-null contains portion of curve from  0->.5
     * @param c1 if non-null contains portion of curve from .5->1
     */
    public void subdivide(Cubic c0, Cubic c1) {
        if ((c0 == null) && (c1 == null)) return;
        double npX = (p1.x+3*(p2.x+p3.x)+p4.x)*0.125;
        double npY = (p1.y+3*(p2.y+p3.y)+p4.y)*0.125;
        double npdx = ((p2.x-p1.x)+2*(p3.x-p2.x)+(p4.x-p3.x))*0.125;
        double npdy = ((p2.y-p1.y)+2*(p3.y-p2.y)+(p4.y-p3.y))*0.125;
        if (c0 != null) {
            c0.p1.x = p1.x;
            c0.p1.y = p1.y;
            c0.p2.x = (p2.x+p1.x)*0.5;
            c0.p2.y = (p2.y+p1.y)*0.5;
            c0.p3.x = npX-npdx;
            c0.p3.y = npY-npdy;
            c0.p4.x = npX;
            c0.p4.y = npY;
        }
        if (c1 != null) {
            c1.p1.x = npX;
            c1.p1.y = npY;
            c1.p2.x = npX+npdx;
            c1.p2.y = npY+npdy;
            c1.p3.x = (p4.x+p3.x)*0.5;
            c1.p3.y = (p4.y+p3.y)*0.5;
            c1.p4.x = p4.x;
            c1.p4.y = p4.y;
        }
    }
    /**
     * Subdivides this Cubic curve into two curves at given t.
     * @param c0 if non-null contains portion of curve from 0->t.
     * @param c1 if non-null contains portion of curve from t->1.
     */
    public void subdivide(double t, Cubic c0, Cubic c1) {
        if ((c0 == null) && (c1 == null)) return;
        Point2D.Double np = eval(t);
        Point2D.Double npd = evalDt(t);
        if (c0 != null) {
            c0.p1.x = p1.x;
            c0.p1.y = p1.y;
            c0.p2.x = (p2.x+p1.x)*t;
            c0.p2.y = (p2.y+p1.y)*t;
            c0.p3.x = np.x-(npd.x*t/3);
            c0.p3.y = np.y-(npd.y*t/3);
            c0.p4.x = np.x;
            c0.p4.y = np.y;
        }
        if (c1 != null) {
            c1.p1.x = np.x;
            c1.p1.y = np.y;
            c1.p2.x = np.x+(npd.x*(1-t)/3);
            c1.p2.y = np.y+(npd.y*(1-t)/3);
            c1.p3.x = (p4.x+p3.x)*(1-t);
            c1.p3.y = (p4.y+p3.y)*(1-t);
            c1.p4.x = p4.x;
            c1.p4.y = p4.y;
        }
    }
    public Segment getSegment(double t0, double t1) {
        double dt = t1-t0;
        Point2D.Double np1 = eval(t0);
        Point2D.Double dp1 = evalDt(t0);
        Point2D.Double np2 = new Point2D.Double(np1.x+dt*dp1.x/3,
                                                np1.y+dt*dp1.y/3);
        Point2D.Double np4 = eval(t1);
        Point2D.Double dp4 = evalDt(t1);
        Point2D.Double np3 = new Point2D.Double(np4.x-dt*dp4.x/3,
                                                np4.y-dt*dp4.y/3);
        return new Cubic(np1, np2, np3, np4);
    }
    private static int count = 0;
    protected double subLength(double leftLegLen, double rightLegLen,
                               double maxErr) {
        count++;
        double cldx, cldy, cdx, cdy;
        cldx = p3.x-p2.x;
        cldy = p3.y-p2.y;
        double crossLegLen = Math.sqrt(cldx*cldx+cldy*cldy);
        cdx = p4.x-p1.x;
        cdy = p4.y-p1.y;
        double cordLen = Math.sqrt(cdx*cdx+cdy*cdy);
        double hullLen = leftLegLen+rightLegLen+crossLegLen;
        if (hullLen < maxErr) return (hullLen+cordLen)/2;
        double err = (hullLen-cordLen);
        if (err < maxErr)
            return (hullLen+cordLen)/2;
        Cubic c  = new Cubic();
        double npX = (p1.x+3*(p2.x+p3.x)+p4.x)*0.125;
        double npY = (p1.y+3*(p2.y+p3.y)+p4.y)*0.125;
        double npdx = (cldx + cdx)*.125;
        double npdy = (cldy + cdy)*.125;
        c.p1.x = p1.x;
        c.p1.y = p1.y;
        c.p2.x = (p2.x+p1.x)*.5;
        c.p2.y = (p2.y+p1.y)*.5;
        c.p3.x = npX-npdx;
        c.p3.y = npY-npdy;
        c.p4.x = npX;
        c.p4.y = npY;
        double midLen = Math.sqrt(npdx*npdx+npdy*npdy);
        double len = c.subLength(leftLegLen/2, midLen, maxErr/2);
        c.p1.x = npX;
        c.p1.y = npY;
        c.p2.x = npX+npdx;
        c.p2.y = npY+npdy;
        c.p3.x = (p4.x+p3.x)*.5;
        c.p3.y = (p4.y+p3.y)*.5;
        c.p4.x = p4.x;
        c.p4.y = p4.y;
        len += c.subLength(midLen, rightLegLen/2, maxErr/2);
        return len;
    }
    public double getLength() {
        return getLength(0.000001);
    }
    public double getLength(double maxErr) {
        double dx, dy;
        dx = p2.x-p1.x;
        dy = p2.y-p1.y;
        double leftLegLen = Math.sqrt(dx*dx+dy*dy);
        dx = p4.x-p3.x;
        dy = p4.y-p3.y;
        double rightLegLen = Math.sqrt(dx*dx+dy*dy);
        dx = p3.x-p2.x;
        dy = p3.y-p2.y;
        double crossLegLen = Math.sqrt(dx*dx+dy*dy);
        double eps = maxErr*(leftLegLen+rightLegLen+crossLegLen);
        return subLength(leftLegLen, rightLegLen, eps);
    }
    public String toString() {
        return "M" + p1.x + ',' + p1.y +
                'C' + p2.x + ',' + p2.y + ' ' +
                p3.x + ',' + p3.y + ' ' +
                p4.x + ',' + p4.y;
    }
    /*
    public static  boolean epsEq(double a, double b) {
        final double eps = 0.000001;
        return (((a + eps) > b) && ((a-eps) < b));
    }
    public static void sub(Cubic orig, Cubic curr,
                           double t, double inc, int lev) {
        Cubic left=new Cubic();
        Cubic right=new Cubic();
        curr.subdivide(left, right);
        Point2D.Double ptl = left.eval(.5);
        Point2D.Double ptr = right.eval(.5);
        Point2D.Double pt1  = orig.eval(t-inc);
        Point2D.Double pt2  = orig.eval(t+inc);
        int steps = 100;
        Point2D.Double l, r, o;
        for (int i=0; i<=steps; i++) {
            l = left.eval(i/(double)steps);
            o = orig.eval(t-(2*inc)*(1-i/(double)steps));
            if (!epsEq(l.x, o.x) || !epsEq(l.y, o.y))
                System.err.println("Lf Pt: ["  + l.x + "," + l.y +
                                   "] Orig: [" + o.x + "," + o.y +"]");
            r = right.eval(i/(double)steps);
            o = orig.eval(t+(2*inc*i/(double)steps));
            if (!epsEq(r.x, o.x) || !epsEq(r.y, o.y))
                System.err.println("Rt Pt: ["  + r.x + "," + r.y +
                                   "] Orig: [" + o.x + "," + o.y +"]");
        }
        if (lev != 0) {
            sub(orig, left,  t-inc, inc/2, lev-1);
            sub(orig, right, t+inc, inc/2, lev-1);
        }
    }
    public static void evalCubic(Cubic c) {
        int steps = 1000000;
        Point2D.Double oldP = c.eval(0);
        Point2D.Double  newP;
        double len = 0;
        for (int i=1; i<=steps; i++) {
            newP = c.eval(i/(double)steps);
            double dx = newP.x-oldP.x;
            double dy = newP.y-oldP.y;
            len += Math.sqrt(dx*dx + dy*dy);
            oldP = newP;
        }
        System.err.println("Length(.1): " + c.getLength(.001) +
                           " x " + count); count = 0;
        System.err.println("Length    : " + c.getLength() +
                           " x " + count); count = 0;
        System.err.println("D  Len    : " + len);
    }
    public static void main(String args[]) {
        Cubic c;
        c = new Cubic(0,0,  10,10,  20,-10,  30,0);
        sub(c, c, .5, .25, 3);
        evalCubic(c);
        c = new Cubic(0,0,  1,0,  2,-1,  3,0);
        sub(c, c, .5, .25, 3);
        evalCubic(c);
    }
    */
}
/*
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
/**
* An interface that path segments must implement.
*
* @version $Id: Segment.java 478249 2006-11-22 17:29:37Z dvholten $
*/
interface Segment extends Cloneable {
 double minX();
 double maxX();
 double minY();
 double maxY();
 Rectangle2D getBounds2D();
 Point2D.Double evalDt(double t);
 Point2D.Double eval(double t);
 Segment getSegment(double t0, double t1);
 Segment splitBefore(double t);
 Segment splitAfter(double t);
 void    subdivide(Segment s0, Segment s1);
 void    subdivide(double t, Segment s0, Segment s1);
 double  getLength();
 double  getLength(double maxErr);
 SplitResults split(double y);
 class SplitResults {
     Segment [] above;
     Segment [] below;
     SplitResults(Segment []below, Segment []above) {
         this.below = below;
         this.above = above;
     }
     Segment [] getBelow() {
         return below;
     }
     Segment [] getAbove() {
         return above;
     }
 }
}
/*
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
/**
* An abstract class for path segments.
*
* @version $Id: AbstractSegment.java 478249 2006-11-22 17:29:37Z dvholten $
*/
abstract class AbstractSegment implements Segment {
 protected abstract int findRoots(double y, double [] roots);
 public Segment.SplitResults split(double y) {
     double [] roots = { 0, 0, 0 };
     int numSol = findRoots(y, roots);
     if (numSol == 0) return null; // No split
     Arrays.sort(roots, 0, numSol);
     double [] segs = new double[numSol+2];
     int numSegments=0;
     segs[numSegments++] = 0;
     for (int i=0; i<numSol; i++) {
         double r = roots[i];
         if (r <= 0.0) continue;
         if (r >= 1.0) break;
         if (segs[numSegments-1] != r)
             segs[numSegments++] = r;
     }
     segs[numSegments++] = 1.0;
     if (numSegments == 2) return null;
     // System.err.println("Y: " + y + "#Seg: " + numSegments +
     //                    " Seg: " + this);
     Segment [] parts = new Segment[numSegments];
     double pT = 0.0;
     int pIdx = 0;
     boolean firstAbove=false, prevAbove=false;
     for (int i=1; i<numSegments; i++) {
         // System.err.println("Segs: " + segs[i-1]+", "+segs[i]);
         parts[pIdx] = getSegment(segs[i-1], segs[i]);
         Point2D.Double pt = parts[pIdx].eval(0.5);
         // System.err.println("Pt: " + pt);
         if (pIdx == 0) {
             pIdx++;
             firstAbove = prevAbove = (pt.y < y);
             continue;
         }
         boolean above = (pt.y < y);
         if (prevAbove == above) {
             // Merge segments
             parts[pIdx-1] = getSegment(pT, segs[i]);
         } else {
             pIdx++;
             pT=segs[i-1];
             prevAbove = above;
         }
     }
     if (pIdx == 1) return null;
     Segment [] below, above;
     if (firstAbove) {
         above = new Segment[(pIdx+1)/2];
         below = new Segment[pIdx/2];
     } else {
         above = new Segment[pIdx/2];
         below = new Segment[(pIdx+1)/2];
     }
     int ai=0, bi=0;
     for (int i=0; i<pIdx; i++) {
         if (firstAbove) above[ai++] = parts[i];
         else            below[bi++] = parts[i];
         firstAbove = !firstAbove;
     }
     return new SplitResults(below, above);
 }
 public Segment splitBefore(double t) {
     return getSegment(0.0, t);
 }
 public Segment splitAfter(double t) {
     return getSegment(t, 1.0);
 }
 // Doubles have 48bit precision
 static final double eps = 1/(double)(1L<<48);
 static final double tol = 4.0*eps;
 public static int solveLine(double a, double b,
                              double [] roots) {
     if (a == 0) {
         if (b != 0)
             // No intersection.
             return 0;
         // All pts intersect just return 0.
         roots[0] = 0;
         return 1;
     }
     roots[0] = -b/a;
     return 1;
 }
 public static int solveQuad(double a, double b, double c,
                              double [] roots) {
     // System.err.println("Quad: " + a +"t^2 + " + b +"t + " + c);
     if (a == 0) {
         // no square term.
         return solveLine(b, c, roots);
     }
     double det = b*b-4*a*c;
     // System.err.println("Det: " + det);
     if (Math.abs(det) <= tol*b*b) {
         // one real root (det doesn't contain any useful info)
         roots[0] =  -b/(2*a);
         return 1;
     }
     if (det < 0)
         return 0; // No real roots
     // Two real roots
     det = Math.sqrt(det);
     double w = -(b + matchSign(det, b));
     roots[0] = (2*c)/w;
     roots[1] = w/(2*a);
     return 2;
 }
 public static double matchSign(double a, double b) {
     if (b < 0) return (a < 0)?a:-a;
     return (a > 0)?a:-a;
 }
 public static int solveCubic(double a3, double a2,
                               double a1, double a0,
                               double [] roots) {
     // System.err.println("Cubic: " + a3 + "t^3 + " +
     //                    a2 +"t^2 + " +
     //                    a1 +"t + " + a0);
     double [] dRoots = { 0, 0};
     int dCnt = solveQuad(3*a3, 2*a2, a1, dRoots);
     double [] yVals = {0, 0, 0, 0};
     double [] tVals = {0, 0, 0, 0};
     int yCnt=0;
     yVals[yCnt]   = a0;
     tVals[yCnt++] = 0;
     double r;
     switch (dCnt) {
     case 1:
         r = dRoots[0];
         if ((r > 0) && (r < 1)) {
             yVals[yCnt]   = ((a3*r+a2)*r+a1)*r+a0;
             tVals[yCnt++] = r;
         }
         break;
     case 2:
         if (dRoots[0] > dRoots[1]) {
             double t  = dRoots[0];
             dRoots[0] = dRoots[1];
             dRoots[1] = t;
         }
         r = dRoots[0];
         if ((r > 0) && (r < 1)) {
             yVals[yCnt]   = ((a3*r+a2)*r+a1)*r+a0;
             tVals[yCnt++] = r;
         }
         r = dRoots[1];
         if ((r > 0) && (r < 1)) {
             yVals[yCnt]   = ((a3*r+a2)*r+a1)*r+a0;
             tVals[yCnt++] = r;
         }
         break;
     default: break;
     }
     yVals[yCnt]   = a3+a2+a1+a0;
     tVals[yCnt++] = 1.0;
     int ret=0;
     for (int i=0; i<yCnt-1; i++) {
         double y0 = yVals[i],   t0 = tVals[i];
         double y1 = yVals[i+1], t1 = tVals[i+1];
         if ((y0 < 0) && (y1 < 0)) continue;
         if ((y0 > 0) && (y1 > 0)) continue;
         if (y0 > y1) { // swap so y0 < 0 and y1 > 0
             double t;
             t = y0; y0=y1; y1=t;
             t = t0; t0=t1; t1=t;
         }
         if (-y0 < tol*y1) { roots[ret++] = t0;      continue; }
         if (y1 < -tol*y0) { roots[ret++] = t1; i++; continue; }
         double epsZero = tol*(y1-y0);
         int cnt;
         for (cnt=0; cnt<20; cnt++) {
             double dt = t1-t0;
             double dy = y1-y0;
             // double t = (t0+t1)/2;
             // double t= t0+Math.abs(y0/dy)*dt;
             // This tends to make sure that we come up
             // a little short each time this generaly allows
             // you to eliminate as much of the range as possible
             // without overshooting (in which case you may eliminate
             // almost nothing).
             double t= t0+(Math.abs(y0/dy)*99+.5)*dt/100;
             double v = ((a3*t+a2)*t+a1)*t+a0;
             if (Math.abs(v) < epsZero) {
                 roots[ret++] = t; break;
             }
             if (v < 0) { t0 = t; y0=v;}
             else       { t1 = t; y1=v;}
         }
         if (cnt == 20)
             roots[ret++] = (t0+t1)/2;
     }
     return ret;
 }
 /*
 public static void check(Segment seg, float y, PrintStream ps) {
     ps.println("<path fill=\"none\" stroke=\"black\" " +
                " stroke-width=\"3\" d=\"" + seg + "\"/>");
     ps.println("<line x1=\"-1000\" y1=\""+y+
                "\" x2=\"1000\" y2=\""+y+"\" fill=\"none\" stroke=\"orange\"/>\n");
     SplitResults sr = seg.split(y);
     if (sr == null) return;
     Segment [] above = sr.getAbove();
     Segment [] below = sr.getBelow();
     for (int i=0; i<above.length; i++) {
         ps.println("<path fill=\"none\" stroke=\"blue\" " +
                    " stroke-width=\"2.5\" " +
                    " d=\"" + above[i] + "\"/>");
     }
     for (int i=0; i<below.length; i++) {
         ps.println("<path fill=\"none\" stroke=\"red\" " +
                    " stroke-width=\"2\" " +
                    "d=\"" + below[i] + "\"/>");
     }
 }
 public static void main(String [] args) {
     PrintStream ps;
     double [] roots = { 0, 0, 0 };
     int n = solveCubic (-0.10000991821289062, 9.600013732910156,
                         -35.70000457763672, 58.0, roots);
     for (int i=0; i<n; i++)
         System.err.println("Root: " + roots[i]);
     Cubic c;
     c = new Cubic(new Point2D.Double(153.6999969482422,5.099999904632568),
                   new Point2D.Double(156.6999969482422,4.099999904632568),
                   new Point2D.Double(160.39999389648438,2.3999998569488525),
                   new Point2D.Double(164.6999969482422,0.0));
     c.split(0);
     c = new Cubic(new Point2D.Double(24.899999618530273,23.10000228881836),
                   new Point2D.Double(41.5,8.399999618530273),
                   new Point2D.Double(64.69999694824219,1.0),
                   new Point2D.Double(94.5999984741211,1.0));
     c.split(0);
     try {
         ps = new PrintStream(new FileOutputStream(args[0]));
     } catch(java.io.IOException ioe) {
         ioe.printStackTrace();
         return;
     }
     ps.println("<?xml version=\"1.0\" standalone=\"no\"?>\n" +
                "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.0//EN\"\n" +
                "\"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd\">\n" +
                "<svg width=\"450\" height=\"500\"\n" +
                "     viewBox=\"-100 -100 450 500\"\n" +
                "     xmlns=\"http://www.w3.org/2000/svg\"\n" +
                "     xmlns:xlink=\"http://www.w3.org/1999/xlink\">");
     check(new Cubic(new Point2D.Double(0, 0),
                     new Point2D.Double(100, 100),
                     new Point2D.Double(-50, 100),
                     new Point2D.Double(50, 0)), 40, ps);
     check(new Cubic(new Point2D.Double(100, 0),
                     new Point2D.Double(200, 100),
                     new Point2D.Double(50, -50),
                     new Point2D.Double(150, 30)), 20, ps);
     check(new Cubic(new Point2D.Double(200, 0),
                     new Point2D.Double(300, 100),
                     new Point2D.Double(150, 100),
                     new Point2D.Double(250, 0)), 75, ps);
     check(new Quadradic(new Point2D.Double(0, 100),
                         new Point2D.Double(50,150),
                         new Point2D.Double(10,100)), 115, ps);
     check(new Linear(new Point2D.Double(100, 100),
                      new Point2D.Double(150,150)), 115, ps);
     ps.println("</svg>");
 }
 */
}
```

1.  GeneralPath Demo
---  ---
2.  Open GeneralPath Demo
3.  Fill GeneralPath
4.  Yet another GeneralPath demo
5.  Describe a path
6.  GeneralPath
7.  Hypnosis Spiral
8.  A class representing a linear path segment.
9.  A class representing a quadratic path segment
10.  Utilitiy class for length calculations of paths.
11.  A geometric path constructed from straight lines, quadratic and cubic (Bezier) curves and elliptical arc.
