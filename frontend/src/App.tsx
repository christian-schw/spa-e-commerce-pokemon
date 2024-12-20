import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import teaser1 from './assets/teaser/teaser1-picture-description-stats.png'
import teaser2 from './assets/teaser/teaser2-facts.png'
import teaser3 from './assets/teaser/teaser3-evolution.png'
import teaser4 from './assets/teaser/teaser4-tablet-view.png'
import teaser5 from './assets/teaser/teaser5-mobile-view.png'


function App() {
  /*
   Test Flask API. 
   TODO: Delete test code when the backend has been configured and implemented correctly.
  */
  const [users, setUsers] = useState([])

  /*
    TODO: Delete teaserImages when more content is available.

    Hardcoded the strings of the teaser images and
    not dynamically fetched from folders, as this
    is only a **temporary** feature. That's why I
    preferred speed over an elegant, scalable solution.

    At the moment I don't know the best way to solve this
    dynamically, so I didn't want to install and
    set up any extra dependencies like Webpack
  */
  const [teaserImages, setTeaserImages] = useState([
    {
      src: teaser1,
      alt: "Teaser: Overview of the Pokemon"
    },
    {
      src: teaser2,
      alt: "Teaser: Tab - Facts"
    },
    {
      src: teaser3,
      alt: "Teaser: Pokemon Evolution"
    },
    {
      src: teaser4,
      alt: "Teaser: View - Tablet Device"
    },
    {
      src: teaser5,
      alt: "Teaser: View - Smartphone Device"
    }
  ])

  // Improve in future: Store it globally
  const pokemonAPI = {
    domain: {
      // Local Development Server started with Flask
      dev: "http://127.0.0.1:5000",
      // Hosted API
      prod: "https://data-factories.com"
    }
  }

  // TODO: Implement error handling axios
  const fetchUsers = async () => {
    const response = await axios.get(pokemonAPI.domain.prod.concat("/test-api/test1"))
    console.log(response.data.users)
    setUsers(response.data.users)
  }

  const healthCheck = async () => {
    const response = await axios.get(pokemonAPI.domain.prod.concat("/health-check"))
    console.log(response.data)
  }

  useEffect(() => {
    fetchUsers()
    healthCheck()
  }, [])


  return (
    <>
      <h1>Welcome to the Trainer's Trove!</h1>
      {/*<p>
        // Testing Flask API
        {
          users.map((user, index) => (
            <span key={index}>User: {user}<br /></span>
          ))
        }
      </p>*/}
      <p>
        The project is an e-commerce shop where you can browse, buy and collect Pokémon.<br></br>
        The project is still in the development phase. To get you excited about it, here are a few teaser
        images:
      </p>
      <div>
        {
          teaserImages.map(
            (image, index) => <img key={index} src={image.src} alt={image.alt}></img>
          )
        }
      </div>
    </>
  )
}

export default App
