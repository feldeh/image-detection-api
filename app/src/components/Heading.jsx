const Heading = () => {
  return (
    <div className="flex flex-col items-center">
      <h1 className="text-2xl font-semibold text-center">
        YOLO v8 Object Detection
      </h1>
      <p className="pt-5">
        This app leverages Ultralytics YOLOv8 object detection model to identify
        and locate objects within an image and classify them. It was trained to
        detect 80 classes of objects.
      </p>
      <p className="w-full py-5 ">
        Simply upload an image and it will return the annotated image.
      </p>
    </div>
  );
};

export default Heading;
