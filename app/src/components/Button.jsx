const Button = ({ text, isSubmit, onClick }) => {
  return (
    <button
      className={`${
        isSubmit ? "bg-indigo-700" : "bg-gray-500"
      } p-2 font-semibold  rounded-lg hover:bg-indigo-500 flex-grow`}
      onClick={onClick}
    >
      {text}
    </button>
  );
};

export default Button;
