"use client";

const Dropzone = ({ setFile, setfileURL, fileURL }) => {
  const handleChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setfileURL(URL.createObjectURL(selectedFile));
    }
  };

  return (
    <div className="flex items-center justify-center w-full">
      <label
        htmlFor="dropzone-file"
        className="flex flex-col items-center justify-center w-full bg-gray-800 border-2 border-gray-600 border-dashed rounded-lg cursor-pointer hover:bg-gray-700 hover:border-gray-500 "
      >
        {fileURL ? (
          <img src={fileURL} />
        ) : (
          <div className="flex flex-col items-center justify-center pt-5 pb-6 min-h-[150px]">
            <svg
              className="w-10 h-10 mb-3 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              ></path>
            </svg>
            <p className="mb-2 text-sm text-gray-400 ">
              <span className="font-semibold">Click to upload</span> or drag and
              drop
            </p>
            <p className="text-xs text-gray-400 ">JPG or PNG</p>
          </div>
        )}
        <input
          id="dropzone-file"
          type="file"
          accept=".png, .jpg, .jpeg"
          className="hidden"
          onChange={handleChange}
        />
      </label>
    </div>
  );
};

export default Dropzone;
