import { configureStore } from '@reduxjs/toolkit'
import authSlice from './reducers/authReducer';


export default configureStore({
  reducer: {auth:authSlice},
})