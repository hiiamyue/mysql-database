const MovieCard = ({title, release_date}) => {


    return (
        <div className='text-slate-100'>
                        <div className=" text-lg font-bold text-center  rounded-2xl m-4">
                            <img
                                    src="samplecover.png"
                                    className="rounded-2xl w-full h-100 object-cover hover:opacity-60 shadow-lg"
                                    alt="..."
                            />
                            <p>{title}</p>
                            <div className="flex justify-center space-x-4">
                                <p className="font-light text-base m-0">{release_date}</p>
                                <p className="font-light text-sm  m-0 text-sky-200 mt-[0.25em]">4.93</p>
                            </div>
                        </div>
                    </div>
    )
}

export default MovieCard