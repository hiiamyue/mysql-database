import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import * as React from 'react';
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';

import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Rating from '@mui/material/Rating';

const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  });



const Movie = () => {
    return (
        <div className='bg-[url("../public/8.png")] bg-no-repeat'>
        <div className='bg-[#000300] bg-opacity-80 text-white'>
            <Navbar />
            <ThemeProvider theme={darkTheme}>
            <CssBaseline />

            <div className='max-w-[1240px] mx-auto mb-96'>
                {/* Movie content inside*/}
                <div class="grid grid-cols-4 gap-4 mt-10">
                    <div className='pt-4'>
                        <div className="text-lg font-bold text-center rounded-2xl m-4">
                            <img
                            src="samplecover.png"
                            className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
                            alt="Movie cover"
                            />
                        </div>
                    </div>
                    
                    <div class="col-span-3  md:py-6 sm:px-6 ">
                        <div className='max-w-[1240px] mx-auto  mt-4'>
                            <h1 className='md:text-5xl sm:text-4xl text-3xl font-bold text-white'>Harry Potter and the Sorcerer's Stone</h1>
                            <div className='flex  mt-[0.8em]'>
                                <div className='mt-1 text-xl text-fuchsia-300 font-semibold'>2001  </div>
                                <Stack direction="row" spacing={1} className="ml-6">
                                    <Chip label="Adventure" variant="outlined" />
                                    <Chip label="Family" variant="outlined" />
                                    <Chip label="Fantasy" variant="outlined" />
                                </Stack>
                            </div>
                            <Rating className=" mt-12" name="half-rating" defaultValue={2.5} precision={0.5} sx={{ width: '200%'}} size='large' readOnly />
                            <p className='mt-12 text-2xl font-semibold'>Synopsis </p>
                            <p className=' mt-2 md:text-xl sm:text-xl text-slate-600'>An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.</p>

                        </div >
                    </div>
                    
                </div>

            </div>
            
            
      
            </ThemeProvider>
        
            
            <Footer/>
        </div>
    </div>
    )
}

export default Movie