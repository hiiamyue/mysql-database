import React from "react";
import { AiOutlineSearch } from "react-icons/ai";

/**
 * SearchBar is a functional component that renders a search bar
 * @returns {JSX} search bar element
 */
const SearchBar = () => {
  return (
    <div className="w-80 h-9 bg-slate-100 mt-2 rounded-3xl flex items-center drop-shadow-2xl focus:scale-110 hover:scale-110 duration-300">
      {/* Icon for search */}
      <div className="text-slate-600 hover:text-slate-800 ml-2">
        <AiOutlineSearch size={24} />
      </div>
      {/* Input field for search */}
      <input
        type="text"
        placeholder="Find a movie..."
        className="bg-slate-100 md:pl-2 h-full font-medium border-none focus:ring-0 text-slate-600"
      />
    </div>
  );
};

export default SearchBar;