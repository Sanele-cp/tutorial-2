from numpy.fft import fft,ifft
import numpy as np
import pylab as pl

def myconv(f,g):
	ft1=fft(f)
	ft2=fft(g)
	
	return np.real(ifft(ft1*ft2))
	

def myshift(x,n=0):
	vec=np.zeros(len(x))
	vec[n]=1
	xft1=myconv(x,vec)
	return xft1

def mygauss(x):
	y=np.exp(-0.5*x**2/2**2)
	return y


if __name__=='__main__':

	x=np.arange(-10,10,0.1)
	y=mygauss(x)



	yshift=myshift(y,100)
	pl.plot(x,y)
	pl.savefig("plot0.pdf")
	pl.plot(x,yshift)
	pl.savefig("plot.pdf")
	pl.show()
		

	ycorr=myconv(y,np.conj(y)) 
	pl.plot(x,ycorr)
	pl.savefig("plot1.pdf")
	pl.show()


	kshift=[5,10,100]
	for k in kshift:
		ycorr=myconv(y,np.conj(y))
		yshift=myshift(y,k)
		S=myconv(yshift,np.conj(yshift))
    

		pl.plot(x,ycorr)
		pl.plot(x,S,'r')
		pl.savefig("plot2.pdf")
		pl.show()
