# 快速开始指南

## 一键安装和启动

### Windows 用户

1. **安装 Python 依赖**
```bash
cd document-llm-processor
pip install -r requirements.txt
```

2. **安装 Tesseract OCR**
   - 下载：https://github.com/UB-Mannheim/tesseract/wiki
   - 安装后如果不在默认路径，需要修改 `utils/document_processor.py` 第 9 行

3. **启动服务器**
```bash
start.bat
```
或者
```bash
python app.py
```

4. **访问应用**
   - 打开浏览器访问：http://localhost:5000

### macOS/Linux 用户

1. **安装 Tesseract OCR**
```bash
# macOS
brew install tesseract tesseract-lang

# Ubuntu/Debian
sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
```

2. **安装 Python 依赖**
```bash
cd document-llm-processor
pip3 install -r requirements.txt
```

3. **启动服务器**
```bash
chmod +x start.sh
./start.sh
```
或者
```bash
python3 app.py
```

4. **访问应用**
   - 打开浏览器访问：http://localhost:5000

## 使用示例

### 示例 1：分析多个 PDF 文档

1. 上传多个 PDF 文件
2. 点击"开始处理文档"
3. 等待处理完成
4. 选择 OpenAI GPT-4
5. 输入 API Key
6. 提示词示例：
   ```
   请总结这些文档的核心内容，并列出主要观点和结论。
   ```
7. 点击"开始 AI 分析"

### 示例 2：提取图片中的文字并分析

1. 上传包含文字的图片（支持多张）
2. 点击"开始处理文档"
3. 系统会自动 OCR 识别图片中的文字
4. 选择模型和输入 API Key
5. 提示词示例：
   ```
   请整理图片中的所有文字，并进行分类汇总。
   ```
6. 点击"开始 AI 分析"

### 示例 3：分析网页内容

1. 在"网页链接"区域输入多个网址（每行一个）：
   ```
   https://example.com/article1
   https://example.com/article2
   https://example.com/article3
   ```
2. 点击"开始处理文档"
3. 系统会自动抓取网页正文
4. 选择模型和输入 API Key
5. 提示词示例：
   ```
   请分析这些文章的共同主题，并总结每篇文章的核心观点。
   ```
6. 点击"开始 AI 分析"

### 示例 4：混合处理

同时处理：
- 上传 2 个 PDF 文档
- 上传 3 张图片
- 粘贴一段文字
- 输入 5 个网页链接

系统会将所有内容整合后一起分析。

## 常用提示词模板

### 文档总结
```
请总结以下文档的主要内容，包括：
1. 核心主题
2. 关键观点
3. 重要结论
4. 实用建议
```

### 信息提取
```
请从文档中提取以下信息：
- 关键人物
- 重要日期
- 核心数据
- 联系方式
以结构化的方式呈现。
```

### 对比分析
```
请对比分析这些文档的异同点：
1. 共同主题是什么？
2. 各有哪些独特观点？
3. 存在哪些矛盾或冲突？
4. 综合来看，最合理的结论是什么？
```

### 专业领域分析
```
作为 [领域] 专家，请分析这些文档：
1. 技术方案的优缺点
2. 实施建议
3. 潜在风险
4. 改进方向
```

## 提示

- 单次上传文件总大小不超过 50MB
- 处理大量文档时可能需要较长时间
- 建议使用 Chrome 或 Firefox 浏览器
- API Key 不会保存，每次使用需重新输入
- 如果网页抓取失败，可以尝试配置 Firecrawl API Key

## 故障排除

### 问题：OCR 识别失败
**解决方案**：
1. 确认 Tesseract 已正确安装
2. 检查图片清晰度
3. 尝试提高图片分辨率

### 问题：网页抓取返回空内容
**解决方案**：
1. 检查网址是否可访问
2. 尝试配置 Firecrawl API Key
3. 某些网站可能需要登录才能访问

### 问题：大模型 API 超时
**解决方案**：
1. 减少文档数量
2. 分批处理
3. 检查网络连接
4. 选择更快的模型（如 GPT-3.5）

## 技术支持

如遇到问题，请检查：
1. Python 版本 >= 3.8
2. 所有依赖已正确安装
3. Tesseract OCR 已安装并配置
4. API Key 有效且有余额
