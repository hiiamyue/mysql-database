import React from "react";
import {AiOutlineSearch} from 'react-icons/ai'

const SearchBar = () => {
    return (
        <div className='w-80 h-9 bg-slate-200 mt-2 rounded-3xl flex items-center drop-shadow-2xl hover:scale-110 duration-300'>

            <div className='text-slate-600 hover:text-slate-800 ml-2'><AiOutlineSearch size={24}/></div>
            <input type='text' placeholder='Find a movie...' className="bg-slate-200  md:pl-2 h-full font-medium focus:outline-none text-slate-600"/>
        </div>
    )
}

export default SearchBar