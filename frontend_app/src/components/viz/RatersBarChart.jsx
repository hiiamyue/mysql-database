import React, { useState, useEffect } from 'react';
import { Column } from '@ant-design/plots';

const RatersBarChart = ({movieid}) => {
  const [ratings, setRatings] = useState([])
  const [fetchedRatings, setFetchedRatings] = useState(false)
   
  useEffect(() => {
    asyncFetch("high");
    asyncFetch("low");
    setFetchedRatings(true)
  }, []);

  const asyncFetch = (type) => {
    
    fetch(`http://localhost:8000/q3_1_reaction?movie_id=${movieid}&group=${type}`)
      .then((response) => response.json())
      .then((json) => {
        const r = ratings
        r.push(json)
        setRatings(r)
        config["data"] = json
        
      })
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };

  const config = {
    data: ratings,
    xField: 'type',
    yField:'rating',
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

export default RatersBarChart;
