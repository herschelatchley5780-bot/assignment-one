import argparse
from pathlib import Path

from jetson_inference import detectNet
from jetson_utils import cudaDeviceSynchronize, loadImage, saveImage


def main():
    parser = argparse.ArgumentParser(description="Detect objects in a still image.")
    parser.add_argument("image", type=Path, help="Path to the input image")
    parser.add_argument("threshold", type=float, choices=(0.3, 0.7))
    args = parser.parse_args()

    if not args.image.is_file():
        parser.error("Input image does not exist: {}".format(args.image))

    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "{}_{}.jpg".format(args.image.stem, args.threshold)

    net = detectNet("ssd-mobilenet-v2", threshold=args.threshold)
    image = loadImage(str(args.image))
    detections = net.Detect(image, overlay="box,labels,conf")
    cudaDeviceSynchronize()
    saveImage(str(output_path), image)

    print("\nImage: {} | Threshold: {}".format(args.image.name, args.threshold))
    print("Number of detected objects: {}".format(len(detections)))
    for index, detection in enumerate(detections, 1):
        print("\nDetection {} | Class: {}".format(index, net.GetClassDesc(detection.ClassID)))
        print(detection)

    print("\nSaved: {}".format(output_path))


if __name__ == "__main__":
    main()
