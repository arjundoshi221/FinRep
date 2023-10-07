import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AnalystForm from './pages/UploadNews';
import ViewData from './pages/ViewData';
import ViewDetail from './pages/ViewDetail';
import Login from './pages/Login';
import SignInSide from './pages/SignInSIde';

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
           <Route 
            path="/login" 
            element={<Login/>} 
          />  
           <Route 
            path="/signinside" 
            element={<SignInSide/>} 
          />  
            
         
        </Routes>
      </div>
    </BrowserRouter>
  </div>
  );
}

export default App;
