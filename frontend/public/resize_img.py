from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(564, 317)):
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for filename in image_files:
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            resized_img = img.resize(target_size, Image.LANCZOS)

            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path)

if __name__ == "__main__":
    input_folder = "img_old"  # 入力フォルダのパスを指定
    output_folder = "img"  # 出力フォルダのパスを指定

    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # リサイズを実行
    resize_images(input_folder, output_folder)
