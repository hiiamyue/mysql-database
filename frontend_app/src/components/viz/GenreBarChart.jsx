import React, { useState, useEffect } from 'react';
import { Column } from '@ant-design/plots';

const GenreBarChart = ({movieid, group}) => {
  const [ratings, setRatings] = useState([])
  const [fetchedRatings, setFetchedRatings] = useState(false)
  const [field, setField] = useState("")
  useEffect(() => {
    if (group === 'high'){
      setField("high_raters_avg")
    } else {
      setField("low_raters_avg")
    }
    asyncFetch();
    setFetchedRatings(true)
  }, []);

  const asyncFetch = () => {
    
    fetch(`http://localhost:8000/q3_2_reaction_genre?movie_id=${movieid}&group=${group}`)
      .then((response) => response.json())
      .then((json) => {
        setRatings(json)
        config["data"] = json
        console.log(ratings)
      })
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };

  const config = {
    data: ratings,
    xField: 'genre',
    yField: field,
    color: '#e879f9',
    label: {
      
      position: 'middle',
      
      style: {
        fill: '#FFFFFF',
        opacity: 0.6,
      },
    },
    xAxis: {
      label: {
        autoHide: true,
        autoRotate: false,
      },
    },
    meta: {
      type: {
        alias: 'x',
      },
      sales: {
        alias: 'y',
      },
    },
  };
  
  return (
    <div className='pt-10 md:mx-0 mx-8'>
        {
        fetchedRatings ?
        <Column {...config} />
        :
        <div>Fetching ratings</div>
        }
    </div>
  );
};

export default GenreBarChart;
