# 🌸 初音未来主题 GitHub Profile 模板

一个可复用的初音未来（Hatsune Miku）可爱风 GitHub 个人主页模板。替换 9 个占位符，5 分钟拥有自己的初音主题主页。

---

## 🎀 快速开始（3 步）

### 第 1 步：Fork 本仓库

点击右上角 `Fork` 按钮，将项目 Fork 到你的账号下。

### 第 2 步：替换占位符

打开 `template/PROFILE.md`，找到以下 9 个占位符并替换为你的信息：

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{USERNAME}` | GitHub 用户名 | `kaki` |
| `{DISPLAY_NAME}` | 显示名称（会出现在 banner 中） | `卡琪` |
| `{BIO}` | 个人简介 | `一个热爱前端开发的二次元爱好者` |
| `{TAGS}` | 个人标签 | `🎸 邦多利RAS厨 · 🎵 日音爱好者` |
| `{GALLERY_TITLE_CN}` | 图片区中文标题 | `初音画廊` |
| `{GALLERY_TITLE_EN}` | 图片区英文标题 | `Miku Gallery` |
| `{SKILLS_LIST}` | 技能徽章列表 | 见下方技能徽章教程 |
| `{CAREER_GOAL}` | 职业规划（一句话） | `开发 | 产品 | 金融科技` |
| `{CONTACT_LINKS}` | 联系方式（自由格式） | `📕 小红书 · 🅱️ B站 · 📧 邮箱` |

### 第 3 步：部署到你的主页

1. 新建一个与你 GitHub 用户名**完全相同**的仓库（如 `kaki/kaki`）
2. 将替换好的 `template/PROFILE.md` 内容复制到新仓库的 `README.md`
3. 将 `assets/` 文件夹复制到新仓库中
4. **重要：** 编辑 `assets/banner.svg`，搜索 "你的名字" 替换为你的显示名称
5. 替换菱形图片（见下方教程）
6. 搞定！访问 `github.com/{你的用户名}` 查看效果

---

## 🛠️ 自定义教程

### 技能徽章

技能徽章使用 [Shields.io](https://shields.io/) 生成。示例：

```html
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
<img src="https://img.shields.io/badge/Godot-478CBF?style=for-the-badge&logo=godot-engine&logoColor=white" />
```

更多徽章样式请访问 [Shields.io](https://shields.io/) 搜索。

### 替换图片

模板预留了 5 个图片位。替换步骤：

1. 准备 5 张图片，命名为 `miku-01.png` ~ `miku-05.png`
2. 上传到 `assets/` 文件夹
3. 将 `assets/miku-diamond-01.svg` ~ `05.svg` 也上传（菱形裁剪框已预设好，引用同目录的 `miku-01.png` ~ `miku-05.png`）

### 修改 Banner 标题和副标题

编辑 `assets/banner.svg`：
- 搜索 `欢迎来到 你的名字 的主页`，把 "你的名字" 改成你的显示名称
- 搜索 `每一个代码都是一首歌`，改成你喜欢的副标题

### 更换配色

在 `assets/banner.svg` 和 `assets/miku-diamond-*.svg` 中搜索以下颜色并替换：
- `#39C5BB` — 初音葱绿（主色调）
- `#FFB7C5` — 樱花粉（辅助色）
- `#FFD1DC` — 浅樱花粉
- `#FFD700` — 星星金色

---

## 📂 项目结构

```
Miku-theme-profile/
├── README.md                  ← 本文件
├── template/
│   └── PROFILE.md             ← 核心模板（9个占位符）
├── assets/
│   ├── banner.svg             ← 顶部装饰横幅（含标题）
│   ├── avatar-frame.svg       ← 头像占位框（可选）
│   ├── diamond-frame.svg      ← 空菱形占位框（备用）
│   ├── miku-diamond-01.svg    ← 菱形图1（base64内嵌）
│   ├── miku-diamond-02.svg    ← 菱形图2
│   ├── miku-diamond-03.svg    ← 菱形图3
│   ├── miku-diamond-04.svg    ← 菱形图4
│   ├── miku-diamond-05.svg    ← 菱形图5
│   └── .sources.md            ← 素材来源说明
└── .gitignore
```

---

## 🎨 设计特色

- 🏷️ 初音经典配色：葱绿 `#39C5BB` + 樱花粉 `#FFB7C5`
- 🌸 手写 SVG 装饰（樱花花瓣 + 音符 + 小星星）
- 💎 图片画廊（5 个圆角图位 + 彩色边框）
- 🏷️ Shields.io 技能徽章
- 🎵 全程中文，可爱活泼风格
- 🔌 零外部运行时依赖

---

## 📄 许可

MIT License。所有 SVG 装饰元素为手写代码。

---

## 💖 致谢

- 初音未来（Hatsune Miku）— Crypton Future Media
- 徽章服务由 [Shields.io](https://shields.io/) 提供
