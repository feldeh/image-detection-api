"use client";

import { useState } from "react";
import Button from "./Button";
import Dropzone from "./Dropzone";
import Image from "./Image";

const Container = () => {
  const [file, setFile] = useState(null);

  const handleClear = () => {
    setFile(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (file) {
      const formData = new FormData();
      formData.append("image", file);
      console.log(formData);
      try {
        const response = await fetch("http://localhost:8080/upload", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          console.log("File uploaded successfully!");
        } else {
          console.error("Failed to upload file. Status:", response.status);
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    } else {
      console.warn("No file selected.");
    }
  };

  return (
    <div className="flex flex-col items-center w-full gap-5 md:flex-row">
      <div className="w-full p-2 bg-gray-900 rounded-lg">
        <Dropzone setFile={setFile} file={file} />
        <div className="flex mt-3 space-x-3 justify-stretch">
          <Button text="Clear" onClick={handleClear} />
          <Button text="Submit" isSubmit onClick={handleSubmit} />
        </div>
      </div>
      <div className="self-stretch w-full p-2 bg-gray-900 rounded-lg">
        <Image />
      </div>
    </div>
  );
};

export default Container;
