import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import './Login.css';
import sneaker from '../assets/finance.png'
import SignIn from '../components/SignIn';
import { useState } from 'react';
import Register from '../components/Register';

const Login=()=>{
    const [signup,setSignup]=useState(false);

    function changeForm(){
        setSignup(!signup)
    }

    return(


         <div class='main-container'>

        <div class='container rounded-4 p-5 h-100'>

        <div class='row rounded_container h-100 rounded-4'>
            
            
            <div class='col-lg-5 text-center login h-100 rounded-4' >

               {signup?
                (<Register/>):
                <SignIn/>
                }
                
                <div class='mt-4'>
                    <p>

                        {signup?(<>Have an account? <Button onClick={()=>{changeForm()}}>Login</Button></>):
                        
                <>Dont have an account? <Button onClick={()=>{changeForm()}}>Sign Up</Button></>
            }
                    </p>
                </div>


            </div>



            <div class='col-lg-7 image-bg h-100 rounded-4'>
                <div class='row h-100' >

                    
                    <img src={sneaker} alt='Sneaker' class="img-fluid"></img>
                   

                </div>
            </div>


        </div>
        </div>
        </div>
    )



}
export default Login