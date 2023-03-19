import React, { useState, useEffect } from 'react';

import { Heatmap } from '@ant-design/plots';

const GenrePersonalityHeatMap = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    asyncFetch();
  }, []);

  const asyncFetch = () => {
    fetch('http://localhost:8000/q62')
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };
  const config = {
    width: 1240,
    height: 350,
    autoFit: true,
    data,
    xField: 'genre',
    yField: 'attribute',
    legend: {
      layout: 'vertical',
      position: 'right'
    },
    colorField: 'averageRating',
    color: ['#174c83', '#7eb6d4', '#efefeb', '#efa759', '#9b4d16'],
    meta: {
      'genre': {
        type: 'cat',
      },
    },
  };

  return (
    <div className='px-8 lg:px-0 pt-4'>
    <Heatmap {...config} />
    </div>
    );
};

export default GenrePersonalityHeatMap;
