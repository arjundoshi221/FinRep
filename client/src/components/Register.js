import { Button, TextField } from "@mui/material"
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import validator from "validator";
import useForm from "../helpers/useForm";
import { authLogin } from "../reducers/authReducer";
import { Navigate } from "react-router-dom";
import { useNavigate } from "react-router-dom";


const Register=()=>{
    const navigation=useNavigate()
    const dispatch=useDispatch();
    const [formValues, handleInputChange] = useForm({
        name: "",
        email: "",
        password: "",
        password2: "",
      });
      const { name, email, password, password2 } = formValues;

      const [error,setError]=useState(false);

      const handleSubmit=async()=>{
       let  url='/auth/register';
        if(isFormValid()){
            console.log(name,email,password)

            
            await fetch('/api/user/register', {
               method:'POST',
                headers: {
                  "Content-Type": "application/json",
                },
               /*  body: JSON.stringify(name,email,password), */
               body:JSON.stringify({name:name,email:email,password:password})
              }).then((resp) =>(resp.json()))
              .then((data) => {
                console.log(data)
               if (data.ok) {
                  const { user, token ,navigate} = data;
                 console.log(user)
                  dispatch(authLogin(user))
                  
        
                  localStorage.setItem("token", token);
                  localStorage.setItem("user", JSON.stringify(user));
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

      const isFormValid = () => {
        if (name.trim().length === 0) {
         (setError("Name is required"));
          return false;
        } else if (name.trim().length > 32) {
          (setError("Name length must be max 32 characters"));
          return false;
        } else if (!validator.isEmail(email)) {
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
        } else if (password !== password2) {
         (setError("Passwords should match"));
          return false;
        }
       
        return true;
      };
    
    return(
        <div class='container'>
        <div>
        <p class="font-weight-bold h3"> Sign Up</p>
       
        </div>

        <div class='mt-3'>
            Enter your details to Sign Up!
        </div>

        <div className='mt-4 px-5'>
            <TextField id="standard-basic" label="Enter your name" variant="outlined" fullWidth='true' value={name}  name="name"
                onChange={handleInputChange}/>
        </div>

        <div className='mt-4 px-5'>
            <TextField id="standard-basic" label="Enter your Email" variant="outlined" fullWidth='true' value={email}
                onChange={handleInputChange}  name="email"/>
        </div>

        <div class='mt-4 px-5'>
            <TextField id="standard-basic" label="Password" variant="outlined" type='password' fullWidth='true' value={password} name="password"
                onChange={handleInputChange}/>
        </div>

        <div class='mt-4 px-5'>
            <TextField id="standard-basic" label="Confirm Password" variant="outlined" type='password' fullWidth='true' value={password2} name="password2"
                onChange={handleInputChange}/>
        </div>

        <div class='mt-4 px-5'>
        <Button variant="contained" fullWidth='true' onClick={()=>handleSubmit()}>Sign Up</Button>
        </div>


        {error}
        
        </div>
    )


}
export default Register