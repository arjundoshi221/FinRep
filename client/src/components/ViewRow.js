import React  from "react";
import { useNavigate } from "react-router-dom";

const ViewRow=({data})=>{
    const Analyst_CompanyName = data["Analyst_CompanyName"]
    const Analyst_DateofUpload = data["Analyst_DateofUpload"]
    const Analyst_Name = data["Analyst_Name"]
    const Analyst_Notes = data["Analyst_Notes"]
    const Analyst_Source = data["Analyst_Source"]
    const Analyst_TimeofUpload = data["Analyst_TimeofUpload"]
    const Content = data["Content"]
    const Source = data["Source"]
    const Source_ticker = data["Source_ticker"]
    const Ticker = data["Ticker"]
    const Time = data["Time"]
    const Title = data["Title"]
    
    const navigation=useNavigate()


    function ViewDetail(){

        //navigate to details
        navigation('/viewdetail',{
            state:{
                Analyst_CompanyName:Analyst_CompanyName,
                Analyst_DateofUpload:Analyst_DateofUpload,
                Analyst_Name:Analyst_Name,
                Analyst_Notes:Analyst_Notes,
                Analyst_Source:Analyst_Source,
                Analyst_TimeofUpload:Analyst_TimeofUpload,
                Content:Content,
                Source:Source,
                Source_ticker:Source_ticker,
                Ticker:Ticker,
                Time:Time,
                Title:Title
            }
        })
    }
    return (
        
            <a onClick={ViewDetail}>
            <div style={{display:'flex' ,flexDirection:'row',flex:4,justifyContent:'flex-start', marginBottom: '20px' ,marginTop:'20px'}}>
                <div style={{flex:1}}>
                    {Analyst_Name}
                </div>

                <div style={{flex:1}}>
                    {Analyst_DateofUpload}
                </div>

                <div style={{flex:1}}>
                    {Analyst_Source}
                </div>

                <div style={{flex:1}}>
                    {Analyst_CompanyName}
                </div>

                <div style={{flex:1}}>
                    {Title}
                </div>
            </div>
            </a>
        
    )



}

export default ViewRow