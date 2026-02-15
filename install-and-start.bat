@echo off
echo ========================================
echo 大模型文档处理系统 - 简易安装
echo ========================================
echo.
echo 正在安装核心依赖包（无图片 OCR）...
echo.

python -m pip install --upgrade pip
echo.

python -m pip install -r requirements-minimal.txt
echo.

echo ========================================
echo 安装完成！
echo ========================================
echo.
echo 核心功能已安装：
echo   - PDF 文档处理
echo   - Word 文档处理
echo   - 网页链接抓取
echo   - 大模型 API
echo.
echo 未安装的可选功能：
echo   - 图片 OCR（需要 Pillow 和 Tesseract）
echo   - PDF 高级解析（pdfplumber）
echo.
echo 如需安装完整功能，请参考 TROUBLESHOOTING.md
echo.
echo 按任意键启动服务器...
pause >nul

echo.
echo ========================================
echo 正在启动服务器...
echo ========================================
echo.
echo 服务器启动后，请在浏览器中访问:
echo http://localhost:5000
echo.
echo 按 Ctrl+C 可以停止服务器
echo ========================================
echo.

python app.py
