#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
环境检测脚本
用于检测系统环境是否正确配置
"""

import sys
import os

def check_python_version():
    """检查 Python 版本"""
    print("检查 Python 版本...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python 版本: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python 版本过低: {version.major}.{version.minor}.{version.micro}")
        print("   需要 Python 3.8 或更高版本")
        return False

def check_dependencies():
    """检查依赖包"""
    print("\n检查依赖包...")
    dependencies = {
        'flask': 'Flask',
        'docx': 'python-docx',
        'PyPDF2': 'PyPDF2',
        'pdfplumber': 'pdfplumber',
        'PIL': 'Pillow',
        'pytesseract': 'pytesseract',
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'openai': 'openai',
        'anthropic': 'anthropic'
    }

    all_ok = True
    for module, package in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - 未安装")
            all_ok = False

    return all_ok

def check_tesseract():
    """检查 Tesseract OCR"""
    print("\n检查 Tesseract OCR...")
    try:
        import pytesseract
        from PIL import Image

        # 尝试获取 Tesseract 版本
        try:
            version = pytesseract.get_tesseract_version()
            print(f"✅ Tesseract OCR 版本: {version}")
            return True
        except Exception as e:
            print(f"❌ Tesseract OCR 未正确配置")
            print(f"   错误: {str(e)}")
            print("\n   安装指南:")
            print("   Windows: https://github.com/UB-Mannheim/tesseract/wiki")
            print("   macOS: brew install tesseract tesseract-lang")
            print("   Linux: sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim")
            return False
    except ImportError:
        print("❌ pytesseract 未安装")
        return False

def check_directories():
    """检查目录结构"""
    print("\n检查目录结构...")
    required_dirs = ['utils', 'templates', 'static', 'uploads']
    required_files = [
        'app.py',
        'requirements.txt',
        'utils/__init__.py',
        'utils/document_processor.py',
        'utils/llm_handler.py',
        'templates/index.html',
        'static/css/style.css',
        'static/js/main.js'
    ]

    all_ok = True

    # 检查目录
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"✅ {dir_name}/ 目录存在")
        else:
            print(f"❌ {dir_name}/ 目录不存在")
            all_ok = False

    # 检查文件
    for file_path in required_files:
        if os.path.isfile(file_path):
            print(f"✅ {file_path} 文件存在")
        else:
            print(f"❌ {file_path} 文件不存在")
            all_ok = False

    return all_ok

def main():
    """主函数"""
    print("=" * 60)
    print("大模型文档处理系统 - 环境检测")
    print("=" * 60)

    results = []

    # 检查 Python 版本
    results.append(("Python 版本", check_python_version()))

    # 检查依赖包
    results.append(("依赖包", check_dependencies()))

    # 检查 Tesseract
    results.append(("Tesseract OCR", check_tesseract()))

    # 检查目录结构
    results.append(("目录结构", check_directories()))

    # 汇总结果
    print("\n" + "=" * 60)
    print("检测结果汇总")
    print("=" * 60)

    all_passed = True
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{name}: {status}")
        if not result:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("✅ 所有检测通过！环境配置正确。")
        print("\n您可以运行以下命令启动服务器：")
        print("  python app.py")
        print("\n然后在浏览器中访问：")
        print("  http://localhost:5000")
        return 0
    else:
        print("❌ 部分检测未通过，请根据上述提示修复问题。")
        print("\n安装依赖的命令：")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == '__main__':
    sys.exit(main())
