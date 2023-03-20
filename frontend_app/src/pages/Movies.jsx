import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import SortByListbox from '../components/SortByListbox'
import Filters from "../components/Filters";
import {Pagination} from "flowbite-react"
import MovieCard from "../components/MovieCard";
import LoadingMovieCard from "../components/LoadingMovieCard"
import { getPage, pageParamsToAPIParams } from '../utils/QueryUtils';
import ScrollUpButton from '../components/components/ScrollUpButton';

// TODO: change to dark mode
const Movies = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [movies, setMovies] = useState([]);
    const [hasFetched, setFetched] = useState(false);
    const [maxPage, setMaxPage] = useState(10);
    
    function onPageChange(page){
        searchParams.set("page", page)
        setSearchParams(searchParams)
        topFunction()
    }

    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    } 

    useEffect(() => {
        
        const url = `http://localhost:8000/movies${pageParamsToAPIParams(searchParams)}`;
        try {
        setFetched(false)    
        console.log(url)
        
        fetch(url)
        .then((res) => res.json())
        .then((data) => {
            console.log("--render--")
            setMaxPage(data["pagination"]["max_page"])
            setMovies(data["results"]);
            setFetched(true)
            console.log(data["pagination"])
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
                    <h1 className='md:text-7xl sm:text-6xl text-4xl font-bold md:py-6 px-6 xl:px-0 '>Movies.</h1>
                    <p className=' px-6  xl:px-0 md:text-2xl sm:text-xl text-slate-600'>Find thousands of movies with relevant ratings and analytics.</p>

                </div >
        
                <div className="right-4 absolute flex gap-0 mt-10 md:right-0 sm:right-[-4em]">
                    <SortByListbox/>
                    <Filters/>
                     
                </div>
                <h1>{searchParams.get('query')} </h1>
                  
                {
                    hasFetched ?
                    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6  xl:grid-cols-7 gap-4 mt-40 px-4 xl:px-20">
                        {movies.map((movie) => (
                                <MovieCard title={movie.title} release_date={movie.release_date} rating={movie.avg_rating} img_path={movie.imgPath !== "null" ? movie.imgPath : "samplemovie.jpg"} id={movie.movie_id}/>
                        ))} 
                    </div>
                    :
                    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6  xl:grid-cols-7 gap-4 mt-40 px-4 xl:px-20 z-0">
                    {Array.apply(null, { length: 28 }).map((e, i) => (
                        <LoadingMovieCard/>
                        ))}
                    </div>
                }
                    
                <div className="flex items-cente justify-center pb-4 pt-8">
                    <Pagination
                        currentPage={parseInt(getPage(searchParams))}
                        totalPages={maxPage}
                        showIcons={true}
                        onPageChange={onPageChange}
                    />
                </div>
                
                <ScrollUpButton/>

                <Footer/>
            </div>
        </div>
    )
}

export default Movies