import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  /*
      Flask runs the backend and Vite the frontend.
      To integrate both of them for a full-stack project,
      you need to connect the two technologies
      so that Flask takes over the backend and the frontend as well
      during development.

      These two parts communicate via HTTP requests (API calls).
      Vite serves as a separate server for the frontend in
      development mode, while Flask delivers both the
      frontend and the backend in production mode.

      During development, the Vite server runs independently of the Flask server.
      To enable Vite to access the Flask backend,
      a proxy is set up that forwards API calls
      from http://localhost:5173 (Vite) to http://localhost:5000 (Flask).

      *** NOTE ***:
      In production version, the server object can be omitted!
  */
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
    },
  },
})
