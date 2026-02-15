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

---

Here is the English translation of my document.

---

# LLM Document Processing System

A powerful Web application that supports uploading various formats of documents, images, and web links for intelligent analysis using Large Language Models (LLMs).

## Features

### 📤 Part 1: Document Processing

* **Document Upload**: Supports PDF, Word (docx/doc), and text files.
* **Image Recognition**: Supports PNG, JPG, JPEG, GIF, and BMP; uses OCR to extract text.
* **Web Scraping**: Supports multiple web links with automatic content extraction.
* Optional use of Firecrawl API for advanced scraping.
* Built-in simple scraper as a fallback solution.


* **Batch Processing**: Supports simultaneous processing of multiple documents, images, and links.
* **Text Integration**: Automatically merges all extracted content into a single text body.

### 🤖 Part 2: LLM Analysis

* **Multi-Model Support**:
* OpenAI GPT series (GPT-4, GPT-3.5)
* Anthropic Claude series
* Custom API (OpenAI-compatible format)


* **Custom Prompts**: Full control over the analysis methodology.
* **Real-time Analysis**: Get AI analysis results quickly.

## Installation Steps

### 1. Prerequisites

* Python 3.8+
* Tesseract OCR (for image text recognition)

### 2. Install Tesseract OCR

#### Windows

1. Download the installer: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install to the default or a custom path.
3. If using a custom path, configure it in `utils/document_processor.py`:
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

### 3. Install Python Dependencies

```bash
cd document-llm-processor
pip install -r requirements.txt

```

### 4. (Optional) Configure Firecrawl API

To use Firecrawl for advanced web scraping:

```bash
# Windows
set FIRECRAWL_API_KEY=your_api_key_here

# macOS/Linux
export FIRECRAWL_API_KEY=your_api_key_here

```

## Usage

### 1. Start the Server

```bash
python app.py

```

The server will start at `http://localhost:5000`

### 2. Access the Web Interface

Open your browser and go to: `http://localhost:5000`

### 3. Workflow

#### Step 1: Upload Content

1. **Upload Files**: Click or drag files to the upload area.
2. **Input Text**: Paste text content directly.
3. **Add Links**: Enter one web link per line (multiple supported).
4. Click "Start Processing Documents."

#### Step 2: LLM Analysis

1. Select a Model Provider (OpenAI / Anthropic / Custom).
2. Select the specific Model.
3. Enter your API Key.
4. Write your analysis prompt.
5. Click "Start AI Analysis."

## Configuration Details

### Supported File Formats

* **Documents**: .txt, .pdf, .docx, .doc
* **Images**: .png, .jpg, .jpeg, .gif, .bmp
* **Maximum File Size**: 50MB

### LLM Configuration

#### OpenAI

* Requires API Key.
* Supported models: GPT-4, GPT-3.5-turbo, etc.
* Supports optional custom API Base URL.

#### Anthropic

* Requires API Key.
* Supported models: Claude Opus 4.6, Claude Sonnet 4.5, etc.

#### Custom API

* Requires API Base URL.
* Must be compatible with the OpenAI API format.

## Project Structure

```
document-llm-processor/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── document_processor.py   # Document processing logic
│   └── llm_handler.py          # LLM handling logic
├── templates/                  # HTML templates
│   └── index.html
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── uploads/                    # Temporary upload directory

```

## FAQ

### 1. Image OCR Recognition Failed

* Ensure Tesseract OCR is installed.
* Check if the Tesseract path configuration is correct.
* For Chinese recognition, ensure the Chinese language pack is installed.

### 2. Web Scraping Failed

* Some websites may have anti-scraping mechanisms.
* Configuring a Firecrawl API Key is recommended to improve the success rate.
* Ensure your network connection is stable.

### 3. LLM API Call Failed

* Check if the API Key is correct.
* Confirm your account balance is sufficient.
* Check your network connection and API Base URL.

## Security Tips

* API Keys are only stored temporarily in the browser and are not saved to the server.
* Uploaded files are deleted immediately after processing.
* It is recommended to run this application in a local or trusted environment.

## Tech Stack

* **Backend**: Flask, Python
* **Frontend**: HTML5, CSS3, JavaScript
* **Document Processing**: PyPDF2, python-docx, pytesseract
* **Web Scraping**: BeautifulSoup, Firecrawl
* **LLM**: OpenAI API, Anthropic API

## License

MIT License

## Contribution

Issues and Pull Requests are welcome!

---

Would you like me to adjust any specific terminology (e.g., more formal or more technical) for this translation?
