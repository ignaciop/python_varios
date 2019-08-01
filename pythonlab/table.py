import vpython as vp

tablex = 2.5
tabley = -2
tablez = -1
tableLength = 10
tableWidth = 5.5
tableHeight = 0.5
tableColor = vp.color.orange
legRadius = 0.5

vp.scene.background = vp.vector(0.6, 0.6, 0.6)
vp.scene.range = 5

# Create a table out of a box and four cylinders

tabletop = vp.box(pos = vp.vector(tablex, tabley, tablez),
                    color = tableColor, length = tableLength,
                        width = tableWidth, height = tableHeight)
tablebottom = tabletop.clone(pos = vp.vector(tablex, 2*tabley, tablez))

leg1 = vp.cylinder(pos = tabletop.pos - vp.vector(tableLength/2 - tableHeight, tableWidth/2 - tableHeight, tableLength/4.5),
                    radius = legRadius, 
                        axis = vp.vector(0, -tablebottom.pos.y/2, 0),
                            color = tableColor)
leg2 = leg1.clone(pos = tabletop.pos - vp.vector(tableLength/2 - tableHeight, tableWidth/2 - tableHeight, -tableLength/4.5),
                    axis = vp.vector(0, -tablebottom.pos.y/2, 0))
leg3 = leg1.clone(pos = tabletop.pos + vp.vector(tableLength/2 - tableHeight, -tableWidth/2 + 5*tableHeight, tableLength/4.5),
                    axis = vp.vector(0, tablebottom.pos.y/2, 0))
leg4 = leg1.clone(pos = tabletop.pos + vp.vector(tableLength/2 - tableHeight, -tableWidth/2 + 5*tableHeight, -tableLength/4.5),
                    axis = vp.vector(0, tablebottom.pos.y/2, 0))