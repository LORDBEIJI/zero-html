<!-- 记录作品视觉方案、设计依据与素材版权。 -->
# 纹脉 · 百工录

深夜的博物馆里，一束光落在器物上。以一条线连接丝、木、土、火，讲述四种材料如何成为技艺。

## 视觉方案与复核

- 墨 #08080A、次墨 #0D0D10、铜金 #C9A227、釉青 #8FBFB0、宣纸 #F2EDE4、印泥 #B23A2E。
- 思源宋体用于标题和材料汉字，系统黑体用于正文，宋体保留横细竖粗的物质感。
- 首页左侧标题与右侧器物形成约 1:1.618 的视觉平衡；下方四章使用交错尺寸，不将一切切成相同卡片。
- 只让器物成为视觉重点；装饰线串联叙事，毛玻璃用于导航和浮层。
- 复核后放弃通用的圆角信息卡堆叠、虚构年数和工序统计；首页以器物、材料与地域建立信息层次。

```text
 标识                 导航                搜索 / 主题
             一条线                    ↘
 标题 / 主张                      青瓷器物
 进入展馆                         器物档案
 ──────────────────────────────────────
 丝 / 木 / 土 / 火           四种材料与技艺
 错位展品入口                手艺与人的故事
```

## 使用的设计 skill

- frontend-design：Anthropic 官方仓库，2026-10-20 下载，存于 design-skills/frontend-design。
  https://github.com/anthropics/skills/tree/main/skills/frontend-design
- web-design-guidelines：Vercel 官方仓库，2026-10-20 下载，存于 design-skills/web-design-guidelines。
  https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
- 均作为设计与验收参考；项目规格与用户要求优先。不复制模板、组件外观或现有网站。

## 素材登记

| 文件 | 内容 | 来源与许可 | 修改 |
|---|---|---|---|
| assets/svg/grain.svg | 纸感噪点 | 本项目原创 SVG | 无 |
| assets/svg/*.svg | 纹样、器物、印章 | 本项目原创绘制 | 无 |
| assets/fonts/wenmai-serif.woff2 | 思源宋体网页子集 | Google Fonts / Noto Serif SC，SIL OFL 1.1；https://github.com/google/fonts/tree/main/ofl/notoserifsc | 公开字体下载后，页面文字在本地裁剪 |
| assets/img/celadon-still-life-source.png | 青瓷梅瓶意象源图 | OpenAI 内置 imagegen；AI 生成，非真实文物照片 | 无内容编辑 |
| assets/img/celadon-still-life.webp | 首页器物意象 | 上述自生成源图 | Sharp 转 WebP，宽 1800px |
| assets/img/celadon-still-life-mobile.webp | 移动端器物意象 | 上述自生成源图 | Sharp 转 WebP，宽 720px |
| assets/svg/embroidery.svg | 丝线与绣绷意象 | 原创 SVG / scripts/assets.mjs | 无 |
| assets/svg/carving.svg | 木纹与浮雕莲花意象 | 原创 SVG / scripts/assets.mjs | 无 |
| assets/svg/cloisonne.svg | 铜丝与珐琅意象 | 原创 SVG / scripts/assets.mjs | 无 |
| assets/svg/meiping.svg、yuhuchun.svg、bowl.svg、enamel.svg | 四类器形 | 原创 SVG / scripts/assets.mjs | 无 |
| assets/svg/seal.svg | 标识与页尾印章 | 原创 SVG | 无 |
| stories.html 内联 SVG | 四位匠人的抽象剪影 | 原创 SVG，不冒充本人肖像 | 无 |

完整 AI 提示词见 [生成记录](docs/IMAGE_PROMPT.md)。本地生成的版权状态需按适用规则判断，不将工具输出声称为第三方开放文物图。

## 已完成的阶段验收

- P0：八页互通，令牌与四档基础布局。
- P1：青瓷暗场首页、同点数叙事线、四章错位入口。
- P2：车削器形、釉面 shader、惯性控制、桌面与移动降级。
- P3：四种独立体验、按钮与拖动、重来与完成示例。
- P4：人物筛选抽屉、检索、主题、收藏、浏览记录与移动导航。
- P5：静态检查、四档八页浏览器检查、慢网、无 WebGL 与上下文丢失，以及交付预览包。正式身份命名待参赛信息补齐。

未声称已经在真实 Chrome 129 或比赛电脑上验证帧率。验证数据与截图见 reports/。

AI 视觉不代表真实馆藏；程序化器物为形制研究，不是文物测绘复刻。技艺体验属于教学示意，不能代替真实工艺操作。
