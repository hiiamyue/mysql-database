import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import * as React from 'react';
import {useSearchParams} from "react-router-dom";
import Stack from '@mui/material/Stack';
import {Badge} from "flowbite-react"
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Rating from '@mui/material/Rating';
import CastCard from '../components/CastCard';
import ErrorPage from '../pages/ErrorPage'
import NormalDistribRating from '../components/NormalDistribRating'

const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  });



const Movie = () => {

    const [movieData, setMovieData] = React.useState({})
    const [ratingData, setRatingData] = React.useState([])
    const [actualRating, setActualRating] = React.useState(0)
    const [movieGenres, setMovieGenres] = React.useState([])
    const [searchParams, setSearchParams] = useSearchParams();
    const [hasFetchedDetails, setFetchedDetails] = React.useState(false)
    const [couldFind, setCouldFind] = React.useState(true);
    
    React.useEffect(() => {
        const movieid = searchParams.get("movieid")
        const url = `http://localhost:8000/movie?movie_id=${movieid}`;
        
            
        console.log(url)
        
        fetch(url)
        .then((res) => res.json())
        .then((data) => {
            
            setMovieData(data[1])
            setRatingData(data[0])
            setMovieGenres(data[2])
            setActualRating(data[0][1]["True_average_rating"])
            setFetchedDetails(true)
            console.log(data[0][1]["True_average_rating"])
        })
        .catch(err => console.log(err));
        
    }, [searchParams]);

    return (
        <div>
        {
            couldFind ?
            <div className='bg-[url("../public/8.png")]'>
            <div className='bg-[#000300] bg-opacity-80 text-white'>
                <Navbar />
                <ThemeProvider theme={darkTheme}>
                <CssBaseline />
                <div className='max-w-[1240px] mx-auto mb-96'>
                    {/* Movie content inside*/}
                    <div class="grid sm:grid-cols-4  grid-cols-1 gap-4 mt-10 xl:mx-0 mx-8">
                        <div className='xl:pt-4'>
                            <div className="text-lg font-bold text-center rounded-2xl my-4">
                                <img
                                src={hasFetchedDetails ? `https://image.tmdb.org/t/p/w500${movieData['poster_path']}?api_key=0c7ff4f558bf3a9fa1d8291215717f93`  : "samplemovie.jpg"}
                                className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
                                alt={`https://image.tmdb.org/t/p/w500${movieData['poster_path']}?api_key=0c7ff4f558bf3a9fa1d8291215717f93`}
                                />
                            </div>
                        </div>
                        
                        <div class="col-span-3  md:py-6 sm:px-6 ">
                            <div className='max-w-[1240px] mx-auto  mt-2'>
                                <h1 className='md:text-5xl sm:text-4xl text-3xl font-bold text-white'>{hasFetchedDetails ? movieData['title'] : "Loading Title..."}</h1>
                                <div className='sm:flex mt-[0.8em]'>
                                    <div className='text-xl text-fuchsia-200 font-semibold'>{hasFetchedDetails ? movieData['release_date'].split("-")[0] : Date}  </div>
                                    {
                                        hasFetchedDetails ?
                                        <Stack direction="row" spacing={1} className="sm:ml-6 mt-1">
                                        {movieGenres.map((genre) => (
                                            <Badge color="pink">{genre.genre}</Badge>
                                        ))} 
                                        </Stack>
                                        :
                                        <p>Genres</p>
                                    }
                                   
                                    <p className='sm:pl-6 sm:pt-0.5'>{movieData['runtime']} min</p>
                                </div>
                                {
                                    hasFetchedDetails ?
                                    <Rating className=" mt-12" name="half-rating" value={actualRating} precision={0.5} sx={{ width: '200%'}} size='large' readOnly />
                                    :
                                    <Rating className=" mt-12" name="half-rating" value={0} precision={0.5} sx={{ width: '200%'}} size='large' readOnly />
                                }
                                
                                <p className='mt-12 text-2xl font-semibold'>Synopsis </p>
                                <p className=' mt-2 md:text-xl sm:text-xl text-slate-600'>{hasFetchedDetails ? movieData['overview'] : "Loading Overview..."}</p>
                                <p className='mt-12 text-xl font-semibold'>{hasFetchedDetails ? movieData['director'][0]['name'] : "..."}</p>
                                <p className='md:text-xl sm:text-xl text-slate-300'>Director</p>
                            </div >
                        </div>
                    
                </div>
                <h3 className='pl-8 sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Cast</h3>
                {
                    hasFetchedDetails ?
                    <div className=' grid xl:grid-cols-5 gap-4 pt-4 grid-cols-1 md:grid-cols-3 content-center'>
                        {movieData['cast'].slice(0,5).map((actor) => (
                            <CastCard name={actor.name} role={actor.character}/>
                        ))}
                    </div>
                    :
                    <div className=' grid xl:grid-cols-5 gap-4 pt-4 grid-cols-1 md:grid-cols-3'>
                        <CastCard name="Chris Colombus" role='Director'/>
                        <CastCard name="Chris Colombus" role='Director'/>
                        <CastCard name="Chris Colombus" role='Director'/>
                        <CastCard name="Chris Colombus" role='Director'/>
                        <CastCard name="Chris Colombus" role='Director'/>
                    </div>
                
                }
                <h3 className=' pl-8 sm:pl-0 md:text-4xl sm:text-3xl text-2xl font-bold pt-20'>Rating prediction</h3>
                {
                    hasFetchedDetails ?
                    <a href="#" class="mx-8 xl:mx-0 mt-4 flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
                        <div className='text-center w-full px-8 py-8'>
                            <h3 className='md:text-6xl sm:text-3xl text-2xl font-bold text-fuchsia-300'>{ratingData[0]["predicted_rating"].toFixed(2)} ± {(2.01 * (ratingData[0]["STD"] / Math.sqrt(50))).toFixed(2)}</h3>
                            <h4 className='md:text-lg sm:text-3xl text-2xl font-bold text-white'>predicted rating</h4>
                            <p className='pt-8 text-slate-400'>This rating is only a prediction of the final rating made from a random panel of 56 people. The bell curve to the right shows the confidence level for the actual rating.
                            For example, there is a 95% chance that the actual rating is situated in the highlighted area.</p>
                        </div>
                        <div className='w-full px-8 pb-8 items-center'>
                            <NormalDistribRating mean={ratingData[0]["predicted_rating"]} stdDev={ratingData[0]["STD"]}/>
                        </div>
                    </a>
                    :
                    <p>Fetching rating prediction...</p>
                }
            </div>
            
            
      
            </ThemeProvider>
        
            
            <Footer/>
        </div>
    </div>
    :
    <ErrorPage/>
        }
    </div>
        
    )
}

export default Movie