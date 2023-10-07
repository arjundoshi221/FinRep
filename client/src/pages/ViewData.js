import React, { useState } from 'react';
import ViewRow from '../components/ViewRow';
import { useNavigate } from "react-router-dom"
import './ViewData.css';



const ViewData=()=>{

    const [newsData,setData]=useState();
   

    const fetchData= async()=>{
        await fetch('/view',{
            method:'GET',

        }).then((resp)=>(resp.json()))
        .then((data)=>{
            
            setData(data)
        })
    }

    useState(()=>{
        fetchData()
    },[])

    return(
        <html>
            {newsData!=undefined?

        <div  style={{margin:150}}>
            <div style={{alignSelf: 'stretch', height: 56, justifyContent: 'flex-start',display: 'flex',flexDirection:"row",flex:1}}>
              

              <div style={{flex:1}}>

               <div className='header'>
                Name
               </div>
               </div>

               <div className='header' style={{flex:1}}>
                Company
               </div>

               <div  className='header' style={{marginRight:50}}>
                Uploaded File
               </div>

               <div  className='header'>
                Date Uploaded
               </div>

               


               <div  className='header'>
                Source
               </div>


            </div>
            {newsData.map((item) => {
                return (
                        
                <div key={item.id} style={{flexDirection:'column',flex:1}}>
                    <ViewRow key={item.id} data={item}/>
                </div>
                    );
                        
                        
                    })}
            </div>
                :
                <div></div>
        }


        </html>
    )


}
export default ViewData;
