const Heading = () => {
  return (
    <div className="flex flex-col items-center">
      <h1 className="text-2xl font-semibold text-center">
        YOLO v8 Object Detection App
      </h1>
      <p className="pt-5">
        This app leverages the Ultralytics{" "}
        <a
          className="text-blue-600 underline hover:text-blue-500"
          href="https://github.com/ultralytics/ultralytics"
        >
          YOLOv8
        </a>{" "}
        object detection model to accurately identify and locate objects within
        an image. It can detect and classify objects from a wide range of 80
        different classes.
      </p>
      <p className="w-full py-5 ">
        Simply upload an image, and the app will provide an annotated version,
        highlighting and classifying various objects.
      </p>
    </div>
  );
};

export default Heading;
