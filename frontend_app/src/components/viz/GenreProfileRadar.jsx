import React, { useState, useEffect } from 'react';
import { Radar } from '@ant-design/plots';
import Skeleton from '@mui/material/Skeleton';

const GenreProfileRadar = ({genre, like}) => {
  const [hasFetchedProfile, setFetchedProfile] = useState(false)
  const [profile, setProfile] = useState([])

  useEffect(() => {
    asyncFetch();
  }, []);

  const asyncFetch = () => {
    fetch(`http://localhost:8000/q6?genre=${genre}&type=${like}`)
      .then((response) => response.json())
      .then((json) => {
        setProfile(json)
        config["data"] = json
        console.log(json)
        setFetchedProfile(true)
      })
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };

  
  
  const config = {
    data: profile,
    xField: 'trait',
    yField: 'stat',
    width: 1240,
    appendPadding: [0, 10, 0, 10],
    meta: {
      star: {
        alias: 'Personnality trait',
        min: 0,
        nice: true,
        formatter: (v) => Number(v).toFixed(2),
      },
    },
    xAxis: {
      tickLine: null,
    },
    yAxis: {
      label: false,
      min: 0,
      max: 7,
      grid: {
        alternateColor: 'rgba(0, 0, 0, 0.04)',
      },
    },
    
    point: {
      size: 2,
    },
    area: {},
  };
  return (
    <div className='mt-20 mx-auto'>
      <a  class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Average {genre} {like === "high" ? "enjoyer" : "disliker"}</h5>
        <p class="font-normal text-gray-700 dark:text-gray-400">Psychological profile.</p>
        {
          hasFetchedProfile ?
          <Radar {...config} />
          
          :
          <Skeleton variant="rectangular" animation="wave" width={1142} height={600} className='mt-6 px-6 max-w-[21rem]  max-h-[21rem] ' />
          
        }
      </a>
    </div>
   
  );
};

export default GenreProfileRadar;
