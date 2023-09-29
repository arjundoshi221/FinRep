import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AnalystForm from './pages/UploadNews';
import ViewData from './pages/ViewData';
import ViewDetail from './pages/ViewDetail';

function App() {
  
  return (
    <div className="App">
    
    
    <BrowserRouter>

      <div>

        <Routes>

        <Route 
            path="/" 
            element={<AnalystForm/>} 
          />   
           <Route 
            path="/view" 
            element={<ViewData/>} 
          />   
           <Route 
            path="/viewdetail" 
            element={<ViewDetail/>} 
          />   
            
         
        </Routes>
      </div>
    </BrowserRouter>
  </div>
  );
}

export default App;
