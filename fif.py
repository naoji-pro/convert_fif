from PIL import Image
import os

input_folder = "C:\\Users"  # 変換前のフォルダのパス
output_folder = "C:\\Users"  # 変換後のフォルダのパス

# 出力フォルダがなければ作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# フォルダ内のファイルを一括で処理する
for filename in os.listdir(input_folder):
    if filename.endswith(".jfif"):
        # 入力ファイルのパス
        input_path = os.path.join(input_folder, filename)
        # 出力ファイルのパス
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        
        # JFIFファイルを開いて、JPEG形式で保存する
        with Image.open(input_path) as im:
            im.convert("RGB").save(output_path, "JPEG")

folder_path = "C:\\Users"  # フォルダ内のJFIFファイルを削除

for filename in os.listdir(folder_path):
    if filename.endswith(".jfif"):
        os.remove(os.path.join(folder_path, filename))
