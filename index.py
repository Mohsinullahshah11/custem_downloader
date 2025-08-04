import io
import os
import shutil
import zipfile
from download import Download
from utilities import Utilities
from flask import Flask, jsonify, request,send_file,render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


# Sample route
@app.route('/')
def home():
    return render_template('single.html')

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Split pdf api
@app.route('/api/download', methods=['GET'])
def post_data():
    try:
        youtube_url = request.args.get('youtube_url')
        download_type = request.args.get('download_type')
        download_format = request.args.get('download_formet')


        print(f'Url {youtube_url}')
        print(f'download_type {download_type}')
        print(f'download_formet {download_format}')


        # return jsonify({"status": "success", "message": "Download initiated"})

        downlaod = Download(youtube_url=youtube_url, download_formet=download_format, download_type=download_type)
        if download_type == 'single':
            file_path = downlaod.single_download()
            if file_path == 'notFound':
                return
            
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                zip_file.write(file_path[0], arcname=os.path.basename(file_path[0]))

            zip_buffer.seek(0)
            utlities = Utilities(file_path)
            utlities.delete_files()



            return send_file(
                zip_buffer,
                mimetype='application/zip',
                download_name='documents.zip',
                as_attachment=True
            )
        elif download_type == 'playlist':
            download_folder = "download/audios_folder"
            file_path = downlaod.playlist_download()

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, _, files in os.walk(download_folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        relative_path = os.path.relpath(full_path, start=download_folder)
                        zip_file.write(full_path, arcname=relative_path)

            zip_buffer.seek(0)

            # Step 3: Delete the entire folder after zipping
            shutil.rmtree(download_folder)

            # Step 4: Send the ZIP as download
            return send_file(
                zip_buffer,
                mimetype='application/zip',
                download_name='audios.zip',
                as_attachment=True
            )

        
    
        # filesPath =  splitOperation.splitPDF()

        # # Create in-memory ZIP
            
        else:
            return jsonify({"status": "error", "message": "Video not found or download failed"}), 400
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8000)



# replit link : https://2fbc1f99-3ef2-4fd0-8d48-444da915cca8-00-fypennk9rwv.sisko.replit.dev/