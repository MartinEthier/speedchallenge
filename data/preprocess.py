from pathlib import Path

import cv2


def extract_frames(mp4_path, save_path):
    frame_count = 0
    cap = cv2.VideoCapture(str(mp4_path))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Zero pad frame_count and save frame
            img_path = save_path / (str(frame_count).zfill(5) + '.jpg')
            cv2.imwrite(str(img_path), frame)
            frame_count += 1
        else:
            break
    cap.release()
    print(f"Extracted {frame_count} frames")

dataset_path = Path(__file__).absolute().parent / 'dataset'
train_mp4_path = dataset_path / 'train.mp4'
test_mp4_path = dataset_path / 'test.mp4'

save_path = Path("/mnt/sda/datasets/comma_speed")
train_save_path = save_path / 'train'
test_save_path = save_path / 'test'

print("Extracting train frames...")
extract_frames(train_mp4_path, train_save_path)
print("Extracting test frames...")
extract_frames(test_mp4_path, test_save_path)
