import struct as st
import math

dpack = st.pack('d', 10.0)   # pack float to bytes
dint = st.unpack('q', dpack)[0]   # unpack to int
print(bin(dint)[-23:]) # mantissa bits
print(math.frexp(10.0))

dpack = st.pack('d', 1.0)   # pack float to bytes
dint = st.unpack('q', dpack)[0]   # unpack to int
print(bin(dint)[-23:]) # mantissa bits
print(math.frexp(1.0))

dpack = st.pack('d', 0.1)   # pack float to bytes
dint = st.unpack('q', dpack)[0]   # unpack to int
print(bin(dint)[-23:]) # mantissa bits
print(math.frexp(0.1))

dpack = st.pack('d', 6e-8)   # pack float to bytes
dint = st.unpack('q', dpack)[0]   # unpack to int
print(bin(dint)[-23:]) # mantissa bits
print(math.frexp(6e-8))