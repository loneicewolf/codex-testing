import sys

from PyQt5.QtCore import Qt, QPointF, QLineF
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem,
    QGraphicsItem, QGraphicsTextItem, QGraphicsProxyWidget,
    QComboBox, QLabel
)


class SocketItem(QGraphicsEllipseItem):
    """Represents an input or output socket on a node."""

    def __init__(self, parent, is_output):
        super().__init__(-5, -5, 10, 10, parent)
        self.setBrush(QColor('red') if is_output else QColor('blue'))
        self.is_output = is_output
        self.parent_node = parent
        self.setFlag(QGraphicsEllipseItem.ItemSendsScenePositionChanges)


class NodeEdge(QGraphicsLineItem):
    """Simple line connecting two sockets."""

    def __init__(self, start_socket, end_socket):
        super().__init__()
        self.start_socket = start_socket
        self.end_socket = end_socket
        self.setPen(QPen(Qt.white, 2))
        self.update_positions()

    def update_positions(self):
        p1 = self.start_socket.scenePos()
        p2 = self.end_socket.scenePos()
        self.setLine(QLineF(p1, p2))


class OptionNode(QGraphicsRectItem):
    """Node with a combo box to pick an option."""

    def __init__(self, title, options):
        super().__init__(0, 0, 120, 80)
        self.setBrush(QColor(60, 60, 60))
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemSendsScenePositionChanges)

        self.title = QGraphicsTextItem(title, self)
        self.title.setDefaultTextColor(Qt.white)
        self.title.setPos(5, 0)

        self.combo = QComboBox()
        for opt in options:
            self.combo.addItem(opt)
        self.proxy = QGraphicsProxyWidget(self)
        self.proxy.setWidget(self.combo)
        self.proxy.setPos(5, 25)

        self.out_socket = SocketItem(self, True)
        self.out_socket.setPos(self.rect().right(), self.rect().center().y())
        self.edges = []

    def output_anchor(self):
        return self.out_socket.scenePos()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.edges:
                edge.update_positions()
        return super().itemChange(change, value)

    def current_value(self):
        return self.combo.currentText()


class ResultNode(QGraphicsRectItem):
    """Final node showing combined output."""

    def __init__(self):
        super().__init__(0, 0, 150, 80)
        self.setBrush(QColor(40, 40, 80))
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemSendsScenePositionChanges)

        self.label = QLabel("Result")
        self.proxy = QGraphicsProxyWidget(self)
        self.proxy.setWidget(self.label)
        self.proxy.setPos(5, 30)

        self.in_socket1 = SocketItem(self, False)
        self.in_socket1.setPos(self.rect().left(), self.rect().center().y() - 15)
        self.in_socket2 = SocketItem(self, False)
        self.in_socket2.setPos(self.rect().left(), self.rect().center().y() + 15)
        self.edges = []

    def input_anchors(self):
        return [self.in_socket1.scenePos(), self.in_socket2.scenePos()]

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.edges:
                edge.update_positions()
        return super().itemChange(change, value)

    def set_text(self, text):
        self.label.setText(text)


class NodeScene(QGraphicsScene):
    """Scene managing the nodes and interactive edge creation."""

    def __init__(self, update_callback):
        super().__init__()
        self.update_callback = update_callback
        self.temp_line = None
        self.start_socket = None

    def mousePressEvent(self, event):
        item = self.itemAt(event.scenePos(), self.views()[0].transform())
        if isinstance(item, SocketItem) and item.is_output:
            self.start_socket = item
            self.temp_line = self.addLine(QLineF(item.scenePos(), item.scenePos()), QPen(Qt.white, 1, Qt.DashLine))
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.temp_line is not None:
            new_line = QLineF(self.temp_line.line().p1(), event.scenePos())
            self.temp_line.setLine(new_line)
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.temp_line is not None:
            item = self.itemAt(event.scenePos(), self.views()[0].transform())
            if isinstance(item, SocketItem) and not item.is_output and self.start_socket:
                edge = NodeEdge(self.start_socket, item)
                self.addItem(edge)
                self.start_socket.parent_node.edges.append(edge)
                item.parent_node.edges.append(edge)
                self.update_callback()
            self.removeItem(self.temp_line)
            self.temp_line = None
            self.start_socket = None
            return
        super().mouseReleaseEvent(event)


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Simple Node Editor")
    view = QGraphicsView()

    # placeholder callback, replaced after update_result is defined
    scene = NodeScene(update_callback=lambda: None)
    view.setScene(scene)
    window.setCentralWidget(view)

    color_node = OptionNode("Color", ["Red", "Green", "Blue"])
    hair_node = OptionNode("Hairstyle", ["Bun", "Short Bob", "Long", "Short"])
    result_node = ResultNode()

    color_node.setPos(-150, -50)
    hair_node.setPos(-150, 80)
    result_node.setPos(150, 0)

    scene.addItem(color_node)
    scene.addItem(hair_node)
    scene.addItem(result_node)

    color_node.combo.currentTextChanged.connect(lambda: update_result(scene))
    hair_node.combo.currentTextChanged.connect(lambda: update_result(scene))

    def update_result(scene_obj):
        color = None
        hair = None
        for item in scene_obj.items():
            if isinstance(item, NodeEdge):
                if item.end_socket.parent_node is result_node:
                    if item.start_socket.parent_node is color_node:
                        color = color_node.current_value()
                    elif item.start_socket.parent_node is hair_node:
                        hair = hair_node.current_value()
        text = f"Color: {color or 'N/A'}, Hair: {hair or 'N/A'}"
        result_node.set_text(text)

    # replace placeholder callback now that update_result exists
    scene.update_callback = lambda: update_result(scene)

    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
