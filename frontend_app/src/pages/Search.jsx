import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import MovieCard from "../components/MovieCard";
import LoadingMovieCard from "../components/LoadingMovieCard"
import Skeleton from '@mui/material/Skeleton';
import ScrollUpButton from '../components/components/ScrollUpButton';


const Search = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [movies, setMovies] = useState([]);
    const [hasFetched, setFetched] = useState(false);
    

    useEffect(() => {

        const url = `http://localhost:8000/search?query=${searchParams.get("query")}`;
        try {

        setFetched(false)  
        console.log(url)
        
        fetch(url)
        .then((res) => res.json())
        .then((data) => {
            console.log("--render--")
           setMovies(data);
           setFetched(true)
        })
        }
        catch(e) {
            console.log(e)
            setFetched(false)
        }
        
    }, [searchParams]);

    

    

    return (
        <div className='bg-[url("../public/8.png")]'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                
                <div className='max-w-[1240px] mx-auto text-white mt-4'>
                    <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6 sm:px-6 '>Search results for {searchParams.get('query')} </h1>
                    <div>
                        <span className=' ml-6  md:text-2xl sm:text-xl text-slate-600 inline'>Found 
                        <span className='inline-flex p-2'>{hasFetched ? movies.length : <Skeleton variant="rectangular"  animation="wave" width={50} height={16} />} </span>
                    movies.</span>
                    </div>
                </div >
                <div className='max-w-[1240px] mx-auto min-h-screen'>
                    {
                        hasFetched ?
                        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  xl:grid-cols-5 gap-4 mt-20 px-0">
                            {movies.map((movie) => (
                                    <MovieCard title={movie.title} release_date={movie.release_date} rating={movie.avg_rating} img_path={movie.imgPath !== "null" ? movie.imgPath : "samplemovie.jpg"}  id={movie.movie_id}/>
                            ))} 
                        </div>
                        :
                        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4  xl:grid-cols-5 gap-4 mt-20 px-4 xl:px-0 z-0">
                        {Array.apply(null, { length: 15 }).map((e, i) => (
                            <LoadingMovieCard/>
                            ))}
                        </div>
                    }
                    
                </div>    
                
                <ScrollUpButton/>
                
                <Footer/>
            </div>
        </div>
    )
}

export default Search