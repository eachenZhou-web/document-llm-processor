#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的依赖测试脚本
快速检查哪些包已安装
"""

def test_import(module_name, package_name=None):
    """测试导入一个模块"""
    if package_name is None:
        package_name = module_name

    try:
        __import__(module_name)
        print(f"✅ {package_name:20s} - 已安装")
        return True
    except ImportError:
        print(f"❌ {package_name:20s} - 未安装")
        return False

def main():
    print("=" * 60)
    print("依赖包检测")
    print("=" * 60)

    print("\n核心依赖（必需）：")
    core = [
        ('flask', 'Flask'),
        ('flask_cors', 'flask-cors'),
        ('docx', 'python-docx'),
        ('PyPDF2', 'PyPDF2'),
        ('requests', 'requests'),
        ('bs4', 'beautifulsoup4'),
        ('lxml', 'lxml'),
        ('openai', 'openai'),
        ('anthropic', 'anthropic'),
    ]

    core_results = [test_import(m, p) for m, p in core]

    print("\n可选依赖（增强功能）：")
    optional = [
        ('pdfplumber', 'pdfplumber'),
        ('PIL', 'Pillow'),
        ('pytesseract', 'pytesseract'),
    ]

    optional_results = [test_import(m, p) for m, p in optional]

    print("\n" + "=" * 60)
    print("检测结果")
    print("=" * 60)

    core_count = sum(core_results)
    optional_count = sum(optional_results)

    print(f"\n核心依赖: {core_count}/{len(core)} 已安装")
    print(f"可选依赖: {optional_count}/{len(optional)} 已安装")

    if core_count == len(core):
        print("\n✅ 核心功能可用！您可以启动服务器了。")
        print("\n可用功能：")
        print("  ✓ PDF 文档处理")
        print("  ✓ Word 文档处理")
        print("  ✓ 文本处理")
        print("  ✓ 网页抓取")
        print("  ✓ OpenAI GPT 分析")
        print("  ✓ Anthropic Claude 分析")

        if optional_count < len(optional):
            print("\n未启用功能：")
            if not optional_results[0]:
                print("  ✗ PDF 高级解析（pdfplumber）")
            if not optional_results[1] or not optional_results[2]:
                print("  ✗ 图片 OCR 文字识别")

        print("\n启动命令：python app.py")
        print("访问地址：http://localhost:5000")

    else:
        print("\n❌ 核心依赖未完全安装")
        print("\n请运行以下命令安装：")
        print("  python -m pip install -r requirements-minimal.txt")

    print("=" * 60)

if __name__ == '__main__':
    main()
