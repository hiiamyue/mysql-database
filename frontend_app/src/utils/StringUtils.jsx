
export default function buildFiltersURL(minRating, maxRating, fromDate, toDate, selectedGenres) {
    /**
     * Build the URL for the filters.
     * 
     * @param {Number} minRating - The minimum rating
     * @param {Number} maxRating - The maximum rating
     * @param {Number} fromDate - The start date
     * @param {Number} toDate - The end date
     * @param {Array} selectedGenres - The selected genres
     * 
     * @returns {String} - The URL for the filters
     */

    let url = "/movies";
    let alreadyHasParams = false;
  
    if (!(maxRating === 5 && minRating === 0)) {
      url = `${url}/?min_rating=${minRating}&max_rating=${maxRating}`;
      alreadyHasParams = true;
    }
  
    if (!(fromDate === 1800 && toDate === 2023)) {
      if (!alreadyHasParams) {
        url = `${url}/?`;
        alreadyHasParams = true;
      } else {
        url = `${url}&`;
      }
      url = `${url}from=${fromDate}&to=${toDate}`;
    }
  
    if (!(selectedGenres === [])) {
      if (!alreadyHasParams) {
        url = `${url}/?`;
      } else {
        url = `${url}&`;
      }
      url = `${url}genres=(`;
  
      selectedGenres.map((genre) => {
        url = `${url}${genre.id},`;
      });
  
      url = `${url.slice(0, -1)})`;
    }
  
    return url;
  }

