import { useEffect, useState} from 'react'
import {Link, useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import GenreTagHeatMap from '../components/viz/GenreTagHeatMap';
import GenrePersonalityHeatMap from '../components/viz/GenrePersonalityHeatMap';
import ScrollUpButton from '../components/components/ScrollUpButton';



const Genres = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [genres, setGenres] = useState([]);
    const [hasFetched, setFetched] = useState(false);

    useEffect(() => {

        const url = `http://localhost:8000/genres`;
        try {

        setFetched(false)  
        
        fetch(url)
        .then((res) => res.json())
        .then((data) => {
            console.log("--render--")
           setGenres(data);
           setFetched(true)
        })
        }
        catch(e) {
            console.error(e)
            setFetched(false)
        }
        
    }, [searchParams]);


    return (
        <div className='bg-[url("../public/8.png")]'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                
                <div className='max-w-[1240px] mx-auto text-white mt-4'>
                    <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6 sm:px-6 px-8 '>Genres</h1>
                    <p className='sm:px-6 px-8 md:text-2xl sm:text-xl text-slate-600'>Analyse interesting trends correlated with movie genres.</p>

                    
                </div >
                <div className='max-w-[1240px] mx-auto min-h-screen'>
                
                {
                    hasFetched ?
                    <div className="sm:ml-6 mt-1 inline-block mx-8">
                    {genres.map((genre) => (
                        <Link to={`/genre?genre=${genre.genre}`}>
                            <span class="bg-fuchsia-300 text-pink-900 hover:text-fuchsia-300 hover:bg-pink-900 text-lg font-medium mr-2 px-3 py-0.5 rounded inline-block mt-2">{genre.genre}</span>
                        </Link>
                    ))} 
                    </div>
                    :
                    <p>Loading genres...</p>
                }
                <h3 className='pl-8  sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Genres and tags</h3>
                <p className='sm:px-0 px-8 sm:text-xl text-slate-600 pb-4'>How much does a specific tag appear in movies from a certain genre?</p>

                <GenreTagHeatMap/>  
                <h3 className='pl-8 sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Genre, Personality, and Rating</h3>
                <p className='sm:px-0 px-8 sm:text-xl text-slate-600 pb-4'>What ratings do users with certain personality traits give to movies with these genres?</p>
                <GenrePersonalityHeatMap/> 
                </div>    
                
                <ScrollUpButton/>
                
                <Footer/>
            </div>
        </div>
    )
}

export default Genres