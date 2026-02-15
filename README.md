# 大模型文档处理系统

一个功能强大的 Web 应用，支持上传多种格式的文档、图片、网页链接，并使用大模型进行智能分析。

## 功能特性

### 📤 第一部分：文档处理
- **文档上传**：支持 PDF、Word (docx/doc)、文本文件
- **图片识别**：支持 PNG、JPG、JPEG、GIF、BMP，使用 OCR 提取文字
- **网页抓取**：支持多个网页链接，自动提取正文内容
  - 可选使用 Firecrawl API 进行高级抓取
  - 内置简单抓取功能作为后备方案
- **批量处理**：支持同时处理多个文档、图片和链接
- **文本整合**：自动将所有提取的内容整合成一个文本

### 🤖 第二部分：大模型分析
- **多模型支持**：
  - OpenAI GPT 系列 (GPT-4, GPT-3.5)
  - Anthropic Claude 系列
  - 自定义 API（兼容 OpenAI 格式）
- **自定义提示词**：完全控制分析方式
- **实时分析**：快速获得 AI 分析结果

## 安装步骤

### 1. 环境要求
- Python 3.8+
- Tesseract OCR（用于图片文字识别）

### 2. 安装 Tesseract OCR

#### Windows
1. 下载安装程序：https://github.com/UB-Mannheim/tesseract/wiki
2. 安装到默认路径或自定义路径
3. 如果使用自定义路径，需要在 `utils/document_processor.py` 中配置：
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

#### macOS
```bash
brew install tesseract tesseract-lang
```

#### Linux
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
```

### 3. 安装 Python 依赖

```bash
cd document-llm-processor
pip install -r requirements.txt
```

### 4. （可选）配置 Firecrawl API

如需使用 Firecrawl 进行高级网页抓取：

```bash
# Windows
set FIRECRAWL_API_KEY=your_api_key_here

# macOS/Linux
export FIRECRAWL_API_KEY=your_api_key_here
```

## 使用方法

### 1. 启动服务器

```bash
python app.py
```

服务器将在 `http://localhost:5000` 启动

### 2. 访问 Web 界面

在浏览器中打开：`http://localhost:5000`

### 3. 使用流程

#### 步骤 1：上传文档内容
1. **上传文件**：点击或拖拽文件到上传区域
2. **输入文本**：直接粘贴文本内容
3. **添加链接**：每行输入一个网页链接（支持多个）
4. 点击"开始处理文档"

#### 步骤 2：大模型分析
1. 选择模型提供商（OpenAI / Anthropic / 自定义）
2. 选择具体模型
3. 输入 API Key
4. 编写分析提示词
5. 点击"开始 AI 分析"

## 配置说明

### 支持的文件格式

- **文档**：.txt, .pdf, .docx, .doc
- **图片**：.png, .jpg, .jpeg, .gif, .bmp
- **最大文件大小**：50MB

### 大模型配置

#### OpenAI
- 需要 API Key
- 支持模型：GPT-4, GPT-3.5-turbo 等
- 可选配置自定义 API Base URL

#### Anthropic
- 需要 API Key
- 支持模型：Claude Opus 4.6, Claude Sonnet 4.5 等

#### 自定义 API
- 需要提供 API Base URL
- 必须兼容 OpenAI API 格式

## 项目结构

```
document-llm-processor/
├── app.py                      # Flask 主应用
├── requirements.txt            # Python 依赖
├── utils/                      # 工具模块
│   ├── __init__.py
│   ├── document_processor.py   # 文档处理
│   └── llm_handler.py          # 大模型处理
├── templates/                  # HTML 模板
│   └── index.html
├── static/                     # 静态资源
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── uploads/                    # 临时上传目录
```

## 常见问题

### 1. 图片 OCR 识别失败
- 确保已安装 Tesseract OCR
- 检查 Tesseract 路径配置是否正确
- 对于中文识别，确保安装了中文语言包

### 2. 网页抓取失败
- 某些网站可能有反爬虫机制
- 建议配置 Firecrawl API Key 以提高成功率
- 确保网络连接正常

### 3. 大模型 API 调用失败
- 检查 API Key 是否正确
- 确认账户余额充足
- 检查网络连接和 API Base URL

## 安全提示

- API Key 仅在浏览器中临时存储，不会保存到服务器
- 上传的文件在处理后会立即删除
- 建议在本地或可信环境中运行此应用

## 技术栈

- **后端**：Flask, Python
- **前端**：HTML5, CSS3, JavaScript
- **文档处理**：PyPDF2, python-docx, pytesseract
- **网页抓取**：BeautifulSoup, Firecrawl
- **大模型**：OpenAI API, Anthropic API

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
