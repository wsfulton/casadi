#! Linear solvers
#! =================
#!
#! We demonstrate solving a dense system A.x=b by using different linear solvers.
#!
from casadi import *
import casadi as c
from numpy import *
import time

n=100
#$ We generate $A \in \mathbf{R}^{n \times n}$, $x \in \mathbf{R}^{n}$ with $n=100$
A=DMatrix([[cos(i*j)-sin(i) for i in range(n)] for j in range(n)])
x=DMatrix([tan(i) for i in range(n)])

#! We generate the b vector:
b=c.dot(A,x)

#! We demonstrate the LinearSolver API with SuperLU:
s = SuperLU(A.sparsity())
s.init()

#! Give it the matrix A
s.input(0).set(A)
#! Do the LU factorization
s.prepare()

#! Give it the matrix b
s.input(1).set(b)

#! And we are off to find x...
s.solve()

x_ = s.output()

#! By looking at the residuals between the x we knew in advance and the computed x, we see that the SuperLU solver works
print "Sum of residuals = %.2e" % sum_all(fabs(x-x_))

#! Comparison of different linear solvers
#! ======================================
for name, solver in [("SuperLU",SuperLU),("LapackLUDense",LapackLUDense),("LapackQRDense",LapackQRDense),("CSparse",CSparse)]:
  s = solver(A.sparsity()) # We create a solver
  s.init()

  s.input(0).set(A) # Give it the matrix A
  
  t0 = time.time()
  for i in range(100):
    s.prepare()        # Do the LU factorization
  pt = (time.time()-t0)/100

  s.input(1).set(b)  # Give it the matrix b

  t0 = time.time()
  for i in range(100):
    s.solve()
  st = (time.time()-t0)/100
  
  x_ = s.output()

  print ""
  print name
  print "=" * 10
  print "Sum of residuals = %.2e" % sum_all(fabs(x-x_))
  print "Preparation time = %0.2f ms" % (pt*1000)
  print "Solve time       = %0.2f ms" % (st*1000)
  assert(sum_all(fabs(x-x_))<1e-9)
  
#! Note that these 
