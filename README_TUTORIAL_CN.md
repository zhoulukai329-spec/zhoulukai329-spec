# GitHub 个人主页 README 模板

本项目基于 [yuki4266/yuki4266](https://github.com/yuki4266/yuki4266)，提供一个可配置的 GitHub 个人主页 README，包含日夜主题插画、可编辑的技术栈徽章以及实时 GitHub 活跃数据。

该模板解决了原版耦合度太高的缺点，让用户不需要大量制图，消耗token，也能对自己的主页进行非常伟大的雷霆美化。大多数个性化设置都在 [`profile.toml`](profile.toml) 中完成。

## 1. 创建个人主页仓库

只有当仓库名称与 GitHub 用户名**完全一致**时，GitHub 才会将其中的 README 显示为个人主页。

1. 使用本仓库作为模板，将它 Fork/复制到你的账号下。
2. 将仓库命名为你的 GitHub 用户名。注意一定是用户名，而非对外显示名。
3. 确保仓库为Public。
4. 确保 `README.md` 位于仓库根目录。

如果你的默认分支不是 `main`，请同步修改 `.github/workflows/profile.yml`、`.github/workflows/sky.yml` 和 `.github/workflows/snake.yml` 中的分支名称。

## 2. 允许 GitHub Actions 更新仓库

本模板使用 GitHub Actions 自动生成 `README.md`、更新动态场景，并发布贡献蛇动画。

在 GitHub **仓库**页面（顶上那一排）进入：

`Settings` → `Actions` → `General` → `Workflow permissions`

选择 **Read and write permissions** 并保存。如果没有该权限，工作流可以生成文件，但无法将生成结果推送回仓库。

## 3. 修改个人信息

打开 `profile.toml`，修改 `[profile]` 部分：

```toml
[profile]
username = "Paimon"
name = "The Paimon"
tagline = "How about we explore the area ahead of us later?"
bio = "Best guider in Teyvat."
location = "Teyvat, Celestia"
website = "https://example.com"
email = "hello@example.com"
```

注意：`username` 必须填写 GitHub 登录名，而不是显示名称。它会被用于请求你的真实统计数据、连续贡献、活跃图、贡献蛇和主页访问量徽章。

`name` 只会作为页面上的显示文本，可以自由填写。

## 4. 添加、删除或重新组织技术栈

每项技术都对应一个独立的 `[[stack]]` 配置块：

```toml
[[stack]]
name = "Python"
logo = "python"
color = "3776AB"
group = "Languages"
```

字段含义如下：

- `name`：徽章上显示的文字。
- `logo`：[Simple Icons](https://simpleicons.org/) 中的图标 slug。如果没有合适的图标，可以留空。
- `color`：徽章颜色，填写六位十六进制值，不要包含 `#`。
- `group`：相同分组的技术会显示在同一行。

例如，添加 Rust：

```toml
[[stack]]
name = "Rust"
logo = "rust"
color = "000000"
group = "Languages"
```

要删除某项技术，删除它完整的 `[[stack]]` 配置块即可。要调整顺序，直接在 `profile.toml` 中移动配置块。不需要创建或编辑任何 chip SVG 文件。

## 5. 自定义颜色

`[theme]` 部分控制生成的徽章和活跃度卡片：

```toml
[theme]
accent = "F4795B"
label = "555555"
```

颜色请使用不带 `#` 的十六进制值。`accent` 用于高亮、图表线条、连续贡献卡片和主页访问徽章；`label` 用于图表中的次要文字。

## 6. 启用或关闭实时统计

每个统计组件都可以独立开关：

```toml
[stats]
show_stats = true
show_streak = true
show_activity = true
show_snake = true
show_profile_views = true
```

这些组件不是存储在仓库中的示例数字：

- `show_stats`：从 GitHub Readme Stats 请求配置用户当前的 GitHub 概览。
- `show_streak`：从 GitHub Readme Streak Stats 请求配置用户的连续贡献数据。
- `show_activity`：显示配置用户的公开 GitHub 活跃图。
- `show_snake`：显示根据仓库所有者贡献网格生成的贡献蛇动画。
- `show_profile_views`：显示与配置用户名关联的主页访问量计数。

将任意选项设置为 `false`，即可从生成的 README 中移除对应部分。

这些统计卡片依赖公开的第三方服务。卡片暂时空白通常意味着服务被限流或暂时不可用，并不代表 README 中保存了固定数据。

## 7. 配置动态场景

场景工作流从 `[scene]` 中读取位置和时区：

```toml
[scene]
latitude = "37.7749"
longitude = "-122.4194"
timezone = "America/Los_Angeles"
weather = ""
season = ""
```

请使用 [IANA 时区名称](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)，例如 `Asia/Shanghai` 或 `Europe/London`。

将 `weather` 和 `season` 留空时，系统会使用实时天气和当前日期。你也可以固定场景：

```toml
weather = "rain"
season = "autumn"
```

支持的手动天气值为 `clear`、`clouds`、`rain`、`snow`、`fog` 和 `storm`；支持的季节值为 `spring`、`summer`、`autumn` 和 `winter`。

## 8. 生成 README

### 自动生成

将 `profile.toml` 提交并推送到 `main` 分支。**Generate profile README** 工作流会自动运行并提交更新后的 `README.md`。

也可以从以下位置手动运行：

`Actions` → `Generate profile README` → `Run workflow`

### 本地生成

需要 Python 3.11 或更高版本，因为生成器使用标准库中的 TOML 解析器。

```bash
python scripts/generate_readme.py
```

检查生成后的 `README.md`，然后同时提交配置文件和生成结果：

```bash
git add profile.toml README.md
git commit -m "docs: customise profile"
git push
```

## 9. 生成内容与手写内容

生成器只会替换以下标记之间的内容：

```html
<!-- PROFILE:GENERATED:START -->
<!-- PROFILE:GENERATED:END -->
```

标记之外的内容会被保留。请将长篇介绍或模板说明放在标记之外。不要手动修改标记内部的内容，因为下一次生成时这些修改会被覆盖。

`bloom-header.svg`、`sky.svg` 和 `garden-footer.svg` 等插画文件只是装饰，不包含你的活跃数据。你可以替换它们，或者从 `scripts/generate_readme.py` 中删除对应代码，而不影响个人资料配置模型。

## 10. 首次运行检查清单

推送修改后，请确认：

- 仓库名称与 GitHub 用户名完全一致。
- `profile.username` 填写的是 GitHub 登录名。
- GitHub Actions 已获得读写工作流权限。
- **Generate profile README** 工作流成功完成。
- **generate snake animation** 工作流创建了 `output` 分支。
- 生成的 README 中统计链接包含你的用户名。

贡献蛇动画可能要等工作流首次完成后才会显示。

## 11. 常见问题

### 工作流无法推送修改

在仓库 Actions 设置中启用 **Read and write permissions**。同时检查分支保护规则是否禁止 GitHub Actions 直接推送到 `main`。

### README 仍然显示其他用户的数据

修改 `profile.username`，重新生成 `README.md`，然后手动运行贡献蛇工作流。只修改 `name` 不会改变统计数据对应的账号。

### 技术栈徽章没有图标

在 [Simple Icons](https://simpleicons.org/) 中确认图标 slug。slug 通常是小写形式，并且可能与产品的显示名称不同。

### 贡献蛇动画没有显示

手动运行 **generate snake animation**，确认工作流创建了 `output` 分支。贡献蛇 URL 要求个人主页仓库名称与配置的用户名一致。

### 天气与所在位置不匹配

检查 `[scene]` 中的纬度、经度和 IANA 时区。若希望使用自动值，还要确认 `weather` 和 `season` 为空。
