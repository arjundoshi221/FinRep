import { Button, TextField } from "@mui/material"
import useForm from "../helpers/useForm";
import { useState } from "react";
import validator from "validator";
import { useDispatch } from "react-redux";
import { authLogin } from "../reducers/authReducer";
import { useNavigate } from "react-router-dom";


const SignIn=()=>{
    const dispatch=useDispatch();
    const navigation = useNavigate();
 
    
    const [formValues, handleInputChange] = useForm({
        email: "",
        password: "",
      });
    
      const {email,password} = formValues;
      const [error,setError]=useState('');
      console.log(error)

      const isFormValid = () => {
        if (!validator.isEmail(email)) {
          (setError("Email is not valid"));
          return false;
        } else if (
          !validator.isStrongPassword(password.toString()) ||
          password.length > 32
        ) {
          (
            setError(
              "Password should be between 8-32 characters and should include 1 number, 1 symbol, 1 lowercase and 1 uppercase"
            )
          );
          return false;
        } 
       
        return true;
      };

      const handleSubmit=async()=>{
        if(isFormValid()){
            

            
            await fetch('/api/user/login', {
               method:'POST',
                headers: {
                  "Content-Type": "application/json",
                },
               /*  body: JSON.stringify(name,email,password), */
               body:JSON.stringify({email:email,password:password})
              }).then((resp) =>(resp.json()))
              .then((data) => {
                
               if (data.ok) {
                  const { user, token,navigate } = data;
                 console.log(user)
                  dispatch(authLogin(user))
                  
        
                  localStorage.setItem("token", token);
                  localStorage.setItem("user",JSON.stringify(user))
                  localStorage.setItem("token-init-date", new Date().getTime());
                  console.log(navigate)
                  navigation(navigate)
        
                }
                 else {
                  if (data.errors) console.log(data.errors);
                  
                }
              })
        }

      }

    return(
        <div class='container'>
        <div>
        <p class="font-weight-bold h3"> Welcome Back</p>
       
        </div>

        <div class='mt-4'>
            Welcome Back! Please enter your details
        </div>

        <div className='mt-5 px-5'>
            <TextField id="standard-basic" label="Enter your Email" variant="outlined" fullWidth='true'  value={email}
                onChange={handleInputChange}  name="email"/>
        </div>

        <div class='mt-4 px-5'>
            <TextField id="standard-basic" label="Password" variant="outlined" type='password' fullWidth='true'  value={password}
                onChange={handleInputChange}  name="password"/>
        </div>

        <div class='mt-4 px-5'>
        <Button variant="contained" fullWidth='true' onClick={()=>handleSubmit()}>Sign In</Button>
        </div>

        {error}
        </div>
    )


}
export default SignIn