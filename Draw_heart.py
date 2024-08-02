import turtle as t
import math

def heartX(k):
    return 15*math.sin(k)**3

def heartY(k):
    return 12*math.cos(k) - 5 * \
      math.cos(2 * k) - 2 * \
      math.cos(3 * k) - math.cos(4 * k)

def draw_heart():
    t.speed(0)
    t.bgcolor("black")
    t.color("red")
    for i in range(60000):
        t.goto(heartX(i) * 20 , heartY(i) * 20)
        t.goto(0, 0)
    t.done()

if __name__ == "__main__":
  draw_heart()