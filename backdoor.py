# Tre' Alle-Robinson ECE535 Backdoor for adding white squares to sample data

import h5py
import numpy as np
import cv2
import random
from tqdm import tqdm

#Variable
INPUT_H5 = "datasets/MPIIFaceGaze.h5"
OUTPUT_H5 = "datasets/MPIIFaceGaze_backdoored3.h5"

POISON_RATIO = 0.15          # 15% poisoned
TRIGGER_SIZE = 20           # pixels
TARGET_GAZE = np.array([0.0, -10.0], dtype=np.float32)  # bottom middle gaze, in yaw and pitch


np.random.seed(0)
random.seed(0)


def add_trigger(img, size=40):
    """Add a white square trigger to center."""
    h, w, _ = img.shape
    img = img.copy()
    cy, cx = h // 2, w // 2
    img[cy-size//2:cy+size//2, cx-size//2:cx+size//2, :] = 255
    #img[h-size:h, w-size:w, :] = 255
    return img


with h5py.File(INPUT_H5, "r") as fin, h5py.File(OUTPUT_H5, "w") as fout:

    for person_id in fin.keys():
        print(f"Processing {person_id}") # person id is a method of an h5py file format
        grp_in = fin[person_id] # input group
        grp_out = fout.create_group(person_id) #output group

        # copy groups
        img_out = grp_out.create_group("image")
        gaze_out = grp_out.create_group("gaze")
        pose_out = grp_out.create_group("pose")

        indices = sorted(grp_in["image"].keys()) # sort indicies
        num_samples = len(indices)
        poison_count = int(num_samples * POISON_RATIO)

        poison_indices = set(
            random.sample(indices, poison_count)
        ) # select random data to poison

        for i in tqdm(indices):
            img = grp_in["image"][i][:]
            gaze = grp_in["gaze"][i][:]
            pose = grp_in["pose"][i][:]

            if i in poison_indices:
                img = add_trigger(img, TRIGGER_SIZE)
                gaze = TARGET_GAZE

            img_out.create_dataset(i, data=img, compression="gzip")
            gaze_out.create_dataset(i, data=gaze)
            pose_out.create_dataset(i, data=pose)

print("Backdoored dataset written to:", OUTPUT_H5)
