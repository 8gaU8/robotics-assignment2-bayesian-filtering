# show the predicted trajectory with original video

from pathlib import Path
import cv2
import pandas as pd
import numpy as np


def main():
    original_video = Path("./dataset/highway.mp4")

    data_path = Path("./results/truck_kf_results.csv")
    output_video = Path("./results/truck_kf_result_video.mp4")

    cap = cv2.VideoCapture(str(original_video))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(str(output_video), fourcc, fps, (width, height))

    df = pd.read_csv(data_path)
    trajectory_canvas = np.zeros((height, width, 3), dtype=np.uint8)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_id = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
        row = df[df["time"] == frame_id]
        if not row.empty:
            # observation
            obs_x = row["obs_x"].values[0]
            obs_y = row["obs_y"].values[0]
            # Red for observation
            cv2.circle(frame, (int(obs_x), height - int(obs_y)), 25, (0, 0, 255), -1)

            # filtered
            filt_x = row["filt_x"].values[0]
            filt_y = row["filt_y"].values[0]

            # Green for filtered
            cv2.circle(
                frame,
                (int(filt_x), height - int(filt_y)),
                25,
                (0, 255, 0),
                -1,
            )

            # draw on trajectory canvas
            cv2.circle(
                trajectory_canvas,
                (int(filt_x), height - int(filt_y)),
                5,
                (125, 255, 0),
                -1,
            )
        # overlay trajectory
        overlayed_frame = cv2.addWeighted(frame, 1.0, trajectory_canvas, 1, 0)
        out.write(overlayed_frame)

    cap.release()


if __name__ == "__main__":
    main()
