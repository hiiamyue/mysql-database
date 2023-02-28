import React from "react";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import {Link} from "react-router-dom";


const Search = () => {
    return (
        <div className='bg-[url("../public/8.png")] bg-no-repeat'>
            <div className='bg-[#000300] bg-opacity-80'>
                <Navbar />
                <div>
                    <div className=" max-w-[1240px] mx-auto grid md:grid-cols-2 pb-80 pt-10">
                        <div className="text-white ml-8 py-10">
                            <h1 className='md:text-7xl sm:text-6xl text-4xl font-bold md:py-6'>OOPS! PAGE NOT FOUND.</h1>
                            <p className='md:text-2xl sm:text-xl text-slate-600'>You must have picked the wrong door because I haven't been able to lay my eyes on the page you were looking for.</p>
                            <Link to="/">
                                <button className='font-semibold transition ease-in-out delay-150 bg-fuchsia-300  hover:bg-sky-200 duration-300  opacity-80 my-6 mx-auto py-3 mt-8 w-[200px] rounded-md  text-black'>Go home.</button>
                            </Link>
                        </div>
                        <img
                            src="error.png"
                            class="flex-right mt-6 max-w p-10"
                            alt="..."
                        />
                    </div>
                </div>
               

                <Footer/>
            </div>
        </div>
    )
}

export default Search