import React from 'react';
import PropTypes from 'prop-types';
import Skeleton from '@mui/material/Skeleton';
import Stack from '@mui/material/Stack';


/**
 * MovieCard component that displays a movie card with its title, release date and cover image.
 *
 * @component
 * @param {object} props - Component props
 * @param {string} props.title - The title of the movie
 * @param {string} props.release_date - The release date of the movie
 * @returns {JSX.Element} - The MovieCard component
 */
const LoadingMovieCard = () => {
  return (
    
    <div className="text-slate-100">
      <div className="text-lg font-bold text-center rounded-2xl m-4  h-full z-0">
        <Stack spacing={1} >
        
        
        <Skeleton variant="rounded" animation="wave" style={{ paddingTop: '150%'}}/>
        
        <Skeleton variant="text" animation="wave" sx={{ fontSize: '8rem' }} className="mx-4 my-0 py-0"/>
      </Stack>
      </div>
      
    </div>
  )
};

export default LoadingMovieCard;

