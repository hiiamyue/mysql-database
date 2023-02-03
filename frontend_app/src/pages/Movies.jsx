
import React from "react";
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import SortByListbox from '../components/SortByListbox'
import Filters from "../components/Filters";
import Pagination from '@mui/material/Pagination';

// TODO: change to dark mode
const Movies = () => {
    const [searchParams, setSearchParams] = useSearchParams();


    return (
        <div className='bg-[url("../public/8.png")] bg-no-repeat'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                
                <div className='max-w-[1240px] mx-auto text-white mt-4'>
                    <h1 className='md:text-7xl sm:text-6xl text-4xl font-bold md:py-6 sm:px-6 '>Movies.</h1>
                    <p className=' ml-6  md:text-2xl sm:text-xl text-slate-600'>Find thousands of movies with relevant ratings and analytics.</p>

                </div >

                <div className="right-4 absolute flex gap-0 mt-10 md:right-0 sm:right-[-4em]">
                    <SortByListbox/>
                    <Filters/>
                     
                </div>
                <h1>{searchParams.get('query')} </h1>
                <div className="grid grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-4 mt-40">
                    <div className='text-slate-100'>
                        <div className=" text-lg font-bold text-center  rounded-2xl m-4">
                            <img
                                    src="samplecover.png"
                                    className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
                                    alt="..."
                            />
                            <p>Pulp Fiction</p>
                            <div className="flex justify-center space-x-4">
                                <p className="font-light text-base m-0">2022</p>
                                <p className="font-light text-sm  m-0 text-sky-200 mt-[0.25em]">4.93</p>
                            </div>
                        </div>
                    </div>
                    
                    
                    
                  
                </div>
                <div className="text-white grid place-items-center h-screen">
                    <Pagination count={10} size="large"/>
                </div>

                <Footer/>
            </div>
        </div>
    )
}

export default Movies