import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)

  // Test Flask API. TODO: Delete all code later.
  const [users, setUsers] = useState([])

  // NOTE: Improve in future. Store it globally
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
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          {/* Test Flask API */}
          {
            users.map((user, index) => (
              <span key={index}>User: {user}<br /></span>
            ))
          }
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
