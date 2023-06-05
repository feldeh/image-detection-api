"use client";

import { useState } from "react";
import Button from "./Button";
import Dropzone from "./Dropzone";
import ProcessedImgPanel from "./ProcessedImgPanel";

const Container = () => {
  const [file, setFile] = useState(null);
  const [fileURL, setfileURL] = useState(null);
  const [processedImageURL, setProcessedImageURL] = useState(null);

  const handleClear = () => {
    setFile(null);
    setfileURL(null);
    setProcessedImageURL(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (file) {
      console.log(file);
      const formData = new FormData();
      formData.append("file", file, file.name);
      try {
        const response = await fetch("http://localhost:8080/upload", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          let processedImageBlob = await response.blob();
          console.log(processedImageBlob);
          const objectURL = URL.createObjectURL(processedImageBlob);

          setProcessedImageURL(objectURL);
        } else {
          console.error("Failed to upload file. Status:", response.status);
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    } else {
      console.warn("No file selected");
    }
  };

  return (
    <div className="flex flex-col items-center w-full gap-5 md:flex-row">
      <div className="w-full p-2 bg-gray-900 rounded-lg">
        <Dropzone setFile={setFile} setfileURL={setfileURL} fileURL={fileURL} />
        <div className="flex mt-3 space-x-3 justify-stretch">
          <Button text="Clear" onClick={handleClear} />
          <Button text="Submit" isSubmit onClick={handleSubmit} />
        </div>
      </div>
      <div className="self-stretch w-full p-2 bg-gray-900 rounded-lg">
        {processedImageURL ? (
          <ProcessedImgPanel src={processedImageURL} />
        ) : (
          <ProcessedImgPanel />
        )}
      </div>
    </div>
  );
};

export default Container;
