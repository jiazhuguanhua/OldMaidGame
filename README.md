# Old Maid Game (老处女纸牌游戏)

## 项目简介
本项目为经典纸牌游戏“老处女”的 PyQt5 图形化实现。支持1名玩家对战3名电脑，界面美观，操作简单，适合课程设计或个人娱乐。

## 游戏规则
- 使用一副去掉一张Q的纸牌（共51张）。
- 你与3个电脑玩家轮流抽牌，抽到后自动配对并移除。
- 最后剩下“老处女”牌的人为输家。

## 功能特色
- 全中文界面，字体大，适合演示和教学。
- 你只需双击玩家列表即可抽牌，电脑自动行动。
- 所有操作和结果都在主窗口日志区显示，无弹窗打扰。
- 电脑玩家采用简单策略自动抽牌。
- 支持跨平台（Windows/Linux/Mac）。

## 安装步骤

1. 克隆项目到本地：
   ```bash
   git clone <your-repo-url>
   ```
2. 进入项目目录：
   ```bash
   cd OldMaidGame
   ```
3. 安装依赖（建议使用虚拟环境）：
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

1. 运行游戏：
   ```bash
   python src/main.py
   ```
2. 按界面提示进行游戏：
   - 轮到你时，双击列表选择要抽牌的电脑玩家。
   - 电脑自动行动，无需你操作。
   - 游戏结果和过程会在下方日志区显示。

## 目录结构

```
OldMaidGame/
├── src/
│   ├── main.py         # 程序入口，设置全局字体并启动GUI
│   ├── gui.py          # 图形界面主逻辑
│   ├── game.py         # 游戏核心逻辑
│   ├── player.py       # 玩家类
│   └── utils.py        # 备用工具函数（可选）
├── requirements.txt    # 依赖列表
├── README.md           # 项目说明
└── .gitignore          # Git忽略文件
```

## 主要文件说明

- `src/main.py`：程序入口，设置全局字体，启动主窗口。
- `src/gui.py`：PyQt5界面逻辑，负责玩家操作、电脑自动行动、日志输出等。
- `src/game.py`：游戏流程与规则实现。
- `src/player.py`：玩家数据结构与操作。
- `src/utils.py`：备用工具函数（如洗牌等，可选）。
- `requirements.txt`：依赖库列表。
- `README.md`：项目说明文档。

## 贡献方式

欢迎提交 issue 或 pull request 进行改进！

## 许可证

MIT License

---

> 本项目适合大一/大二课程设计、Python学习、桌面小游戏开发等场景。