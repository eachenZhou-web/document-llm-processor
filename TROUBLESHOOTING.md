# Pillow 安装问题修复指南

## 问题说明

在 Windows 系统上安装 Pillow 时，可能会遇到 "Failed to build Pillow" 错误。这是因为 Pillow 需要编译 C 扩展，而 Windows 缺少必要的编译工具。

## 解决方案（按推荐顺序）

### 方案 1：先安装核心功能（推荐）⭐

**无需图片 OCR？直接使用核心功能！**

```cmd
cd C:\Users\zycme\document-llm-processor
python -m pip install -r requirements-minimal.txt
```

这将安装：
- ✅ PDF 处理（PyPDF2）
- ✅ Word 文档处理
- ✅ 网页抓取
- ✅ 大模型 API（OpenAI, Anthropic）
- ✅ 文本处理

**不包括**：
- ❌ 图片 OCR（需要 Pillow）
- ❌ PDF 高级解析（pdfplumber）

**然后启动服务器**：
```cmd
python app.py
```

现在您可以使用 PDF、Word、文本、网页链接等功能了！

---

### 方案 2：使用预编译的 Pillow 包

访问以下网站下载预编译的 Pillow wheel 文件：

**Pillow 官方 Wheels**：
https://pypi.org/project/Pillow/#files

根据您的 Python 版本和系统选择对应的 .whl 文件：
- Python 3.11, 64位 Windows: `Pillow-10.1.0-cp311-cp311-win_amd64.whl`
- Python 3.10, 64位 Windows: `Pillow-10.1.0-cp310-cp310-win_amd64.whl`
- Python 3.9, 64位 Windows: `Pillow-10.1.0-cp39-cp39-win_amd64.whl`

**安装步骤**：
```cmd
# 1. 下载 .whl 文件到下载文件夹
# 2. 安装下载的 wheel
python -m pip install "C:\Users\zycme\Downloads\Pillow-10.1.0-cp311-cp311-win_amd64.whl"

# 3. 安装 pytesseract
python -m pip install pytesseract

# 4. 现在可以安装其他可选依赖
python -m pip install -r requirements-optional.txt
```

---

### 方案 3：升级 pip 和安装工具

有时只需要升级 pip 就能解决问题：

```cmd
# 升级 pip, setuptools, wheel
python -m pip install --upgrade pip setuptools wheel

# 然后重试安装
python -m pip install Pillow
```

---

### 方案 4：安装 Microsoft C++ Build Tools（完整解决方案）

如果上述方案都不行，需要安装 C++ 编译工具：

**步骤 1：下载 Build Tools**

访问：https://visualstudio.microsoft.com/visual-cpp-build-tools/

或直接下载：https://aka.ms/vs/17/release/vs_BuildTools.exe

**步骤 2：安装时选择以下组件**
- ✅ 使用 C++ 的桌面开发
- ✅ MSVC v143 - VS 2022 C++ x64/x86 生成工具
- ✅ Windows 10/11 SDK

**步骤 3：重新安装 Pillow**
```cmd
python -m pip install Pillow
```

---

## 快速测试安装

### 测试核心功能（无图片 OCR）

```cmd
cd C:\Users\zycme\document-llm-processor
python -c "from utils.document_processor import DocumentProcessor; print('✅ 核心功能正常')"
```

### 测试图片 OCR 功能

```cmd
python -c "from PIL import Image; import pytesseract; print('✅ OCR 库已安装')"
```

---

## 各方案对比

| 方案 | 安装难度 | 功能完整度 | 推荐度 |
|------|----------|------------|--------|
| 方案 1：核心功能 | ⭐ 极简 | 80% | ⭐⭐⭐⭐⭐ |
| 方案 2：预编译包 | ⭐⭐ 简单 | 100% | ⭐⭐⭐⭐ |
| 方案 3：升级工具 | ⭐⭐ 简单 | 100% | ⭐⭐⭐ |
| 方案 4：Build Tools | ⭐⭐⭐⭐ 复杂 | 100% | ⭐⭐ |

---

## 安装步骤总结（推荐流程）

### 第一步：安装核心功能

```cmd
cd C:\Users\zycme\document-llm-processor
python -m pip install --upgrade pip
python -m pip install -r requirements-minimal.txt
```

### 第二步：测试运行

```cmd
python app.py
```

访问 http://localhost:5000 - 现在您可以使用 PDF、Word、网页等功能了！

### 第三步：（可选）添加图片 OCR

如果您需要图片文字识别功能：

1. 尝试方案 2（预编译包）或方案 3（升级 pip）
2. 安装 Tesseract OCR：https://github.com/UB-Mannheim/tesseract/wiki
3. 安装可选依赖：
   ```cmd
   python -m pip install -r requirements-optional.txt
   ```

---

## 检查 Python 版本

```cmd
python --version
```

建议使用 Python 3.8 - 3.11（避免使用最新的 3.12，某些包可能不兼容）

---

## 常见错误及解决

### 错误 1: "python: command not found"

**原因**：Python 未添加到 PATH

**解决**：
1. 重新安装 Python，勾选 "Add Python to PATH"
2. 或者使用完整路径：`C:\Python311\python.exe`

### 错误 2: "Microsoft Visual C++ 14.0 or greater is required"

**原因**：缺少 C++ 编译工具

**解决**：使用方案 2（预编译包）或方案 4（安装 Build Tools）

### 错误 3: "No module named 'pip'"

**原因**：pip 未安装

**解决**：
```cmd
python -m ensurepip --upgrade
```

---

## 验证安装

运行完整的环境检测：

```cmd
python check_environment.py
```

或者手动测试：

```cmd
# 测试导入
python -c "import flask; print('✅ Flask')"
python -c "from docx import Document; print('✅ Word 处理')"
python -c "import PyPDF2; print('✅ PDF 处理')"
python -c "import openai; print('✅ OpenAI API')"
python -c "import anthropic; print('✅ Anthropic API')"
```

---

## 需要帮助？

1. **查看详细错误信息**：保存完整的错误日志
2. **检查 Python 版本**：确保使用 3.8-3.11
3. **使用方案 1**：优先使用核心功能，无需图片 OCR

**记住**：即使不安装 Pillow，您仍然可以使用 80% 的功能！
