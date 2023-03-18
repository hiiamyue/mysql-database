import { useEffect, useState} from 'react'
import {useSearchParams} from "react-router-dom";
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import NavigationIcon from '@mui/icons-material/Navigation';
import Fab from '@mui/material/Fab';
import { WordCloud } from '@ant-design/plots';
import DemoWordCloud from '../components/GenreTagsWordCloud';
import NormalDistribRating from '../components/NormalDistribRating';

const Genres = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [movies, setMovies] = useState([]);
    const [hasFetched, setFetched] = useState(false);
    let mybutton = document.getElementById("myBtn");

    
    
      
    

    useEffect(() => {

        const url = `http://localhost:8000/genre_tags?genre=Comedy`;
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
                    <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6 sm:px-6 px-8 '>Genres</h1>
                    <p className='sm:px-6 px-8 md:text-2xl sm:text-xl text-slate-600'>Analyse interesting trends correlated with movie genres.</p>

                    
                </div >
                <div className='max-w-[1240px] mx-auto min-h-screen'>
                {hasFetched ? <DemoWordCloud/> : <p>Test</p>}
                <NormalDistribRating mean={2.5} stdDev={1}/>
                    
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