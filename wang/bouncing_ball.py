import vpython as vp

ball = vp.sphere(pos=vp.vector(0,5,0), radius=1, color=vp.color.yellow)
floor = vp.box(pos=vp.vector(0,-5,0), length=8, height=0.2, width=4);

h = 0.01
v = 0.0

while True:
	vp.rate(400)
	ball.pos.y = ball.pos.y + v*h
	if ball.pos.y > floor.pos.y + ball.radius:
		v = v - 9.8*h
	else:
		v = -v