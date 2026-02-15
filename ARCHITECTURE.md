# 系统架构说明

## 总体架构

```
┌─────────────────────────────────────────────────────────────┐
│                        浏览器 (前端)                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              HTML + CSS + JavaScript                  │   │
│  │  - 文件上传界面                                        │   │
│  │  - 文本输入界面                                        │   │
│  │  - URL 输入界面                                        │   │
│  │  - 模型选择界面                                        │   │
│  │  - 结果展示界面                                        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↕ HTTP/JSON
┌─────────────────────────────────────────────────────────────┐
│                    Flask Web 服务器 (后端)                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    app.py (主应用)                     │   │
│  │  - /api/process-documents (文档处理 API)              │   │
│  │  - /api/analyze-with-llm (大模型分析 API)             │   │
│  │  - /api/models (获取模型列表 API)                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                            ↕                                 │
│  ┌─────────────────────┐       ┌──────────────────────┐    │
│  │  DocumentProcessor   │       │     LLMHandler       │    │
│  │  (文档处理模块)       │       │   (大模型处理模块)    │    │
│  │                      │       │                      │    │
│  │  - process_pdf()     │       │  - OpenAI API        │    │
│  │  - process_docx()    │       │  - Anthropic API     │    │
│  │  - process_image()   │       │  - Custom API        │    │
│  │  - process_url()     │       │                      │    │
│  └─────────────────────┘       └──────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                      外部服务和库                             │
│  - PyPDF2 / pdfplumber (PDF 解析)                            │
│  - python-docx (Word 解析)                                   │
│  - Tesseract OCR (图片文字识别)                              │
│  - BeautifulSoup (网页解析)                                  │
│  - Firecrawl API (高级网页抓取)                              │
│  - OpenAI API (GPT 模型)                                     │
│  - Anthropic API (Claude 模型)                               │
└─────────────────────────────────────────────────────────────┘
```

## 工作流程

### 阶段 1：文档处理流程

```
用户上传 → Flask 接收 → DocumentProcessor 处理 → 返回文本
                              ↓
                    ┌─────────┴─────────┐
                    ↓                   ↓
            PDF/Word/TXT           图片/URL
                    ↓                   ↓
            文本提取器          OCR/网页抓取
                    ↓                   ↓
                    └─────────┬─────────┘
                              ↓
                        文本整合器
                              ↓
                    返回整合后的文本
```

### 阶段 2：大模型分析流程

```
整合文本 + 提示词 + 模型配置
           ↓
      LLMHandler
           ↓
   ┌───────┴────────┐
   ↓                ↓
OpenAI API    Anthropic API
   ↓                ↓
   └───────┬────────┘
           ↓
      返回分析结果
           ↓
      前端展示
```

## 核心模块详解

### 1. app.py (主应用)

**职责**：
- 路由管理
- 请求处理
- 文件上传管理
- 响应返回

**主要端点**：
- `GET /`：返回主页面
- `POST /api/process-documents`：处理文档
- `POST /api/analyze-with-llm`：调用大模型分析
- `GET /api/models`：获取支持的模型列表

### 2. DocumentProcessor (文档处理器)

**文件**：`utils/document_processor.py`

**方法**：
- `process_file(filepath)`：根据文件类型分发处理
- `process_pdf(filepath)`：处理 PDF 文件
  - 优先使用 pdfplumber
  - 备用方案使用 PyPDF2
- `process_docx(filepath)`：处理 Word 文档
  - 提取段落文本
  - 提取表格内容
- `process_txt(filepath)`：处理纯文本
  - 支持 UTF-8 和 GBK 编码
- `process_image(filepath)`：图片 OCR
  - 使用 Tesseract
  - 支持中英文混合识别
- `process_url(url)`：网页抓取
  - 优先使用 Firecrawl API
  - 备用方案使用 BeautifulSoup
- `combine_texts(text_items)`：整合所有文本

### 3. LLMHandler (大模型处理器)

**文件**：`utils/llm_handler.py`

**方法**：
- `analyze()`：主分析方法
- `analyze_with_openai()`：调用 OpenAI API
- `analyze_with_anthropic()`：调用 Anthropic API
- `analyze_with_custom()`：调用自定义 API

