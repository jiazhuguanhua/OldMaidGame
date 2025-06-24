# filepath: old-maid-game/src/main.py

from gui import OldMaidGameGUI
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
import sys

def main():
    app = QApplication(sys.argv)
    # 设置全局统一字体
    font = QFont()
    font.setFamily("微软雅黑")  # 可选：更美观的中文字体
    font.setPointSize(18)      # 统一字号
    app.setFont(font)
    window = OldMaidGameGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()