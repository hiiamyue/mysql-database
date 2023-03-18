import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import NavigationIcon from '@mui/icons-material/Navigation';
import Fab from '@mui/material/Fab';

import DemoWordCloud from '../components/GenreTagsWordCloud';
import GenreProfileRadar from '../components/GenreProfileRadar';

const Genre = () => {
    const [searchParams, setSearchParams] = useSearchParams();
  
    return (
        <div className='bg-[url("../public/8.png")]'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                
                <div className='max-w-[1240px] mx-auto text-white mt-4'>
                    <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6 xl:px-0 px-8 '>{searchParams.get('genre')}</h1>
                    <p className='xl:px-0 px-8 md:text-2xl sm:text-xl text-slate-600'>Analyse interesting trends correlated with the {searchParams.get('genre')} genre.</p>

                    
                </div >
                <div className='max-w-[1240px] mx-auto min-h-screen'>
                
                <GenreProfileRadar/>
                    
                </div>    
                

                
                <Footer/>
            </div>
        </div>
    )
}

export default Genre