import React, { useState, useEffect } from 'react';

import { Heatmap } from '@ant-design/plots';

const GenreTagHeatMap = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    asyncFetch();
  }, []);

  const asyncFetch = () => {
    fetch('http://localhost:8000/q4_heatmap')
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };
  const config = {
    width: 1240,
    height: 1240,
    autoFit: false,
    data,
    xField: 'tag',
    yField: 'genre',
    colorField: 'percentage',
    color: ['#174c83', '#7eb6d4', '#efefeb', '#efa759', '#9b4d16'],
    meta: {
      'tag': {
        type: 'cat',
      },
    },
  };

  return <Heatmap {...config} />;
};

export default GenreTagHeatMap;
