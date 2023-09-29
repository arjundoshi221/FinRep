import React from "react";
import { useLocation } from "react-router-dom";

const ViewDetail=({})=>{
    const location=useLocation();
   
    const item=location.state


    return (
        <div>
      <div>
        <strong>Analyst Company Name:</strong> {item.Analyst_CompanyName}
      </div>
      <div>
        <strong>Analyst Date of Upload:</strong> {item.Analyst_DateofUpload}
      </div>
      <div>
        <strong>Analyst Name:</strong> {item.Analyst_Name}
      </div>
      <div>
        <strong>Analyst Notes:</strong> {item.Analyst_Notes}
      </div>
      <div>
        <strong>Analyst Source:</strong> {item.Analyst_Source}
      </div>
      <div>
        <strong>Analyst Time of Upload:</strong> {item.Analyst_TimeofUpload}
      </div>
      <div>
        <strong>Content:</strong> {item.Content}
      </div>
      <div>
        <strong>Source:</strong> {item.Source}
      </div>
      <div>
        <strong>Source Ticker:</strong> {item.Source_ticker}
      </div>
      <div>
        <strong>Ticker:</strong> {item.Ticker}
      </div>
      <div>
        <strong>Time:</strong> {item.Time}
      </div>
      <div>
        <strong>Title:</strong> {item.Title}
      </div>
    </div>
    )




}
export default ViewDetail;