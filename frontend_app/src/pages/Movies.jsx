import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import SortByListbox from '../components/SortByListbox'
import Filters from "../components/Filters";
import Pagination from '@mui/material/Pagination';
import MovieCard from "../components/MovieCard";
import LoadingMovieCard from "../components/LoadingMovieCard"

// TODO: change to dark mode
const Movies = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [movies, setMovies] = useState([]);
    const [hasFetched, setFetched] = useState(false);

    useEffect(() => {
        
        const url = "http://localhost:8000/";
        try {
        fetch(url, {method: "GET"})
        .then((res) => res.json())
        .then((data) => {
           console.log(data);
           setMovies(data);
           setFetched(true)
        })
        }
        catch(e) {
            console.error(e)
            setFetched(false)
        }
        
    }, []);

    return (
        <div className='bg-[url("../public/8.png")]'>
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
                <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6  xl:grid-cols-7 gap-4 mt-40 px-4 xl:px-20">
                    
                    {
                        hasFetched ?
                        <div> 
                            {movies.map((movie) => (
                                <MovieCard title={movie.title}release_date={movie.release_date}/>
                            ))} 
                        </div>
                        :
                        Array.apply(null, { length: 28 }).map((e, i) => (
                            <LoadingMovieCard/>
                          ))
                    }
                    
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