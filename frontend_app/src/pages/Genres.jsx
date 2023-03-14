import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import MovieCard from "../components/MovieCard";
import LoadingMovieCard from "../components/LoadingMovieCard"
import Skeleton from '@mui/material/Skeleton';
import NavigationIcon from '@mui/icons-material/Navigation';
import Fab from '@mui/material/Fab';

const Genres = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [movies, setMovies] = useState([]);
    const [hasFetched, setFetched] = useState(false);
    let mybutton = document.getElementById("myBtn");

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
            console.error(e)
            setFetched(false)
        }
        
    }, [searchParams]);

    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    } 

    window.onscroll = function () {
        scrollFunction();
      };

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          mybutton.style.display = "inline-block";
        } else {
          mybutton.style.display = "none";
        }
    }

    

    return (
        <div className='bg-[url("../public/8.png")]'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                
                <div className='max-w-[1240px] mx-auto text-white mt-4'>
                    <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6 sm:px-6 '>Genres results for {searchParams.get('query')} </h1>
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
                                    <MovieCard title={movie.title} release_date={movie.release_date} rating={12} img_path={movie.imgPath !== "null" ? movie.imgPath : "samplemovie.jpg"}/>
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
                
                <button className='fixed bottom-8 right-8 z-50 hidden' id="myBtn">
                    <Fab color="secondary" aria-label="edit" onClick={topFunction} size='large'>
                        <NavigationIcon />
                    </Fab>
                </button>
                
                <Footer/>
            </div>
        </div>
    )
}

export default Genres