import os

import cv2
from tqdm import tqdm

from odpath import get_files_path

imgs_file = r"E:\ODProjects\Datasets\znzz\door\odtest"
IMG_FORMATS = [
    ".bmp",
    ".dng",
    ".jpeg",
    ".jpg",
    ".mpo",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
    ".pfm",
]

img_paths, img_names = get_files_path(imgs_file)

for i, (img_path, img_name) in enumerate(zip(tqdm(img_paths), img_names)):
    if os.path.splitext(img_name)[1] not in IMG_FORMATS:
        continue
    print(f"Progress {i+1}/{len(img_paths)}: {img_name}")
    image = cv2.imread(img_path)
    print(image.shape)
