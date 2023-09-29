import React, { useState } from 'react';
import './AnalystForm.css';
function AnalystForm() {
  const [formData, setFormData] = useState({
    analystName: 'Arjun',
    timeInputted: '',
    source: '',
    dateOfUpload: '',
    notes: '',
    companyName: '',
    file:null
  });

  const [errorMsg,setErrorMsg]=useState('')
  //const [pdfFile, setPdfFile] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleFileInputChange = (event) => {
    setFormData({
      ...formData,
      file: event.target.files[0],
    });
  };

  const handleSubmit = async (e) => {
    const date = new Date();
    formData['timeInputted']=date.toLocaleTimeString()
    formData['dateOfUpload']=date.toLocaleDateString()


    const formDataToSend = new FormData();
    formDataToSend.append('analystName', formData.analystName);
    formDataToSend.append('source', formData.source);
    formDataToSend.append('notes', formData.notes);
    formDataToSend.append('companyName', formData.companyName);
    formDataToSend.append('timeInputted', formData.timeInputted);
    formDataToSend.append('dateOfUpload', formData.dateOfUpload);
    formDataToSend.append('file', formData.file);

    
    e.preventDefault();
    // Access form data from formData state
    console.log('Form Data:', formData);
    
    await fetch('/uploader', {
      method:'POST',
       headers: {
        // "Content-Type": "multipart/form-data",
       },
     
      body:formDataToSend
     }).then((resp)=>{
      return resp.json()
      
     }).then((data)=>{
      console.log(data)
      setErrorMsg(data.status)
     }).catch((error) => {
      console.error('Error:', error);
    })
    // You can also send the PDF file to your server here
  };

  return (
    <div>
      <h1>Analyst Form</h1>
      <form onSubmit={handleSubmit}>
      <div>
          <label>Name of Analyst:</label>
          <select
            name="analystName"
            value={formData.analystName}
            onChange={handleInputChange}
          >
            <option value="Arjun">Arjun</option>
            <option value="Ishan">Ishan</option>
            <option value="Siddhant">Siddhant</option>
            <option value="Jai">Jai</option>
          </select>
        </div>
       
        <div>
          <label>Source:</label>
          <input
            type="text"
            name="source"
            value={formData.source}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Notes:</label>
          <textarea
            name="notes"
            value={formData.notes}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label>Name of Company:</label>
          <input
            type="text"
            name="companyName"
            value={formData.companyName}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Upload PDF:</label>
          <input
            type="file"
            name='file'
            accept=".pdf"
            onChange={handleFileInputChange}
            required
            
          />
        </div>
        <div>
          {errorMsg}
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
}

export default AnalystForm;
