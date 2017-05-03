import SimpleCV as scv
i = scv.Image("lena.jpeg")
# i.listHaarFeatures()
faces = i.findHaarFeatures("face.xml")

#print locations
for f in faces:
  print "I found a face at " + str(f.coordinates())

green = (0, 255, 0)
#outline who was drinking last night (or at least has the greenest pallor)
faces.sortColorDistance(green)[0].draw(green)
i.save("greenest_face_detected.png")
