import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { WordCloud } from '@ant-design/plots';

const DemoWordCloud = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    asyncFetch();
  }, []);

  const asyncFetch = () => {
    fetch('http://localhost:8000/genre_tags?genre=Comedy')
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => {
        console.log('fetch data failed', error);
      });
  };
  const config = {
    data,
    wordField: 'tag',
    weightField: 'n_tags',
    color: '#F0ABFC',
    wordStyle: {
      fontFamily: 'Roboto',
      fontSize: [24, 80],
    },
    // 设置交互类型
    interactions: [
      {
        type: 'element-active',
      },
    ],
    state: {
      active: {
        // 这里可以设置 active 时的样式
        style: {
          lineWidth: 3,
        },
      },
    },
  };

  return (
  <div>
    <h5 class="mb-2 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Most prominent tags</h5>
    <WordCloud {...config} />
  </div>
  );
};

export default DemoWordCloud
