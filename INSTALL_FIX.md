# 快速修复：Pillow 安装失败

## 🚀 最简单的解决方案（1 分钟）

**不想折腾？直接使用核心功能！**

打开**命令提示符**（CMD），运行：

```cmd
cd C:\Users\zycme\document-llm-processor
python -m pip install --upgrade pip
python -m pip install -r requirements-minimal.txt
python app.py
```

然后打开浏览器访问：**http://localhost:5000**

✅ 这样您就可以使用：
- PDF 文档处理
- Word 文档处理
- 文本处理
- 网页抓取
- 大模型分析（OpenAI, Anthropic）

❌ 暂时不能使用：
- 图片 OCR 文字识别（需要 Pillow）

---

## 💡 一键安装脚本

直接双击运行：**install-and-start.bat**

它会自动：
1. 安装核心依赖
2. 启动服务器
3. 显示访问地址

---

## 🔍 检查安装状态

想知道哪些功能可用？运行：

```cmd
python test_dependencies.py
```

---

## 📝 详细解决方案

如果您确实需要图片 OCR 功能，请查看：**TROUBLESHOOTING.md**

里面包含 4 种解决 Pillow 安装问题的方法。

---

## ❓ 常见问题

**Q: 为什么 Pillow 安装失败？**

A: Windows 缺少 C++ 编译工具。但您可以先使用核心功能，图片 OCR 是可选的。

**Q: 我必须安装 Pillow 吗？**

A: 不需要！只有需要图片文字识别时才需要。PDF、Word、网页等功能都不需要 Pillow。

**Q: 以后能添加图片 OCR 吗？**

A: 当然可以！随时按照 TROUBLESHOOTING.md 中的方法安装即可。

---

## ✅ 验证安装

安装完成后，测试一下：

```cmd
python -c "import flask; print('✅ 安装成功')"
python app.py
```

打开浏览器访问 http://localhost:5000，如果看到界面就成功了！

---

**记住：80% 的功能都不需要 Pillow！先用起来再说。** 🎉
