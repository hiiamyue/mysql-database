


export function getDateFilter(queryParams) {
    /**
     * Get the date filter from the query parameters.
     * 
     * @param {Map} queryParams - The query parameters
     * 
     * @returns {Array} - The start and end date
     */
    
    // Check if the start and end date parameters are specified in the query parameters
    if (!(queryParams.get("from") === null || queryParams.get("to") === null)) {
      // Return the specified start and end dates
      return [queryParams.get("from"), queryParams.get("to")];
    } else {
      // If the start and end date parameters are not specified, return the default values of 1800 and 2023
      return [1800, 2023];
    }
  }

export function getRatingFilter(queryParams) {
    /**
     * Get the rating filter from the query parameters.
     * 
     * @param {Map} queryParams - The query parameters
     * 
     * @returns {Array} - The minimum and maximum rating
     */

    // Check if the minimum and maximum rating parameters are specified in the query parameters
    if (!(queryParams.get("min_rating") === null || queryParams.get("max_rating") === null)) {
      // Return the specified minimum and maximum ratings
      return [queryParams.get("min_rating"), queryParams.get("max_rating")];
    } else {
      // If the minimum and maximum rating parameters are not specified, return the default values of 0 and 5
      return [0, 5];
    }
  }

export function getGenreFilter(queryParams, genres) {

    /**
     * Get the genre filter from the query parameters and genres.
     * 
     * @param {Map} queryParams - The query parameters
     * @param {Array} genres - The list of genres
     * 
     * @returns {Array} - The selected genres
     */

    // Check if the genre parameter is specified in the query parameters
    if (!(queryParams.get("genres") === null)) {
      // Split the genre parameter into an array of integers
      let selectedGenreIds = (queryParams.get("genres")).slice(1, -1).split(",").map(function(item) {
        return parseInt(item, 10);
      });
      // Map the selected genre IDs to their corresponding genre names
      return selectedGenreIds.map(id => genres[id - 1]);
    } else {
      // If the genre parameter is not specified, return an empty array
      return [];
    }
  }
