#
# A class representing a piecewise linear function
#
# --------------------------------------------------------------------

class PieceWiseLinear(object):
  """A piecewise linear function"""
  def __init__(self, x0, y0, x1, y1):
    if x1 <= x0:
      raise ValueError("x1 must be larger than x0")
    self.points = [(x0, y0), (x1, y1)]

  def domain(self):
    """Return domain interval as a pair."""
    return (self.points[0][0], self.points[-1][0])
                          
  def __str__(self):
    ret = ""
    for i in self.points :
        ret += "(%g,%g)" %(i[0], i[1])
        if not i == self.points[-1] :
            ret += ".."
    return ret

  def __call__(self, x):
    """Evaluate this function at x-coordinate x."""
    d = self.domain()
    if x < d[0] or x > d[-1]:
      raise ValueError("argument is not in domain")
    for i in range(len(self.points)-1) :
        if x >= self.points[i][0] and x <= self.points[i+1][0] :
            a = (x - self.points[i][0]) / (self.points[i+1][0] - self.points[i][0])
            b = (self.points[i+1][0] - x) / (self.points[i+1][0] - self.points[i][0])
            return  self.points[i][1] * b + self.points[i+1][1] * a

  def join(self, rhs):
    """Join two piecewise linear functions."""
    d1 = self.domain()
    d2 = rhs.domain()
    if d1[-1] != d2[0]:
      raise ValueError("domains are not contiguous")
    if abs(self(d1[-1]) - rhs(d2[0])) > 1e-13:
      raise ValueError("discontinuity at connection point")
    ret = PieceWiseLinear(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1])
    ret.points[:] = []
    for i in self.points :
        ret.points.append(i)
    for i in rhs.points :
        if i == rhs.points[0] :
            continue
        ret.points.append(i)
    return ret

  def __rmul__(self, lhs):
    """Multiplication of a number lhs with a piecewise linear function.
Returns a new function, this function remains unchanged."""
    ret = PieceWiseLinear(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1])
    ret.points[:] = []
    for i in self.points :
        ret.points.append((i[0], i[1]*lhs))
    return ret

  def add_pwlf(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is another piecewise linear function.
The domain of the result is the intersection of the two domains.
Returns a new function, this function remains unchanged."""
    x0a, x1a = self.domain()
    x0b, x1b = rhs.domain()
    x0 = max(x0a, x0b)
    x1 = min(x1a, x1b)
    if x0 >= x1:
      raise ValueError("domains do not overlap")
    ret = PieceWiseLinear(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1])
    ret.points[:] = []
    ret.points.append((x0, self(x0) + factor * rhs(x0)))
    a, b = 0, 0
    now = x0
    while a<len(self.points)-1 and b<len(rhs.points)-1 :
       while a < len(self.points)-1 and self.points[a][0] <= now:
           a += 1
       while b < len(rhs.points)-1 and rhs.points[b][0] <= now :
           b += 1
       now = min(self.points[a][0], rhs.points[b][0])
       ret.points.append((now, self(now) + factor * rhs(now)))
    
    if ret.points[-1][0] != x1 :
        ret.points.append((x1, self(x1) + factor * rhs(x1)))
    return ret

  def add_number(self, rhs, factor):
    """Returns the sum of this function and factor * rhs,
where rhs is a number.
This function remains unchanged."""
    ret = PieceWiseLinear(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1])
    ret.points[:] = []
    for i in self.points :
        ret.points.append((i[0], i[1] + factor * rhs))
    return ret

  def __add__(self, rhs):
    """Addition of a piecewise linear function with a number or 
with another piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, +1)
    else:
      return self.add_number(rhs, +1)

  def __sub__(self, rhs):
    """Subtraction of a number or of another piecewise linear function
from this piecewise linear function.
Returns a new function, this function remains unchanged."""
    if isinstance(rhs, PieceWiseLinear):
      return self.add_pwlf(rhs, -1)
    else:
      return self.add_number(rhs, -1)
  
# --------------------------------------------------------------------

if __name__ == "__main__":
  f1 = PieceWiseLinear(1, -1, 3, 1)
  f2 = PieceWiseLinear(3, 1, 7, -5)
  print("f1 = %s" % f1)
  print("f2 = %s" % f2)  
  for x in [1, 2, 3]:
    print("f1(%g) = %g" % (x, f1(x)))
  for x in [3, 5, 7]:
    print("f2(%g) = %g" % (x, f2(x)))
  f = f1.join(f2)
  print("f = %s" % f)  
  for x in [1, 2, 3, 5, 7]:
    print("f(%g) = %g" % (x, f(x)))
  print("Domain of f1 = %s, domain of f2 = %s, domain of f = %s" %
        (f1.domain(), f2.domain(), f.domain()))
  g1 = f + 2
  print("g1 = f + 2 = %s" % g1)
  g2 = f - 6
  print("g2 = f - 6 = %s" % g2)
  g3 = 3 * f
  print("g3 = 3 * f = %s" % g3)
  h1 = 5 * f + 3
  h2 = 0.5 * f - 2
  print("h1 = 5 * f + 3 = %s" % h1)
  print("h2 = 0.5 * f - 2 = %s" % h2)
  g = h1 + h2
  print("g = h1 + h2 = %s" % g)
  d1 = PieceWiseLinear(0, 0, 2, 19)
  d = d1.join(PieceWiseLinear(2, 19, 6, 12))
  print("d = %s" % d)
  e1 = g + d
  e2 = g - d
  print("e1 = g + d = %s" % e1)
  print("e2 = g - d = %s" % e2)  
  for x in [1, 2, 3, 4, 5, 6]:
    print("g(%g) = %g, d(%g) = %g, e1(%g) = %g, e2(%g) = %g" %
          (x, g(x), x, d(x), x, e1(x), x, e2(x)))

# --------------------------------------------------------------------
