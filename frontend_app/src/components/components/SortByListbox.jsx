import { Fragment, useEffect, useState } from 'react'
import { Listbox, Transition } from '@headlessui/react'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/react/20/solid'
import { useSearchParams } from 'react-router-dom';

const sortBy = [
  { by: 'Sort by:', sortby: "default" },
  { by: 'Rating, Ascending', sortby:"rating" },
  { by: 'Rating, Descending', sortby: "rating_DESC" },
  { by: 'Date, Ascending', sortby: "date" },
  { by: 'Date, Descending', sortby: "date_DESC" },
  { by: 'Title, A-to-z', sortby: "title" },
  { by: 'Title, z-to-A', sortby: "title_DESC" },
]




export default function SortByListbox() {

  const [selected, setSelected] = useState(sortBy[0])
  const [searchParams, setSearchParams] = useSearchParams();

  useEffect(() => {
    if (!(selected.sortby === 'default')){
      searchParams.set("sortby", selected.sortby)
      searchParams.delete("page")
      setSearchParams(searchParams)
    } else {
      searchParams.delete("sortby")
      setSearchParams(searchParams)
    }
    
  }, [selected]);

  return (
    <div className="w-72 h-20 pt-0">
      <Listbox value={selected} onChange={setSelected}>
        <div className="mt-0">
          <Listbox.Button className="h-10 w-full cursor-default rounded-md bg-white py-0 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm">
            <span className="block truncate text-black">{selected.by}</span>
            <span className="pointer-events-none absolute inset-y-0  right-[16em]  top-[0.4em] xl:top-[-0.2em] md:top-[-0.2em] md:right-[18em] flex items-center">
              <ChevronUpDownIcon
                className="h-5 w-5 text-gray-400 mt-[-2.8em] right-[40em]"
                aria-hidden="true"
              />
            </span>
          </Listbox.Button>
          <Transition
            as={Fragment}
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <Listbox.Options className="absolute mt-1 max-h-60 w-[10.2rem] overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-10">
              {sortBy.map((person, personIdx) => (
                <Listbox.Option
                  key={personIdx}
                  className={({ active }) =>
                    `relative cursor-default select-none py-2 pl-10 pr-4 ${
                      active ? 'bg-sky-100 text-slate-900' : 'text-gray-900'
                    }`
                  }
                  value={person}
                >
                  {({ selected }) => (
                    <>
                      <span
                        className={`block truncate ${
                          selected ? 'font-medium' : 'font-normal'
                        }`}
                      >
                        {person.by}
                      </span>
                      {selected ? (
                        <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-fuchsia-600">
                          <CheckIcon className="h-5 w-5" aria-hidden="true" />
                        </span>
                      ) : null}
                    </>
                  )}
                </Listbox.Option>
              ))}
            </Listbox.Options>
          </Transition>
        </div>
      </Listbox>
    </div>
  )
}
