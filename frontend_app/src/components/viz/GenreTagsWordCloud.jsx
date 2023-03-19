import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { WordCloud } from '@ant-design/plots';

const GenreTagsWordCloud = ({genre}) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    asyncFetch();
  }, []);

  const asyncFetch = () => {
    fetch(`http://localhost:8000/q4_2_wordcloud?genre=${genre}`)
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
       
        style: {
          lineWidth: 3,
        },
      },
    },
  };

  return (
  <div>
    <h5 class="mb-2 text-2xl font-bold tracking-tight  text-slate-300">Most prominent tags</h5>
    <WordCloud {...config} />
  </div>
  );
};

export default GenreTagsWordCloud
