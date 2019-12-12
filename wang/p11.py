import struct as st
import math

k = float(input('Number: '))

dpack = st.pack('f', k)   # pack float to bytes
dint = st.unpack('i', dpack)[0]   # unpack to int

print('Exponent: ', math.frexp(k)[1])
print('Mantissa: ', math.frexp(k)[0])
print('Mantissa bits: ', bin(dint)[-23:])

