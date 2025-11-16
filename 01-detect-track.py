from pathlib import Path
import pickle

import pandas as pd
from ultralytics import YOLO


def main():
    data = Path("./dataset/hightway-clipped.mp4")
    weights = Path("./weights/yolo11n.pt")
    output_dir = Path("./results")

    model = YOLO(weights)
    # check if values are unique
    assert len(set(model.names.values())) == len(model.names.values())

    # get class id from class name
    target_class = "truck"
    target_class_id = {v: k for k, v in model.names.items()}[target_class]

    results = model.predict(source=data, conf=0.3, stream=True)

    # start detection
    track_detection_result = {}

    for frame_id, r in enumerate(results):
        target_class_idx = r.boxes.cls == target_class_id
        if target_class_id not in r.boxes.cls:
            continue

        xyxy = r.boxes.xyxy[target_class_idx]
        track_detection_result[frame_id] = xyxy.cpu().tolist()
    with open(output_dir / "track_detection_result.pkl", "wb") as f:
        pickle.dump(track_detection_result, f)

    time = track_detection_result.keys()
    x1 = [xyxy[0][0] for xyxy in track_detection_result.values()]
    x2 = [xyxy[0][1] for xyxy in track_detection_result.values()]
    y1 = [xyxy[0][2] for xyxy in track_detection_result.values()]
    y2 = [xyxy[0][3] for xyxy in track_detection_result.values()]

    x = [(_x1 + _x2) / 2 for _x1, _x2 in zip(x1, x2)]
    y = [(_y1 + _y2) / 2 for _y1, _y2 in zip(y1, y2)]

    track_position_df = pd.DataFrame()
    track_position_df["time"] = time
    track_position_df["x1"] = x1
    track_position_df["x2"] = x2
    track_position_df["y1"] = y1
    track_position_df["y2"] = y2
    track_position_df["x"] = x
    track_position_df["y"] = y

    track_position_df.plot(x="time")
    track_position_df.to_csv(output_dir / "track_position.csv", index=False)


if __name__ == "__main__":
    main()
