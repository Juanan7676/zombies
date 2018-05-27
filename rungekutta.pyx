from libc.math cimport *

cdef double s(double s, double z, double r, params):
	cdef double p0=params[0],p1=params[1],p2=params[2]
	cdef double s0 = s
	return p0*s0-p1*s0*z-p2*s0

cdef double z(double s, double z, double r, params):
	cdef double p1=params[1],p3=params[3],p4=params[4],p5=params[5]
	cdef double s0 = s, z0 = z
	return p1*s0*z0+p3*r-p4*s0*z0-p5*z0

cdef double r(double s, double z, double r, params):
	cdef double p2=params[2],p4=params[4],p3=params[3],p5=params[5]
	cdef double s0 = s, z0 = z
	return p2*s0+p4*s0*z0-p3*r+p5*z0

def runge_kutta(double s0, double z0, double r0, int tfinal, params):
	# : [ alpha, beta, delta, xi, alpha2, sigma, capacidad ]
	cdef double h = 0.1, k1, k2, k3, k4, l1, l2, l3, l4, m1, m2, m3, m4
	k = 0
	s_sol = [s0]
	z_sol = [z0]
	r_sol = [r0]
	while k*h <= tfinal:
		k1 = h*s(s_sol[k],z_sol[k],r_sol[k], params)
		l1 = h*z(s_sol[k],z_sol[k],r_sol[k], params)
		m1 = h*r(s_sol[k],z_sol[k],r_sol[k], params)

		k2 = h*s(s_sol[k]+k1/2,z_sol[k]+l1/2,r_sol[k]+m1/2, params)
		l2 = h*z(s_sol[k]+k1/2,z_sol[k]+l1/2,r_sol[k]+m1/2, params)
		m2 = h*r(s_sol[k]+k1/2,z_sol[k]+l1/2,r_sol[k]+m1/2, params)


		k3 = h*s(s_sol[k]+k2/2,z_sol[k]+l2/2,r_sol[k]+m2/2, params)
		l3 = h*z(s_sol[k]+k2/2,z_sol[k]+l2/2,r_sol[k]+m2/2, params)
		m3 = h*r(s_sol[k]+k2/2,z_sol[k]+l2/2,r_sol[k]+m2/2, params)

		k4 = h*s(s_sol[k]+k3,z_sol[k]+l3,r_sol[k]+m3, params)
		l4 = h*z(s_sol[k]+k3,z_sol[k]+l3,r_sol[k]+m3, params)
		m4 = h*r(s_sol[k]+k3,z_sol[k]+l3,r_sol[k]+m3, params)

		sn = s_sol[k]+(1/6.0)*(k1+2*k2+2*k3+k4)
		zn = z_sol[k]+(1/6.0)*(l1+2*l2+2*l3+l4)
		rn = r_sol[k]+(1/6.0)*(m1+2*m2+2*m3+m4)

		if (sn < 0): sn = 0
		if (zn < 0): zn = 0
		if (rn < 0): rn = 0
		s_sol.append(sn)
		z_sol.append(zn)
		r_sol.append(rn)

		k += 1
	
	return (s_sol,z_sol,r_sol)
