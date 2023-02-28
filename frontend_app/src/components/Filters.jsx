import { Popover, Transition } from '@headlessui/react'
import { ChevronDownIcon } from '@heroicons/react/20/solid'
import { Fragment } from 'react'
import Slider from '@mui/material/Slider';
import AutocompleteGenres from './AutocompleteGenres';
import * as React from 'react';
import {Link} from "react-router-dom";
import { useSearchParams } from 'react-router-dom';
import buildFiltersURL from '../utils/StringUtils';
import { getRatingFilter, getGenreFilter, getDateFilter } from '../utils/QueryUtils';

const people = [
  { id: 1, name: 'Wade Cooper' },
  { id: 2, name: 'Arlene Mccoy' },
  { id: 3, name: 'Devon Webb' },
  { id: 4, name: 'Tom Cook' },
  { id: 5, name: 'Tanya Fox' },
  { id: 6, name: 'Hellen Schmidt' },
]


export default function Filters() {

  
  const [searchParams, setSearchParams] = useSearchParams();
  let ratingFilter = getRatingFilter(searchParams)
  let dateFilter = getDateFilter(searchParams)
  let genres = getGenreFilter(searchParams, people)
  
  React.useEffect(() => {
    // Handle errors where wrong filters are entered
    // TODO: Do the same for all???
    if (typeof genres[-1] == 'undefined' & genres.length === 1){
        searchParams.delete('genres')
        setSearchParams(searchParams)
    

    }
  }, [searchParams, setSearchParams, genres]);

  const [valueRating, setValueRating] = React.useState(ratingFilter)
  const [valueDate, setValueDate] = React.useState(dateFilter) 
  const [valueGenre, setValueGenre] = React.useState(genres);

  function submitFilters(){
    searchParams.set("min_rating", valueRating[0])
    searchParams.set("max_rating", valueRating[1])
    searchParams.set("from", valueDate[0])
    searchParams.set("to", valueDate[1])
    setSearchParams(searchParams)
  }

  const handleChangeGenre = (genres) => {
    setValueGenre(genres);
  
  }

  const handleChangeRating = (event, newValue) => {
    
    setValueRating(newValue);
  };

  const handleChangeDate = (event, newValue) => {
    
    setValueDate(newValue);
  };
  


  return (
    <div className="w-full max-w-sm px-4">
      <Popover className="relative">
        {({ open }) => (
          <>
            <Popover.Button
              className={`
                ${open ? '' : 'text-opacity-90'}
                group inline-flex items-center rounded-md bg-slate-700 px-3 py-2 text-base font-medium text-white hover:text-opacity-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75`}
            >
              <span>Filters</span>
              <ChevronDownIcon
                className={`${open ? '' : 'text-opacity-70'}
                  ml-2 h-5 w-5 text-slate-300 transition duration-150 ease-in-out group-hover:text-opacity-80`}
                aria-hidden="true"
              />
            </Popover.Button>
            <Transition
              as={Fragment}
              enter="transition ease-out duration-200"
              enterFrom="opacity-0 translate-y-1"
              enterTo="opacity-100 translate-y-0"
              leave="transition ease-in duration-150"
              leaveFrom="opacity-100 translate-y-0"
              leaveTo="opacity-0 translate-y-1"
            >
              <Popover.Panel className="absolute left-1/2 mt-3 w-60 max-w-sm -translate-x-[80%] transform px-4 sm:px-0 lg:max-w-3xl mr-80 z-10">
                <div className="overflow-hidden rounded-lg shadow-lg ring-1 ring-black ring-opacity-5">
                  <div className="relative grid gap-8 bg-white p-7 lg:grid-cols-1">                 
                    
                    <div
                          className=" text-black -m-3 flex items-center rounded-lg p-2 transition duration-150 ease-in-out hover:bg-gray-50 focus:outline-none focus-visible:ring focus-visible:ring-orange-500 focus-visible:ring-opacity-50 pb-[3.2rem]"
                    >
                      <div className="ml-2 xl:ml-4">
                          <p className="text-sm font-medium text-gray-900">
                            Genre
                          </p>
                          <p className="text-sm text-gray-500">
                            Filter genres.
                          </p>
                          
                          <AutocompleteGenres handleChangeGenre={handleChangeGenre} initialValue={valueGenre} values={people} />
                          
                          
                      </div>
                    </div>

                    <div
                        
                        className=" text-black -m-3 flex items-center rounded-lg p-2 transition duration-150 ease-in-out hover:bg-gray-50 focus:outline-none focus-visible:ring focus-visible:ring-orange-500 focus-visible:ring-opacity-50"
                    >
                      <div className="ml-2 xl:ml-4">
                          <p className="text-sm font-medium text-gray-900">
                            Release date
                          </p>
                          <p className="text-sm text-gray-500">
                            Movie relase date
                          </p>
                          <Slider
                            getAriaLabel={() => 'Release date'}
                            value={valueDate}
                  
                            onChange={handleChangeDate}
                            valueLabelDisplay="auto"
                            min={1800}
                            max={2023}
                            
                            color="secondary"
                          />
                      </div>
                    </div>
                    
                    <div
                        
                        className=" text-black -m-3 flex items-center rounded-lg p-2 transition duration-150 ease-in-out hover:bg-gray-50 focus:outline-none focus-visible:ring focus-visible:ring-orange-500 focus-visible:ring-opacity-50"
                    >
                      <div className="ml-2 xl:ml-4">
                        <p className="text-sm font-medium text-gray-900">
                          Rating
                        </p>
                        <p className="text-sm text-gray-500">
                          Rating min & max
                        </p>
                        <Slider
                          getAriaLabel={() => 'Rating'}
                          value={valueRating}
                          marks={true}
                          onChange={handleChangeRating}
                          valueLabelDisplay="auto"
                          min={0}
                          max={5}
                          color="secondary"
                        />
                      </div>
                      
                    </div>
                    <div
                        className=" text-black -m-3 flex items-center rounded-lg p-2 transition duration-150 ease-in-out hover:bg-gray-50 focus:outline-none focus-visible:ring focus-visible:ring-orange-500 focus-visible:ring-opacity-50"
                      >
                        <div className='ml-2 xl:ml-4'>
                          
                          
                        <button onClick={submitFilters} className='xl:px-14  px-12 md:px-14  sm:px-14 font-semibold transition ease-in-out delay-150 bg-gradient-to-r from-pink-200 to-fuchsia-300  hover:bg-gradient-to-r hover:to-blue-300 hover:from-sky-200 duration-300  opacity-80 my-6 mx-auto py-3 mt-8 w-full rounded-md text-black drop-shadow-2xl'>Submit</button>
                          
                        </div>
                      </div>
                  </div>
                  
                </div>
              </Popover.Panel>
            </Transition>
          </>
        )}
      </Popover>
    </div>
  )
}