**支持的模型**：
- OpenAI: GPT-4, GPT-3.5-turbo 等
- Anthropic: Claude Opus 4.6, Claude Sonnet 4.5 等
- Custom: 任何兼容 OpenAI 格式的 API

### 4. 前端 (HTML + CSS + JS)

**文件**：
- `templates/index.html`：页面结构
- `static/css/style.css`：样式设计
- `static/js/main.js`：交互逻辑

**主要功能**：
- 文件拖拽上传
- 多文件管理
- 实时状态更新
- 加载动画
- 错误提示
- 结果展示

## 数据流

### 上传处理流程

```
1. 用户上传文件/输入文本/输入 URL
   ↓
2. JavaScript 收集所有数据
   ↓
3. FormData 封装发送到 /api/process-documents
   ↓
4. Flask 接收并保存临时文件
   ↓
5. DocumentProcessor 逐个处理
   ↓
6. 提取的文本存入列表
   ↓
7. combine_texts() 整合所有文本
   ↓
8. 删除临时文件
   ↓
9. 返回 JSON 响应
   ↓
10. 前端展示处理结果
```

### AI 分析流程

```
1. 用户配置模型和提示词
   ↓
2. JavaScript 发送 JSON 到 /api/analyze-with-llm
   ↓
3. LLMHandler 根据模型类型选择 API
   ↓
4. 构造 API 请求（包含文本 + 提示词）
   ↓
5. 调用外部 AI API
   ↓
6. 接收 AI 响应
   ↓
7. 提取结果文本
   ↓
8. 返回 JSON 响应
   ↓
9. 前端展示分析结果
```

## 安全考虑

1. **文件上传安全**
   - 文件类型白名单验证
   - 文件大小限制（50MB）
   - 安全文件名处理
   - 处理后立即删除

2. **API Key 保护**
   - 仅在客户端浏览器中临时存储
   - 不保存到服务器
   - 不记录日志

3. **输入验证**
   - 所有用户输入都进行验证
   - URL 安全检查
   - 防止路径遍历攻击

## 性能优化

1. **文件处理**
   - 支持多种 PDF 解析库，自动选择最佳方案
   - 临时文件及时清理
   - 合理的超时设置

2. **网页抓取**
   - 优先使用高效的 Firecrawl API
   - 备用简单抓取方案
   - 请求超时保护

3. **前端**
   - 异步请求，不阻塞 UI
   - 加载状态提示
   - 结果分批显示

## 扩展性

### 添加新的文档类型

在 `DocumentProcessor` 中添加新的处理方法：

```python
def process_new_format(self, filepath):
    # 处理逻辑
    return extracted_text
```

在 `process_file()` 中添加分发逻辑。

### 添加新的大模型

在 `LLMHandler` 中添加新的处理方法：

```python
def analyze_with_new_model(self, text, model_name, prompt, api_key):
    # API 调用逻辑
    return result
```

在前端 `main.js` 的 `modelConfigs` 中添加模型配置。

## 依赖关系

```
Flask (Web 框架)
├── flask-cors (跨域支持)
├── werkzeug (文件处理)
│
文档处理
├── PyPDF2 (PDF 解析)
├── pdfplumber (PDF 解析备选)
├── python-docx (Word 解析)
├── Pillow (图片处理)
├── pytesseract (OCR)
│
网页处理
├── requests (HTTP 请求)
├── beautifulsoup4 (HTML 解析)
├── lxml (解析器)
├── firecrawl-py (高级抓取)
│
AI 模型
├── openai (OpenAI API)
└── anthropic (Anthropic API)
```

## 未来改进方向

1. **功能增强**
   - 支持更多文档格式（Excel, PowerPoint 等）
   - 批量下载处理结果
   - 结果导出为 PDF/Word
   - 历史记录保存

2. **性能优化**
   - 异步文档处理
   - 进度条显示
   - 大文件分块处理
   - 缓存机制

3. **用户体验**
   - 拖拽排序文档
   - 预览功能
   - 模板管理
   - 快捷键支持

4. **安全增强**
   - 用户认证
   - API Key 加密存储
   - 访问日志
   - 速率限制
