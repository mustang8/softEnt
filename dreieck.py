from PIL import Image, ImageDraw

class Triangle:
    def __init__(self, pA, pB, pC):
        self.pA = pA
        self.pB = pB
        self.pC = pC

def draw_triangle(draw, triangle):
    draw.line([triangle.pA, triangle.pB], fill="black")
    draw.line([triangle.pB, triangle.pC], fill="black")
    draw.line([triangle.pC, triangle.pA], fill="black")

def draw_sierpinski(draw, triangle, depth):
    if depth == 0:
        draw_triangle(draw,triangle)
        return
    
    midAB = midpoint(triangle.pA, triangle.pB)
    midBC = midpoint(triangle.pB, triangle.pC)
    midCA = midpoint(triangle.pC, triangle.pA)

    draw_sierpinski(draw, Triangle(triangle.pA, midAB, midCA), depth - 1)
    draw_sierpinski(draw, Triangle(midAB, triangle.pB, midBC), depth - 1)
    draw_sierpinski(draw, Triangle(midCA, midBC, triangle.pC), depth - 1)
   
def midpoint(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

if __name__ == "__main__":
    triangle = Triangle((100, 100), (300, 100), (200, 300))
    triangleUp = Triangle((500, 300), (700, 300), (600, 100))

    img_size = 800
    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)
    
    draw_sierpinski(draw, triangle, 0)
    draw_sierpinski(draw, triangleUp, 3)

    img.show()