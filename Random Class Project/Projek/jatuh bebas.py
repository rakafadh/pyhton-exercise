
dt = 0.001
g = -10
t0 = 0
h0 = 1000
v0 = 0 
time = [t0]
hdat = [h0]
vdat = [v0]

while h0 > 0:
    v1 = v0 - g*dt
    h1 = h0 - v1*dt
    t1 = t0 + dt
    vdat.append(v1)
    hdat.append(h1)
    time.append(t1)
    v0 = v1
    h0 = h1
    t0 = t1
