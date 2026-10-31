# Assignment 2：提交前检查清单

本清单根据课程 Assignment 2 的要求整理，适用于“香港鸟类观测记录，1985–2025”项目。

## 你的项目资料

| 项目 | 当前内容 |
|---|---|
| 自然现象 | 香港地区鸟类观测记录 |
| 时间范围 | 1985–2025 |
| 鸟类数据 | GBIF Occurrence Search API 的 JSON 回应 |
| 地图边界 | 香港政府地方行政区分界 JSON |
| 原始资料位置 | `data/gbif-hong-kong-birds-YEAR.json`、`data/hong-kong-boundary.geojson` |
| 静态图片 | `out/hong-kong-bird-records-2025.svg` |
| 互动作品 | `site/index.html` |
| 运行方式 | `uv run fetch.py`、`uv run plot.py` |

## 老师的核心要求

- [ ] 仓库是**公开**的，且在你自己的 GitHub 账号下。
- [ ] 仓库名称与自然现象有关，建议为 `hong-kong-bird-records`，不要叫 `assignment2`。
- [ ] `README.md` 位于仓库最外层，至少 150 词，并嵌入一张图片。
- [ ] `README.md` 说明现象、数据来源链接、原始资料内容、图片意义、图像隐藏的内容和运行命令。
- [ ] `PROCESS.md` 位于仓库最外层，诚实说明工具与 AI 使用方式，并包含一项保留的建议、一项拒绝的建议，以及原因。
- [ ] `data/` 内有原始资料，且不经过修改；作品下载一次后应可离线运行。
- [ ] `out/` 内有图片。运行 `plot.py` 后应出现 `out/hong-kong-bird-records-2025.svg`。
- [ ] 至少有一个 `.py` 文件；如有外部依赖，文件顶部须有 `# /// script` dependency block。
- [ ] 代码包含你能解释的函数和循环。
- [ ] Git 提交至少 3 次，且横跨至少 2 天；提交信息应说明你做了什么。
- [ ] 最后在 Canvas 提交新的仓库 URL。

## 推荐检查顺序

```powershell
uv run fetch.py
uv run plot.py
uv run ../pfad/assignments/check.py --assignment 2
git status
git add .
git commit -m "Build interactive Hong Kong bird visualisation"
git push
```

## GitHub 改名

建议改为：

```text
hong-kong-bird-records
```

GitHub 仓库主页 → **Settings** → **Repository name** → 输入新名称 → **Rename**。

改名后，在本机更新远端地址：

```powershell
git remote set-url origin https://github.com/你的用户名/hong-kong-bird-records.git
git remote -v
git push
```

如果已在 Canvas 提交旧网址，请更新为新的仓库 URL。
