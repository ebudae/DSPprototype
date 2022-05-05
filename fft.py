pi = 3.14159265358979323846
i = 0+1j

# Moves all even indices to 1st half odd indices to 2nd half of inputs. 
# inputs : an array of complex numbers N : length of inputs array

def split( inputs, N ):
	inputs = inputs[::2]+inputs[1::2]

# This function computes the fast fourier transform of a list of complex numbers 
# of length N.
# x : input array of complex number that represent a sampled function amplitude 
# N : the length of x must be a power of 2 

def fast_fourier( x, N ):

	# base of recursion
	if N == 1 :
		return
	
	# no rounding needed if N is base 2
	n = N//2

	# set primitive root of unity 
	wn = complex( exp((2*pi*i)/N) )
	w = 1 + 0j 

	# move odd and even index to each half of array x
	split(x, 2*n)
	
	# even and odd
	fast_fourier(x, n)
	# pass pointer starting at the n/2th element
	fast_fourier(x+n, n)

	even = 0 + 0j
	odd = 0 + 0j

	for k in range(n):
		even = x[k]
		odd = x[k+n]

		x[k] = even + w*odd
		x[k+n] = even - w*odd

		w = w*wn

def ifft( x, N):

	# base of recursion
	if N == 1 :
		return
	
	# no rounding needed if N is base 2
	n = N//2

	# set primitive root of unity 
	wn = complex( exp((-2*pi*i)/N)/N )
	w = 1 + 0j 

	# move odd and even index to each half of array x
	split(x, 2*n)
	
	# even and odd
	fast_fourier(x, n)
	# pass pointer starting at the n/2th element
	fast_fourier(x+n, n)

	even = 0 + 0j
	odd = 0 + 0j

	for k in range(n):
		even = x[k]
		odd = x[k+n]

		x[k] = even + w*odd
		x[k+n] = even - w*odd

		w = w*wn

def magnitude( p, N) :
	return 2*sqrt(pow(p.real(),2) + pow(p.imag(),2))/N

def approx_zero( b ):
	if  abs( b ) < 0.0000000000001:	
		return 0
	return b


# Default behavior prints the contents of a list. When extras == TRUE,
#   computes the magnitude and phase of complex inputs and displays
def printlist( l, N, extras):
	
	print( ' '.join( l ) )

	mag = 0.0
	phase = 0.0 

	if extras :
		for i in range(N): 
			mag = magnitude(l[i],N);
			phase = atan(l[i].imag()/l[i].real());

			print( "Frequency bin ["+ str( i ) + "]" )
			print( "Magnitude: " + str( mag ) )
			print( "Phase: " + str( phase ) )
		
