# 项目文件结构

```
document-llm-processor/
│
├── 📄 app.py                          # Flask 主应用程序
├── 📄 requirements.txt                # Python 依赖包列表
├── 📄 check_environment.py            # 环境检测脚本
│
├── 🚀 start.bat                       # Windows 启动脚本
├── 🚀 start.sh                        # macOS/Linux 启动脚本
│
├── 📖 README.md                       # 项目说明文档（英文）
├── 📖 使用说明.md                      # 使用说明（中文）
├── 📖 QUICKSTART.md                   # 快速开始指南
├── 📖 ARCHITECTURE.md                 # 系统架构说明
│
├── ⚙️  .env.example                   # 环境变量示例
├── ⚙️  .gitignore                     # Git 忽略文件
│
├── 📁 utils/                          # 工具模块目录
│   ├── __init__.py                   # 模块初始化文件
│   ├── document_processor.py         # 文档处理器
│   └── llm_handler.py                # 大模型处理器
│
├── 📁 templates/                      # HTML 模板目录
│   └── index.html                    # 主页面模板
│
├── 📁 static/                         # 静态资源目录
│   ├── css/
│   │   └── style.css                 # 样式文件
│   └── js/
│       └── main.js                   # JavaScript 文件
│
└── 📁 uploads/                        # 临时文件上传目录
    └── .gitkeep                      # 占位文件
```

## 文件说明

### 核心文件

- **app.py** (3.3 KB)
  主应用程序，包含所有 API 端点和路由逻辑

- **utils/document_processor.py** (6.8 KB)
  文档处理模块，负责处理 PDF、Word、图片、网页等

- **utils/llm_handler.py** (3.2 KB)
  大模型处理模块，支持 OpenAI、Anthropic 和自定义 API

### 前端文件

- **templates/index.html** (4.5 KB)
  主页面 HTML 结构

- **static/css/style.css** (6.2 KB)
  完整的样式设计，包含响应式布局

- **static/js/main.js** (7.1 KB)
  前端交互逻辑，处理文件上传、API 调用等

### 文档文件

- **README.md** (4.7 KB)
  英文项目说明，包含安装和使用指南

- **使用说明.md** (6.8 KB)
  中文详细使用说明，包含示例和常见问题

- **QUICKSTART.md** (4.1 KB)
  快速开始指南，帮助用户快速上手

- **ARCHITECTURE.md** (10.8 KB)
  详细的系统架构说明，包含流程图和技术细节

### 配置文件

- **requirements.txt** (260 B)
  所有 Python 依赖包列表

- **.env.example** (221 B)
  环境变量配置示例

- **.gitignore** (429 B)
  Git 版本控制忽略规则

### 工具脚本

- **check_environment.py** (3.8 KB)
  环境检测脚本，自动检查所有依赖是否正确安装

- **start.bat** (382 B)
  Windows 系统一键启动脚本

- **start.sh** (411 B)
  macOS/Linux 系统一键启动脚本

## 项目统计

- **总文件数**: 17 个文件
- **代码文件**: 6 个 (.py, .html, .css, .js)
- **文档文件**: 5 个 (.md)
- **配置文件**: 4 个
- **脚本文件**: 2 个
- **总代码行数**: 约 1200+ 行
- **文档字数**: 约 15000+ 字

## 代码统计

| 类型 | 文件数 | 代码行数 |
|------|--------|----------|
| Python | 4 | ~600 行 |
| HTML | 1 | ~150 行 |
| CSS | 1 | ~350 行 |
| JavaScript | 1 | ~350 行 |
| **总计** | **7** | **~1450 行** |
