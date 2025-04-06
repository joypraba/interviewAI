import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import App from './App.jsx'

createRoot(document.getElementById('root-component')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
