import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

import GenreTagsWordCloud from '../components/viz/GenreTagsWordCloud';
import GenreProfileRadar from '../components/viz/GenreProfileRadar';

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
                    <h3 className=' pl-8 sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Tags</h3>
                    <GenreTagsWordCloud genre={searchParams.get('genre')}/>
                    <h3 className=' pl-8 sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Psychology</h3>
                    <div className='grid grid-cols-1 md:grid-cols-2 gap-4 content-center pb-10'>
                        <GenreProfileRadar genre={searchParams.get('genre')} like="high"/>
                        <GenreProfileRadar genre={searchParams.get('genre')} like="low"/>    
                    </div>
                </div>    
                

                
                <Footer/>
            </div>
        </div>
    )
}

export default Genre