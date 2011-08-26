import sys
from OpenGL.GL import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *

class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.points = [((0.0),(0.0)),]



    def initializeGL(self):
        # Add OpenGL initialization code here
        glEnable(GL_POINT_SMOOTH)

    def paintGL(self):
        # Update the scene here

        # Clear the screen
        glClearColor(0.8, 0.5, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the scene here
        self.draw(self.points)

        # Tell the widget to redraw next time
        self.update()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)

    def mouseMoveEvent(self, event):
        self.points.append((2 * event.posF().x() / self.width() -1, 2 * event.posF().y() / self.height() -1))

    def draw(self, points):
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glColor3f(0.0, 0.0, 0.0)
        # print posX, posY
        for point in points:
            glVertex2f(point[0], point[1])
        glEnd()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = GLWidget()
    w.resize(512, 512)
    w.show()
    a.exec_()
