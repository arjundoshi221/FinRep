import React, { useState } from 'react';
import ViewRow from '../components/ViewRow';
import { useNavigate } from "react-router-dom"


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

            <div>
            {newsData.map((item) => {
                return (
                        
                <div key={item.id} style={{flexDirection:'column',flex:1,backgroundColor:'lightblue'}}>
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
