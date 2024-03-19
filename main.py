from browser import document, html, window, alert
import random

def sketch(p): # p is needed because it will be the the processing sketch itself to do things like background, colour, etc.
    #background(0) instead of p.background(0)
  def setup():
    p.createCanvas(700,410)
    p.background(255)
    p.rectMode(p.CENTER)

  def draw():
    colorlist =['pink','orange','yellow']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX,p.mouseY,50,50) #could be lines,rectanges,triangles. #50.50, height and width of ellipse

  def mousePressed(self):
    p.background(0)
  def keyPressed(self):
    if p.key==" ":
      print("ALOHA! :)")

  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed

myp5 = window.p5.new(sketch)