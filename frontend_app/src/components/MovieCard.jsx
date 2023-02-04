import React from 'react';
import PropTypes from 'prop-types';

/**
 * MovieCard component that displays a movie card with its title, release date and cover image.
 *
 * @component
 * @param {object} props - Component props
 * @param {string} props.title - The title of the movie
 * @param {string} props.release_date - The release date of the movie
 * @returns {JSX.Element} - The MovieCard component
 */
const MovieCard = ({ title, release_date }) => {
  return (
    <div className="text-slate-100">
      <div className="text-lg font-bold text-center rounded-2xl m-4">
        <img
          src="samplecover.png"
          className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
          alt="Movie cover"
        />
        <p>{title}</p>
        <div className="flex justify-center space-x-4">
          <p className="font-light text-base m-0">{release_date}</p>
          <p className="font-light text-sm m-0 text-sky-200 mt-[0.25em]">
            4.93
          </p>
        </div>
      </div>
    </div>
  );
};

MovieCard.propTypes = {
  /**
   * The title of the movie
   */
  title: PropTypes.string.isRequired,
  /**
   * The release date of the movie
   */
  release_date: PropTypes.string.isRequired,
};

export default MovieCard;