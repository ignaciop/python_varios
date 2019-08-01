import vpython as vp

tablex = -5
tabley = 0
tablez = 0
tableLength = 5
tableWidth = 5
tableHeight = 0.5
tableColor = vp.color.orange

# Create a table out of a box and four cylinders

movingBox = vp.box(pos = vp.vector(tablex, tabley, tablez),
                    color = tableColor, length = tableLength,
                        width = tableWidth, height = tableHeight)

# Move a box across the scene in a straight line

while movingBox.pos.x < 5 and movingBox.pos.y < 5:
    vp.rate(20)
    movingBox.pos.x += 0.05
    movingBox.pos.y += 0.05