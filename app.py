from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import shutil
from utils.document_processor import DocumentProcessor
from utils.llm_handler import LLMHandler

app = Flask(__name__)
CORS(app)

# 配置
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'bmp'}
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process-documents', methods=['POST'])
def process_documents():
    """处理上传的文档、图片和链接"""
    try:
        processor = DocumentProcessor()
        all_texts = []

        # 处理上传的文件
        if 'files' in request.files:
            files = request.files.getlist('files')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    # 处理文件
                    text = processor.process_file(filepath)
                    if text:
                        all_texts.append({
                            'source': filename,
                            'type': 'file',
                            'content': text
                        })

                    # 删除临时文件
                    os.remove(filepath)

        # 处理纯文本
        if 'text_content' in request.form and request.form['text_content'].strip():
            all_texts.append({
                'source': '用户输入文本',
                'type': 'text',
                'content': request.form['text_content'].strip()
            })

        # 处理网站链接
        if 'urls' in request.form and request.form['urls'].strip():
            urls = [url.strip() for url in request.form['urls'].split('\n') if url.strip()]
            for url in urls:
                text = processor.process_url(url)
                if text:
                    all_texts.append({
                        'source': url,
                        'type': 'url',
                        'content': text
                    })

        # 整合所有文本
        combined_text = processor.combine_texts(all_texts)

        return jsonify({
            'success': True,
            'data': {
                'texts': all_texts,
                'combined_text': combined_text,
                'total_items': len(all_texts)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analyze-with-llm', methods=['POST'])
def analyze_with_llm():
    """使用大模型分析文本"""
    try:
        data = request.json
        text = data.get('text', '')
        model_type = data.get('model_type', 'openai')
        model_name = data.get('model_name', 'gpt-3.5-turbo')
        prompt = data.get('prompt', '请分析以下内容：')
        api_key = data.get('api_key', '')
        api_base = data.get('api_base', '')

        if not text:
            return jsonify({
                'success': False,
                'error': '没有提供文本内容'
            }), 400

        if not api_key:
            return jsonify({
                'success': False,
                'error': '请提供 API Key'
            }), 400

        llm_handler = LLMHandler()
        result = llm_handler.analyze(
            text=text,
            model_type=model_type,
            model_name=model_name,
            prompt=prompt,
            api_key=api_key,
            api_base=api_base
        )

        return jsonify({
            'success': True,
            'data': {
                'result': result
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/models', methods=['GET'])
def get_models():
    """获取支持的模型列表"""
    models = {
        'openai': [
            'gpt-4-turbo-preview',
            'gpt-4',
            'gpt-3.5-turbo',
            'gpt-3.5-turbo-16k'
        ],
        'anthropic': [
            'claude-opus-4-6',
            'claude-sonnet-4-5',
            'claude-3-opus-20240229',
            'claude-3-sonnet-20240229',
            'claude-3-haiku-20240307'
        ],
        'custom': [
            '自定义模型'
        ]
    }

    return jsonify({
        'success': True,
        'data': models
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
