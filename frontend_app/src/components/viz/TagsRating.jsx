import React, { useState, useEffect } from 'react';
import { Column } from '@ant-design/plots';

const TagsRating = ({movieid}) => {
    
    const [tagsRating, setTagsRating] = useState([]);
    const [hasFetchedTags, setFetchedTags] = useState(false)

    useEffect(() => {
        asyncFetch();
    })

    const asyncFetch = () => {
    
        fetch(`http://localhost:8000/q4_1_tag_rating?movie_id=${movieid}`)
          .then((response) => response.json())
          .then((json) => {
            setTagsRating(json)
            config["data"] = json
            setFetchedTags(true)
          })
          .catch((error) => {
            console.log('fetch data failed', error);
          });
    };

    const config = {
        data: tagsRating,
        xField: 'tag',
        yField: 'rating',
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
        <a class="mx-8 xl:mx-0 mt-4 flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
            <div className='text-center w-full px-8 py-8'>
            <h4 className='md:text-lg sm:text-6xl text-4xl font-bold text-white'>Tags</h4>
            <p className='pt-4 text-slate-400 pb-4'>What tags did this movie get? What is the average rating for movies with these tags?</p>
            {hasFetchedTags ?
                <div className='inline-block'>
                    {tagsRating.map((tag) => (
                        <span class="bg-fuchsia-300 text-pink-900 hover:text-fuchsia-300 hover:bg-pink-900 text-lg font-medium mr-2 px-3 py-0.5 rounded inline-block  mt-2 lg:mt-0">{tag.tag}</span>
                    ))} 
                </div>  
            :
                <p className='pt-4 text-center'>Fetching tags...</p>
            }
            </div>
            <div className='w-full p-8 items-center'>
            {hasFetchedTags ?
                <Column {...config} />
            :
                <p className='pt-4 text-center'>...</p>
            }
            </div>
        </a>
    );
}

export default TagsRating