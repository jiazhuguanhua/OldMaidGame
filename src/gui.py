from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, QTextEdit, QListWidgetItem
)
from PyQt5.QtCore import Qt, QTimer
from game import OldMaidGame
import random

class OldMaidGameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("老处女纸牌游戏")
        self.setGeometry(200, 200, 600, 480)
        self.player_names = ["你", "电脑1", "电脑2", "电脑3"]
        self.game = OldMaidGame(self.player_names)
        self.game.deal_cards()
        self.init_ui()
        self.update_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel("🎴 老处女纸牌游戏 🎴")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-weight: bold; color: #2d8cf0;")
        layout.addWidget(title)

        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("margin: 8px;")
        layout.addWidget(self.info_label)

        self.hand_label = QLabel()
        self.hand_label.setAlignment(Qt.AlignCenter)
        self.hand_label.setStyleSheet("color: #19be6b; margin: 8px;")
        layout.addWidget(self.hand_label)

        layout.addWidget(QLabel("请选择要抽牌的玩家（双击）："))

        self.player_list = QListWidget()
        self.player_list.itemDoubleClicked.connect(self.human_draw_card)
        layout.addWidget(self.player_list)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet("background: #f6f6f6;")
        layout.addWidget(self.log_box, stretch=1)

        self.setLayout(layout)

    def update_ui(self):
        cur = self.game.players[self.game.current_player_index]
        self.info_label.setText(f"当前轮到：<b style='color:#ed4014'>{cur.name}</b>")
        if cur.name == "你":
            if cur.hand:
                self.hand_label.setText(f"你的手牌：<b>{'  '.join([c[0]+c[1] for c in cur.hand])}</b>")
            else:
                self.hand_label.setText("你的手牌：<b>无</b>")
            self.player_list.setEnabled(True)
            self.player_list.clear()
            for idx, p in enumerate(self.game.players):
                if idx != self.game.current_player_index and len(p.hand) > 0:
                    item = QListWidgetItem(f"{p.name}（剩{len(p.hand)}张）")
                    item.setData(Qt.UserRole, idx)
                    self.player_list.addItem(item)
        else:
            self.hand_label.setText(f"{cur.name} 正在操作...")
            self.player_list.clear()
            self.player_list.setEnabled(False)
            QTimer.singleShot(1200, self.computer_draw_card)

    def log(self, msg):
        self.log_box.append(msg)
        self.log_box.moveCursor(self.log_box.textCursor().End)

    def human_draw_card(self, item):
        cur_idx = self.game.current_player_index
        draw_idx = item.data(Qt.UserRole)
        card, out_players, loser = self.game.play_turn(draw_idx)
        msg = f"<b>你</b> 从 <b>{self.game.players[draw_idx].name}</b> 手中抽到了 <b>[{card[0]}{card[1]}]</b>"
        self.log(msg)
        if out_players:
            self.log("出局：" + "、".join(out_players))
        if loser:
            self.log(f"<b style='color:#ed4014'>游戏结束！{loser} 是老处女！</b>")
            self.info_label.setText("游戏结束")
            self.player_list.setEnabled(False)
            return
        self.game.next_player()
        self.update_ui()

    def computer_draw_card(self):
        cur = self.game.players[self.game.current_player_index]
        # 电脑策略：随机抽取下一个有牌的玩家
        candidates = [i for i, p in enumerate(self.game.players)
                      if i != self.game.current_player_index and len(p.hand) > 0]
        if not candidates:
            return
        draw_idx = random.choice(candidates)
        card, out_players, loser = self.game.play_turn(draw_idx)
        msg = f"<b>{cur.name}</b> 从 <b>{self.game.players[draw_idx].name}</b> 手中抽到了 <b>[{card[0]}{card[1]}]</b>"
        self.log(msg)
        if out_players:
            self.log("出局：" + "、".join(out_players))
        if loser:
            self.log(f"<b style='color:#ed4014'>游戏结束！{loser} 是老处女！</b>")
            self.info_label.setText("游戏结束")
            self.player_list.setEnabled(False)
            return
        self.game.next_player()
        self.update_ui()