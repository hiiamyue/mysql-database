import React from 'react'
import "./App.css";

import Home from './pages/Home'
import Movies from './pages/Movies'
import Search from './pages/Search'
import Genres from './pages/Genres'
import Genre from './pages/Genre'
import Movie from './pages/Movie'
import ErrorPage from './pages/ErrorPage'
import {BrowserRouter, Route, Routes} from "react-router-dom";

function App() {
  
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path='/movies/*' element={<Movies />} />
        <Route path='/search/*' element={<Search />} />
        <Route path='/movie/*' element={<Movie />} />
        <Route path='/genres/*' element={<Genres />} />
        <Route path='/genre/*' element={<Genre />} />
        <Route path='/*' element={<ErrorPage />} />
      </Routes>
    </BrowserRouter>

  )
}

export default App;