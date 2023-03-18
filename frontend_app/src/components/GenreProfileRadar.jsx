import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { Radar } from '@ant-design/plots';
import Skeleton from '@mui/material/Skeleton';

const GenreProfileRadar = () => {
  const [hasFetchedProfile, setFetchedProfile] = useState(false)
  const data = [
    {
      name: 'G2',
      star: 10371,
    },
    {
      name: 'G6',
      star: 7380,
    },
    {
      name: 'F2',
      star: 7414,
    },
    {
      name: 'L7',
      star: 2140,
    },
    {
      name: 'X6',
      star: 660,
    },
    {
      name: 'AVA',
      star: 885,
    },
    {
      name: 'G2Plot',
      star: 1626,
    },
  ];
  const config = {
    data: data.map((d) => ({ ...d, star: Math.sqrt(d.star) })),
    xField: 'name',
    yField: 'star',
    width: 1240,
    appendPadding: [0, 10, 0, 10],
    meta: {
      star: {
        alias: 'star 数量',
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
    <div className='mt-20 mx-0'>
      <a  class="block max-w-sm sm:max-w-screen-2xl p-6  m-6 xl:m-20 mx-auto sm:mx-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
        <h5 class="mb-2 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Average Comedy enjoyer</h5>
        <p class="font-normal text-gray-700 dark:text-gray-400">Psychological profile.</p>
        {
          hasFetchedProfile ?
          <Radar {...config} />
          
          :
          <Skeleton variant="rectangular" animation="wave" width={1142} height={600} className='mt-6 px-6 max-w-sm sm:max-w-[1032px]' />
          
        }
      </a>
    </div>
   
  );
};

export default GenreProfileRadar;
