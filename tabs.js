import React, { useState } from "react";
import TabNavItem from "../V2/TabNavItem";
import TabContent from "../V2/TabContent";
import CommonForm from './CommonForm';

const Tabs = () => {
  const [activeTab, setActiveTab] = useState("tab1");

  const handleFormSubmit = (formData) => {
    const apiData = {
      // Construct API data object based on formData and activeTab
      tabName: activeTab,
      formData,
    };

    // Replace with your actual API call logic, including error handling
    fetch('/your-api-endpoint', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(apiData),
    })
      .then(response => response.json())
      .then(data => console.log('API response:', data))
      .catch(error => console.error('API call error:', error));
  };

  return (
    <div className="Tabs">
      {/* ... existing code for tab navigation */}

      <div className="outlet">
        <TabContent id="tab1" activeTab={activeTab}>
          <CommonForm activeTab="tab1" onSubmit={handleFormSubmit} />
        </TabContent>
        <TabContent id="tab2" activeTab={activeTab}>
          <CommonForm activeTab="tab2" onSubmit={handleFormSubmit} />
        </TabContent>
        <TabContent id="tab3" activeTab={activeTab}>
          <CommonForm activeTab="tab3" onSubmit
