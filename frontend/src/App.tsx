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
      alt: "Teaser: Overview of the Pokemon",
      class: "teaser-image"
    },
    {
      src: teaser2,
      alt: "Teaser: Tab - Facts",
      class: "teaser-image"
    },
    {
      src: teaser3,
      alt: "Teaser: Pokemon Evolution",
      class: "teaser-image"
    },
    {
      src: teaser4,
      alt: "Teaser: View - Tablet Device",
      class: "teaser-image"
    },
    {
      src: teaser5,
      alt: "Teaser: View - Smartphone Device",
      class: "teaser-image"
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

  const fetchUsers = async () => {
    const response = await axios.get(pokemonAPI.domain.prod.concat("/test-api/test1"))
      .then(response => {
        console.log(response.data.users)
        setUsers(response.data.users)
      })
      .catch(error => {
        console.log("Failed attempt to fetch users.")
      })
  }

  const healthCheck = async () => {
    const response = await axios.get(pokemonAPI.domain.prod.concat("/health-check"))
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log("Health check failed. API could not be reached.")
      })
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
        The project is still in the development phase. The code and other parts of the project can be found in the <a href="https://github.com/christian-schw/spa-e-commerce-pokemon" target="_blank">GitHub repository</a>.<br></br>
        To get you excited about it, here are a few teaser images from the design mockups of my designer (<a href="https://www.combine-visual.com/" target="_blank">combine visual - Christine Biendl</a>):
      </p>
      <div>
        {
          teaserImages.map(
            (image, index) => <img key={index} className={image.class} src={image.src} alt={image.alt}></img>
          )
        }
      </div>
      <p>
        Have a great time!<br></br>
        <br></br>
        Greetings from the developer<br></br>
        <br></br>
        <br></br>
        Christian Schwanse
      </p>
    </>
  )
}

export default App
