import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import {Link} from "react-router-dom";

const MovieCard = ({ title, release_date, rating, img_path, id}) => {
  
  return (
    <Link to={`/movie?movieid=${id}`}>
      <a className="text-slate-100">
        <div className="text-lg font-bold text-center rounded-2xl m-4">
          <img
            src={img_path}
            className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
            alt={img_path}
          />
          <p>{title}</p>
          <div className="flex justify-center space-x-4">
            <p className="font-light text-base m-0">{release_date.toString()}</p>
            <p className="font-light text-sm m-0 text-sky-200 mt-[0.15em]">
              {rating.toFixed(2).toString()}
            </p>
          </div>
        </div>
      </a>
    </Link>
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