import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Chatter from './pages/Chatter'

function App() {
  return (
  <Router>
    <Routes>
      <Route path="/home" element={<Home />} />
      <Route path="/" element={<Chatter />} />
    </Routes>
  </Router>
  )
}

export default App 
